# 專案與可恢復製作

腳本路徑以本 skill 所在位置解析，不使用作者機器的絕對路徑。

先在新建的空 render 子目錄依目前官方方式初始化 HyperFrames，或保留既有 HyperFrames 專案。輔助工具不建立 hyperframes.json，也不冒充官方 init。

```sh
python3 /path/to/skill/scripts/studio.py init /path/to/lesson
python3 /path/to/skill/scripts/studio.py inventory /path/to/lesson/inputs --out /path/to/lesson/ASSETS.json
```

結構：inputs/ 原教材、assets/ 本次採用的素材、audio/、captions/、boards/、render/ HyperFrames 專案、exports/、PROJECT.json。BRIEF.md、SCRIPT.md、STORYBOARD.md、QA.md 由 agent 按本次實際內容建立，不用空白範本假裝完成。

PROJECT.json 保存 stage、stages 狀態與 requirements（是否需要旁白字幕）。每階段完成才更新；status 值可用 pending/running/blocked/complete。另記實際產物路徑、工具版本與輸入來源。更動腳本會使配音／字幕／畫面／合成待更新，更動美術只使受影響場景及合成待更新。不要重跑未變更的付費素材。

ASSETS.json 的自動 inventory 只列檔名、相對路徑、位元組數、SHA-256 與副檔名；agent 再補 sources、用途、授權、是否 AI 示意。不自動掃描工作區外的 symlink，也不讀 .env、金鑰與私人設定。資料夾大量檔案時先限定範圍。

在 exports/ 保留 lesson.mp4、subtitles.srt（需要時）、製作專案 ZIP 及 QA 摘要。不要把老師教材、學生資料、付費素材或 API key 包進公開 skill repository；交付專案是否含原素材需依老師用途決定。
