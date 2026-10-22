# Video Shotcraft 導演方法接法

先讀 direction-engine.md，完成視覺特徵與動態性格，再把每個教學功能映射到鏡頭。用一句「學生應看見什麼變化」表達功能，而非只說要華麗／電影感。

鏡頭規格包含：教學用途、視覺主角、起始構圖、主動作、結束構圖、鏡頭距離與路徑、停留、交接錨點、素材、音效、參考卡／demo、驗收時間點。一鏡有一個主要動作，其餘動作輔助；不是必須每鏡換全新效果。

需要上游精確配方時：
1. 查 `gallery/api/library.json` 的 card name、style key、source。
2. 讀 `references/shots/...` 對應卡片的完整內容，尤其已知坑與參考實作。
3. 讀該 demo 的精確 TSX 及必要共用依賴；如未能取得，不能聲稱已復刻卡片。
4. 記錄 upstream revision/hash、所用參數、修改處與理由。字體、色彩、素材應依本次教師需求重做；保留有用的動作結構。
5. 看動態參考或關鍵幀，驗證實際素材下的效果。不以檔名代替效果證據。

這次查核的兩個例子特別說明名稱陷阱：
- `brand-ink-open` 是品牌字標壓印、準星描線與副標，不是墨水潑灑轉場。來源 `references/shots/opening/brand-ink-open.md`，demo `demos/typography/brand-ink-open/BrandInkOpen.tsx`。
- `wipe-transitions` 是 3D 百葉翻片的幾何擦除，不是天然筆刷。來源 `references/shots/transition/wipe-transitions.md`，demo `demos/transition/wipe-transitions/BlindsSlice.tsx`。

兩者只供辨識與方法研究，本版不附其程式或音樂。要用它們才讀對應 demo，不需為一般教學載入所有鏡頭卡。

保留 Shotcraft 的「先 styleframe、再映射、再分鏡、用實作證據驗收」。不照搬固定 3 秒、全片只能用某招一次、品牌 logo 停留秒數等產品案例規則；教學時長由理解難度及聲音決定。旁白主導的片不強制每一切點卡音樂拍。

3D 美術門檻：近拍物件需有可辨識結構與適當細節、材質差異、可讀標籤、接地陰影，亮暗不壓掉形體。必須有全貌／中景／近景至少所需的代表幀作比較。僅方塊堆疊、全片同一塑膠材質與空洞環境只能標 blockout，不能交為精緻成片。
