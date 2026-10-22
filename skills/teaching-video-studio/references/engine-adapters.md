# 選擇一個時間來源

## HyperFrames（預設）

沿用 hyperframes.md。GSAP 採一個 paused master，語意標籤如 request/send/resolve，鏡頭、遮罩、字幕共用時間。不要靠 onComplete 改變永久狀態；亂序 seek 必須重建當下狀態。Three.js 用官方 hf-seek；Canvas 亦可由同一 renderAt(t) 呼叫。不要動畫框架管理的 clip 可見性。

## Remotion（選用）

若已有 Remotion 專案或需要直接保留 Shotcraft TSX，讀實際安裝的 remotion-best-practices、remotion-markup、remotion-render 與需要的 captions/3d references。依版本確認 API。`useCurrentFrame()` 與 `useVideoConfig().fps` 是時間來源；t=frame/fps，場景內計時要注意 Sequence 的局部 frame。

不要直接把自由播放 GSAP、CSS animation 或 requestAnimationFrame 接入 Remotion；移植為由 frame 算出的純函式，或採已驗證且鎖定 frame 的 adapter。影片長度、素材載入、字體、音訊依官方 API 管理。內附 mask 的純函式可共用；在 Canvas React 元件需使用該 Remotion 版本的載入／渲染完成機制，不能假設 effect 已繪完。

## 素材、程式碼與授權

Remotion skills 的授權與 Remotion renderer 的授權是兩回事；使用 renderer 前查看當前官方 LICENSE，不寫死免費團隊人數。套件 MIT 只涵蓋本套件原創檔案。

不在同一正式影片中無理由混合兩個主 renderer。必須混合時，先把外部片段渲成固定 fps／尺寸的影片，再由主 renderer 組裝，記錄音訊與起始時間。預覽、亂序 seek、正式輸出三者要各驗證。
