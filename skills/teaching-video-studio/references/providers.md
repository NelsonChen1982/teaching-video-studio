# 能力偵測與選用服務

建立 CAPABILITIES.md：本機檔案、shell、Node、Python、FFmpeg/ffprobe、瀏覽器/WebGL、HyperFrames、配音、對時、imagegen、影片生成、Drive。每項記錄 available/unavailable/untested 與證據；模型名稱不是能力證據。

圖片：老師指定優先，其次可用的 Codex/宿主 imagegen 或已匯出的 Grok 圖像；再按需要選授權素材或程式繪圖。Grok 圖像匯出是輸入能力，不代表有 Grok API。無工具時可輸出提示詞讓老師在別處生成，亦可繼續不依賴該素材的工作。

影片：有 Higgsfield 或其他已連接服務時，查看現有工具／模型／預設與費用，依鏡頭需求選用。只在請求生成且符合授權時呼叫。遵循服務確認機制，不預設某斜線指令可由普通語句自動啟用。保存 job id、輸入、費用及結果；逾時先查既有任務，不重送付費生成。

聲音：老師錄音 → 使用者指定服務 → 已可用宿主 TTS → 已安裝且語言適合的本機 TTS。比較短句確認發音；不得因 provider 預設而忽略語言／聲線偏好。沒有可用方案時不要宣稱能產完整有聲影片。

Drive：使用宿主連接工具與專用 skill；只讀明確資料夾／選定檔案，保留 file id、修改時間及原始連結。原生 Docs/Slides/Sheets 按工具支援匯出。下載到本次 assets 或 inputs，不依賴受登入保護的 URL 做逐幀渲染。沒有 Drive 連接就請老師下載 ZIP 放入專案。上傳成果要有使用者指定／授權；無寫入工具就交本機成果。

平台差異：有 shell 的 agent 可執行套件；只有聊天／附件的 bot 僅可規劃或產原始碼，必須連接執行環境才能渲染。以 doctor 加一個實際渲染測試證明能力。不使用任何環境的私有憑證路徑，不將 API key 寫入專案或 ZIP。
