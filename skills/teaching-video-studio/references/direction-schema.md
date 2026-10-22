# DIRECTION.json 決策摘要

由 agent 根據已讀教材／參考填寫；不得要老師填 JSON。最少欄位見 [direction-example.json](../assets/direction-example.json)。

- version: 1
- style: intent（美術意圖）、evidence（可觀察證據，至少一項）、traits（line、shape、palette、material、composition、type）、motion（節奏、重量與幅度的具體摘要）
- engine: hyperframes 或 remotion
- transitions: id、relation、asset_mode、candidates、selected、reason、implementation、qa_times
- candidates: 至少兩項 id + tradeoff，包含 cut / none / match-continuity 之一作低效果比較
- qa_times: 正規化 progress，至少包含 0、0.25、0.5、0.75、1
- review: styleframe 與 transition_sample 各為 pending / passed / failed，evidence 為實際檢查檔案或時間點陣列

用 `python3 scripts/validate_direction.py DIRECTION.json` 驗證結構。`--require-reviewed` 額外要求兩個人工／agent 視覺檢查 passed 及證據。驗證器只能檢查完整性與已回報狀態，不能判斷藝術品質，也不自行將 pending 改為 passed。
