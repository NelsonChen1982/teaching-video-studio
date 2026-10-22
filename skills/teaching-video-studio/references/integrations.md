# 七個能力來源如何組合

使用者列出六個名稱；本版本將原有 HyperFrames 視為第七個。這是方法與選用接法整合，不是把七份 skill 原文或 runtime 全部包進來。內附模組可獨立閱讀；下列上游只有在需要其精確程式／資產時才取得，並遵守授權。

| 來源 | 採用的能力 | 適用邊界 |
|---|---|---|
| Video Shotcraft | 視覺規格 → 教學功能到鏡頭映射 → 精確配方／demo → 分鏡 → 逐幀 QA | 主要導演方法。產品宣傳的 UI 截圖、品牌節奏、宣傳模板不套到所有教材 |
| Motion Design Skill（LottieFiles） | 情緒、主動作、材質重量、緩動與編排 | UI 毫秒時長、強制三層動態與固定 archetype 不作教學硬規則 |
| GSAP Core／Timeline | 可 seek timeline、標籤、同步、fromTo 與緩動 | 在 HyperFrames 依其 timeline 契約；不要在 Remotion 內自由播放另一個時鐘 |
| Pixel2Motion | 語意部件、幾何品質、終幀契約、交接風險採樣 | 原本是 Logo 工具，只在 Logo／可靠向量標誌需要時用。不能拿來替代插畫生成 |
| Story to Handdraw（gnipbao/story-to-handdrawn-video） | 參考圖分析、角色／素材一致性、風格與素材快取分離、完整母圖檢查 | 不繼承固定彩鉛風、固定比例、字幕烘進圖或靜音交付；不能宣稱它原生有配音 |
| Remotion（官方文件／選用 skills 連結） | 以 frame/fps 決定畫面、字幕／音訊／3D、逐幀渲染 | 選用執行引擎，直接使用 Shotcraft TSX 時可選；不是自動美術提升器 |
| HyperFrames 官方 skills | HTML/Canvas/Three.js 時間軸、聲音與輸出 | 保持預設渲染引擎，具體契約依已安裝版本 |

## 解析與載入

先查宿主已安裝 skills；存在時讀對應入口與本次需要的 reference。沒有時讀本套件模組；若需要特定 Shotcraft 卡片或外部實作，再從 SOURCES / upstream-sources.json 的確認來源取得。不要臆造卡名、工具指令或套件 API。

上游有自己的創作模式，整合時保留老師已選的 collaborative/autonomous 與輸出需求，不重問、不改成品牌宣傳、不默認模板。使用者已要求 MP4 就應完成渲染；只要求樣片則停在樣片。

只有真正使用了原始碼才標為 copied/adapted-code 並保留授權；本版本原創模組標為 methodology-adapter。來源閱讀不等於測試過所有上游 runtime。不得替老師自動發布、提交回饋、上傳範例或推廣原作者帳號。

授權邊界見 [第三方通知](../THIRD_PARTY_NOTICES.md)。Remotion skills 未找到明確授權，不內附或改寫分發原文；官方 runtime 文件與 API 用法由本模組獨立說明。GSAP runtime 不適用其 skills 的 MIT。
