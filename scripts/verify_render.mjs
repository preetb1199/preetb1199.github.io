#!/usr/bin/env node
/**
 * Zero-dependency headless Chrome regression verifier (Node 22+ built-in WebSocket).
 * Verifies desktop & mobile rendering, light/dark theme toggle, interactive tabs,
 * zero JS console/runtime errors, and loaded images across key pages.
 *
 * Usage: node scripts/verify_render.mjs [baseUrl]
 */
import { spawn } from "node:child_process";

const BASE = (process.argv[2] || "http://127.0.0.1:8771").replace(/\/$/, "");
const PAGES = [
  "/",
  "/publications.html",
  "/research/",
  "/research/agentsentry.html",
  "/research/metaaudit.html",
  "/research/cora.html",
  "/research/prompt-injection-screening.html",
  "/research/ligo-monitoring.html",
  "/research/cost-aware-llm-judges.html",
  "/research/gaming-the-gatekeeper.html",
  "/research/rai-gate.html",
  "/research/opsagent-rl.html",
];

function launchChrome() {
  return new Promise((resolve, reject) => {
    const proc = spawn(
      "google-chrome",
      [
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--remote-debugging-port=0",
        "--disable-background-networking",
        "--disable-default-apps",
        "about:blank",
      ],
      { stdio: ["ignore", "pipe", "pipe"] }
    );
    let stderr = "";
    const onData = (chunk) => {
      stderr += chunk.toString();
      const m = stderr.match(/DevTools listening on (ws:\/\/[^\s]+)/);
      if (m) {
        proc.stderr.off("data", onData);
        resolve({ proc, wsUrl: m[1] });
      }
    };
    proc.stderr.on("data", onData);
    proc.on("error", reject);
    setTimeout(() => reject(new Error("Chrome startup timeout: " + stderr)), 15000);
  });
}

class CDP {
  constructor(wsUrl) {
    this.ws = new WebSocket(wsUrl);
    this.id = 0;
    this.pending = new Map();
    this.events = [];
    this.ready = new Promise((res, rej) => {
      this.ws.addEventListener("open", res);
      this.ws.addEventListener("error", rej);
    });
    this.ws.addEventListener("message", (ev) => {
      const msg = JSON.parse(ev.data.toString());
      if (msg.id && this.pending.has(msg.id)) {
        const { res, rej } = this.pending.get(msg.id);
        this.pending.delete(msg.id);
        if (msg.error) rej(new Error(msg.error.message));
        else res(msg.result);
      } else if (msg.method) {
        this.events.push(msg);
      }
    });
  }
  send(method, params = {}, sessionId = undefined) {
    const id = ++this.id;
    const payload = { id, method, params };
    if (sessionId) payload.sessionId = sessionId;
    return new Promise((res, rej) => {
      this.pending.set(id, { res, rej });
      this.ws.send(JSON.stringify(payload));
    });
  }
  close() {
    this.ws.close();
  }
}

async function main() {
  const { proc, wsUrl } = await launchChrome();
  const cdp = new CDP(wsUrl);
  await cdp.ready;

  let failures = 0;
  try {
    const { targetId } = await cdp.send("Target.createTarget", { url: "about:blank" });
    const { sessionId } = await cdp.send("Target.attachToTarget", { targetId, flatten: true });
    await cdp.send("Page.enable", {}, sessionId);
    await cdp.send("Runtime.enable", {}, sessionId);
    await cdp.send("Log.enable", {}, sessionId);

    for (const path of PAGES) {
      const url = `${BASE}${path}`;
      const pageErrors = [];
      cdp.events = [];

      // Desktop viewport check
      await cdp.send(
        "Emulation.setDeviceMetricsOverride",
        { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false },
        sessionId
      );
      await cdp.send("Page.navigate", { url }, sessionId);
      await new Promise((r) => setTimeout(r, 900));

      const desktop = await cdp.send(
        "Runtime.evaluate",
        {
          returnByValue: true,
          expression: `(() => {
            const imgs = [...document.querySelectorAll('img')].filter(i => {
              const s = getComputedStyle(i);
              return s.display !== 'none' && s.visibility !== 'hidden' && i.loading !== 'lazy';
            });
            const broken = imgs.filter(i => !i.complete || i.naturalWidth === 0).map(i => i.getAttribute('src'));
            const themeBefore = document.documentElement.getAttribute('data-theme');
            const toggle = document.querySelector('[data-theme-toggle]');
            if (toggle) toggle.click();
            const themeAfter = document.documentElement.getAttribute('data-theme');
            if (toggle) toggle.click();
            const tab = document.querySelector('[role="tab"][aria-selected="false"]');
            let tabWorked = true;
            if (tab) {
              tab.click();
              tabWorked = tab.getAttribute('aria-selected') === 'true' || tab.classList.contains('is-active');
            }
            return {
              title: document.title,
              overflow: document.documentElement.scrollWidth - window.innerWidth,
              brokenImgs: broken,
              themeBefore,
              themeAfter,
              tabWorked
            };
          })()`,
        },
        sessionId
      );

      // Mobile viewport check
      await cdp.send(
        "Emulation.setDeviceMetricsOverride",
        { width: 390, height: 844, deviceScaleFactor: 2, mobile: true },
        sessionId
      );
      await new Promise((r) => setTimeout(r, 250));
      const mobile = await cdp.send(
        "Runtime.evaluate",
        {
          returnByValue: true,
          expression: `(() => ({ overflow: document.documentElement.scrollWidth - window.innerWidth }))()`,
        },
        sessionId
      );

      for (const ev of cdp.events) {
        if (ev.method === "Runtime.exceptionThrown") {
          pageErrors.push(ev.params?.exceptionDetails?.text || "Runtime exception");
        }
        if (ev.method === "Log.entryAdded" && ev.params?.entry?.level === "error") {
          pageErrors.push(ev.params.entry.text);
        }
      }

      const d = desktop.result.value;
      const m = mobile.result.value;
      const themeOk = d.themeBefore !== d.themeAfter;
      const ok =
        d.overflow <= 4 &&
        m.overflow <= 4 &&
        d.brokenImgs.length === 0 &&
        themeOk &&
        d.tabWorked &&
        pageErrors.length === 0;
      if (!ok) failures++;
      console.log(
        `[${ok ? "OK" : "FAIL"}] ${path} | desktopOverflow=${d.overflow}px mobileOverflow=${m.overflow}px | theme=${d.themeBefore}->${d.themeAfter} | tab=${d.tabWorked} | brokenImgs=${d.brokenImgs.length} | jsErrors=${pageErrors.length}`
      );
      if (pageErrors.length) console.log("   JS Errors:", pageErrors);
      if (d.brokenImgs.length) console.log("   Broken imgs:", d.brokenImgs);
    }
  } finally {
    cdp.close();
    proc.kill("SIGTERM");
  }
  process.exit(failures > 0 ? 1 : 0);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
