# 教學影片工作室 · Teaching Video Studio

讓 AI 從教材與對話出發，製作有旁白、字幕、動畫與運鏡的教學短片。**風格開放，預設先問需求、確認方向與樣片，再做完整影片。**

這是可安裝的 agent skill，搭配輔助工具；不是一鍵影片網站。版本：**0.2.3 preview**。

## 快速開始

1. 從 GitHub 的 **Code → Download ZIP** 下載並解壓，將資料夾放入 AI 可讀取的工作區。
2. 告訴 AI：

   > 請閱讀 skills/teaching-video-studio/SKILL.md，使用這個技能幫我做一支介紹 Grok bot 的 short。

3. 回答受眾、呈現方式、風格與節奏。可提供教材、照片、影片、參考截圖，或已連接的 Google Drive 資料夾。
4. 確認風格方向，再看代表性樣片；滿意後才製作整片。

**只說「幫我做」不會跳過訪談。** 若要自主完成，明確說：「不用問我，缺少的由你決定，直接完成。」若只要預覽，說：「先給樣片，不要做整片。」

## 安裝到常用 agent

先下載並進入本專案資料夾，選一種安裝方式：

```sh
# Codex：個人 skills
python3 install.py --target ~/.codex/skills

# Claude Code：指定專案的 skills
python3 install.py --target /你的專案/.claude/skills

# 其他採用 .agents/skills 的環境
python3 install.py --target /你的專案/.agents/skills
```

安裝器不覆蓋已有版本；更新時先備份並移走舊的 `teaching-video-studio` 資料夾。也可直接將 `skills/teaching-video-studio` 整個資料夾放入宿主支援的 skills 位置。

Grok bot 或其他未確認安裝規格的宿主，使用上方「讀取 SKILL.md」方式。只上傳 ZIP 不會讓聊天機器人自動取得執行程式的能力。

## 製作流程與成果

**需求訪談 → 風格方向確認 → 腳本／分鏡 → 旁白與字幕對時 → 樣片確認 → 完整合成與檢查**

AI 依視覺特徵、材質、教學目的與鏡頭關係選擇動畫及轉場；不將風格名稱固定套成特效。可採實拍、Canvas、Three.js 3D，或選用 imagegen／Higgsfield。預設以 HyperFrames 合成，Remotion 為選用引擎。

完成時交付 **MP4、SRT、可修改專案及檢查紀錄**。若缺少配音或渲染工具，必須說明缺口，不把 HTML、截圖或無聲預覽當成有聲成片。

## 執行條件

完整製作需要能讀寫檔案、執行程式及操作瀏覽器的 AI 環境，並具備 Python 3.10+、Node.js、FFmpeg、HyperFrames 與可用配音來源。可先請 AI 執行環境檢查：

```sh
python3 skills/teaching-video-studio/scripts/studio.py doctor
```

外部生圖／影片服務不是必要條件；本套件不含服務額度。聊天網頁版、免費帳號或特定模型能否完成，取決於實際工具權限，不能只看產品名稱。

## 驗證與授權

目前已驗證輔助工具、動畫可重現性及獨立代理的訪談流程；**尚未完成 Grok bot 有聲影片的端到端實測**。內附 3D 與遮罩是技術起點，不是商業品質成片範本。

本專案原創內容採 [MIT](LICENSE)。外部引擎與素材另依其條款；Remotion skills 未找到明確授權，因此不隨包分發。詳見 [來源與授權](SOURCES.md)。

[完整測試紀錄](VALIDATION.md) · [Grok 測試方式](START_HERE_GROK.md) · [開發與貢獻](CONTRIBUTING.md)
