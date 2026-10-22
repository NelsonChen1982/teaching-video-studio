# 網頁繪圖與 3D 製作

Canvas／Three.js 是第一級能力，不依賴外部 AI 圖片。選擇技術要對應概念；物件不是裝飾，運鏡要帶出關係。

## 可用骨架

`assets/three-starter/` 是原創三區場景與跟拍／拉遠示範，包含時間函式、打光、材質及字幕位置。這是技術起點，不是完成的教學影片或固定美術風格。先複製到獨立測試目錄，`npm install` 後 `npm run vendor` 將固定版本 Three.js 複製到本地 vendor/，再透過 HTTP 提供檔案。首次下載需網路；渲染不依賴 CDN。原始碼附依賴授權處理，發布建置結果時保留授權。

`renderAt(t)` 完全由秒數決定攝影機、物件、標籤、粒子與材質。不要累加 rotation += delta；不要以 Date.now、requestAnimationFrame 或物理引擎的上一幀決定成片。GLTF 使用 mixer.setTime(t)。物理效果需先烘焙或可從種子與 t 重建。Canvas 每次清空並重畫完整狀態。

依 HyperFrames three adapter，監聽 `hf-seek` 的 `event.detail.time`，指定 root data-duration。需要自訂非同步工作時，按目前官方 buildReady 契約註冊 promise；不猜 runtime 私有 API。此套件預覽手動 `window.renderAt(t)` 只是測試介面。

## 視覺品質

先確認鏡頭構圖、物件比例與輪廓，再做材質。使用有厚度、倒角或成熟模型的物件；教學圖形可以抽象，但不要冒充真實設備。主光塑形，補光保留暗部資訊，輪廓光分離背景；陰影接觸地面。色彩管理採 sRGB 輸出、合理 tone mapping，避免過曝光暈。PBR 材質需要適合照明；沒有環境貼圖時不盲用全金屬或玻璃。

材質、光線與背景配合選定風格。浮世繪可採平塗、木刻輪廓、紙張紋理與分層景深，不必強行寫實 PBR。程式紋理需固定 seed，避免每幀抖動。

鏡頭 position 與 lookAt target 可用插值或曲線，但確保穿越中點仍有主體、近遠裁切正常、標籤不被遮擋。用平滑曲線處理啟停；長距離移動檢查速度峰值。運鏡避免不必要搖晃。OrbitControls 僅供製作檢視，不能決定正式時間軸。

固定輸出尺寸、pixel ratio；先在 540p 或 720p 做效能測試，最終依規格渲染。模型與紋理事先載入並確認完成。時間歷史型後製、動態網路載入與依裝置像素比的尺寸不適合直接逐幀渲染。

## 驗證

至少檢查 t=0、動作中點、鏡頭切換前後、尾幀。以非順序 t=8→2→8 測試同一時間畫面一致；不能只順播測試。查看 browser errors、WebGL availability、空白 canvas、文字裁切與影片輸出。重點動作觀看正常速度；截圖無法證明節奏品質。遇不支援效果可先輸出該段影片再組裝，但必須實測並揭露替代方案。
