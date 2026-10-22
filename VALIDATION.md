# 0.2.3 驗證紀錄

日期：2026-10-22。此紀錄區分套件工具、場景骨架與整片工作流程。

## 本版新增驗證

- Python unittest：12 項通過，包含決策欄位、候選選擇、缺少審查證據與不自動宣稱審查通過。
- Node test：9 項通過，包含三種遮罩的端點、單調覆蓋、固定 seed、局部羽化與不透明合成。
- 實際 Chrome 測試三種遮罩各五個進度，共 15 張截圖；0.5→0.1→0.5 亂序跳轉逐像素一致，無 page errors。已人工檢視三種中間畫面。
- 遮罩只是可選技術元件，以上測試不代表筆刷、潑墨或任意風格的商業美術品質通過。
- 七個來源為已閱讀文件後整理的方法接法，並未安裝或執行七套上游 runtime。來源與文件雜湊見 upstream-sources.json。
- 多風格案例是待執行的 agent 行為驗收規格，不宣稱已完成各風格成片測試。

## 0.1 延續的驗證

- 官方 skill-creator quick_validate：通過。
- Python unittest：7 項通過，涵蓋初始化不覆蓋、素材排除隱藏檔與 symlink、字幕重疊／越界／無效時間、估算時間需明示、安裝防覆蓋、輸出防覆蓋。
- Node test：4 項通過，涵蓋亂序 seek 狀態一致、逐幀數值有效與範圍、鏡頭節點連續、無效時間拒絕。
- Three.js 0.181.2 安裝及本地 vendor 準備成功，lockfile 隨 starter 提供。
- 實際 Chrome headless／WebGL 渲染 0、8、12、18 秒截圖，無 page errors。
- 瀏覽器內 8→2→8 秒跳轉，兩張第 8 秒截圖逐像素一致。
- 人工檢視第 8 秒截圖：標題／標示可見、主體及光線正常。這是技術樣例，不是完整商業美術認證。

## 尚未驗證／不宣稱已支援

- Grok bot、ChatGPT Work、Claude Cowork／Code 等各宿主實際執行。
- 在 HyperFrames 中完成此 starter 的 lint／check／正式 MP4 渲染。
- 中文 TTS、實際語音對時、完整影片聽驗及最終合成。
- Google Drive 下載／回存、imagegen、Higgsfield 的端到端整合。
- 自動生成的各種風格之成片品質，以及 Remotion 正式渲染。

本版本的配音與服務整合是 agent 工作流程接法，不是內建通用 API client。doctor 不會連接服務或下載依賴。Three starter 只有 18 秒無聲可 seek 場景；使用者正式測試仍須依分鏡創作，不得直接把技術樣例當作 60 秒教學影片交付。

後續以 examples/grok-test.md 執行並保存實際 QA 紀錄。相容性及品質結論以真實產物為準。

## 0.2.1 修正範圍

本版僅修改訪談指令與行為驗收案例；skill 格式驗證通過。下列既有工具測試紀錄沿用 0.2。新的訪談行為尚未在 Grok bot 重測，文字指令無法保證宿主遵循。

## 0.2.2 對話驗證

見 evaluations/intake-2026-10-22.md：獨立代理先提問、再提方向並等待；第三輪為引導式停止點檢查。未實際產出樣片，未在 Grok 測試。工具程式未變更。

## 0.2.3 公開發布檢查

- 12 項 Python、9 項 Node、skill 格式檢查通過。
- 修正 lockfile 後 npm ci 與 vendor 成功，Three.js 0.181.2 的 LICENSE 和 vendor 通知逐位元一致。
- 文件本地連結、個人路徑及常見憑證格式掃描通過；此掃描非通用機密辨識保證。
- 第三方授權核對見 license-audit.json 與 THIRD_PARTY_NOTICES；未確認的外部內容不內附，沒有宣稱所有 runtime 都是 MIT。
