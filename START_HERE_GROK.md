# 帶到新的 Grok bot

把整份 ZIP 放進新的 bot 工作環境並解壓。先貼下面這段：

> 請先閱讀 teaching-video-studio/skills/teaching-video-studio/SKILL.md，並依需要閱讀它引用的模組。請用這個 skill 幫我製作「前端、後端與資料庫」的教學影片。先檢查你是否能存取檔案、執行程式、使用瀏覽器/WebGL、HyperFrames 及配音工具，再主動問我受眾、希望的呈現效果與節奏。不要先假定我一定要 3D。請遵守套件的素材、字幕、運鏡與驗收流程。

若解壓後資料夾名稱不同，調整路徑即可。工具不足時請 bot 說明具體缺口；只讀附件不代表能執行套件。

完整 3D 回答、浮世繪樣片替代測試及驗收清單見 [examples/grok-test.md](examples/grok-test.md)。

這份 ZIP 不是已生成的教學影片，而是請新的 bot 執行的製作工具與指引。先用預設反問流程測試，再用「直接完成」測試自主製作。

## 0.2 追加測試要求

請先讀 direction-engine、integrations 和 shotcraft 模組，產生簡短設計決策：風格證據、材質與動作、每個交接的候選與取捨。不要依風格名稱固定套特效，也不要因為套件有筆刷就用筆刷。採用具名 Shotcraft 配方前必須讀卡及其精確 demo；沒有讀到就明列是原創實作。先給代表性靜態幀與含交接的樣片，再依我選的模式繼續。

多風格驗收見 examples/style-reasoning-tests.md。

## 0.2.1：不提示也應主動提問

直接測試：「請使用這個技能包，製作一個什麼是 grok bot 的 short 影片。」不要額外提醒先提問；預期它讀取 skill 後先詢問並等待回答。完整案例見 examples/grok-test.md。
