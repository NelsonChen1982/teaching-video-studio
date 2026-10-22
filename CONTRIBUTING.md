# 開發與貢獻

修改入口在 `skills/teaching-video-studio/SKILL.md`，詳細方法在 `references/`。新增規則應解決具體失敗，不把單一風格變成全域預設。

## 驗證

```sh
python3 -m unittest discover -s tests -v
node --test tests/*.test.mjs
```

可選瀏覽器測試：安裝 Playwright 與其 Chromium 後執行 `node tests/browser-smoke.mjs`。亦可用 `PLAYWRIGHT_MODULE`、`CHROME_PATH` 指定既有環境；`SMOKE_OUTPUT` 指定截圖位置。

Three.js starter：在 `skills/teaching-video-studio/assets/three-starter` 執行 `npm ci`、`npm run vendor`，以本機 HTTP server 預覽。它是 18 秒無聲技術樣例。

修改對話規則時，用新的獨立 agent 測試；不要提供標準答案。行為案例放在 `examples/`，不要塞進 runtime 指引。紀錄是否真實渲染、是否使用外部服務及測試限制。

## 提交

說明問題、變更與驗證結果。第三方程式／素材須記錄來源、版本、授權與修改，保留適用通知。未明確授權的內容不得收錄。不要提交憑證、教師教材、學生資料、私有素材或 node_modules/vendor。
