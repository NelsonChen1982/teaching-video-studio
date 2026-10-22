# HyperFrames 執行接法

HyperFrames 為外部執行依賴，不隨本套件附帶，也不在安裝 skill 時偷偷安裝。需要 Node、支援的瀏覽器與渲染環境；首次安裝使用已授權的正常套件來源。

有官方 HyperFrames skills 時，先讀 hyperframes，再按需讀 core、animation、keyframes、audio、cli、registry。保留本 skill 已形成的 brief、風格與審核模式，避免重複訪談。沒有 skills 時從官方 repo/docs 取得適用版本的契約；CLI flags 以 `--help` 和實際版本為準。不要從舊筆記猜命令。

官方來源：https://github.com/heygen-com/hyperframes

1. 檢查 Node、HyperFrames 版本及當前 init/doctor/check/render 用法，記錄版本。新專案選定版本後固定依賴並保留 lockfile，不在成片途中自動升級。
2. 在空的 render/ 或新的子目錄完成官方 init，保持 inputs 與紀錄不被覆蓋。
3. 把本次素材與本地字型放在渲染可存取範圍，使用穩定相對路徑。
4. root 明確給 composition id、寬高、時長。GSAP 每個 composition 用一條 paused timeline，key 與 composition id 相同。純 Three.js 使用 three adapter 與 hf-seek；不必虛構 GSAP timeline。
5. 不直接動畫框架管理的 clip visibility；動畫放子元素。音訊有唯一 id，時間範圍與全片一致，避免重複套兩層媒體 timing。
6. 先 lint／check，確認真的採樣；零採樣不能算版面通過。檢查關鍵幀與樣片，再渲染正式影片。
7. ffprobe 驗證串流、尺寸、時長及所需音訊；播放檢查聲畫。保存具體檢查結果。

HyperFrames 整合不能由「瀏覽器能開」推論成功。若只能產 HTML，標記 preview-only 並報告缺少項目；不要稱為 MP4 成片。
