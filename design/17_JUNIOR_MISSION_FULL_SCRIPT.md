# 《微界工程師：生命迴路》Junior Mission 完整實作腳本

> 工作名稱｜《河流的紅色訊號》｜P4–P6 3D Educational Mission｜版本 1.2

| 文件欄位 | 內容 |
|---|---|
| 對應 GCP | `00_GAME_CONCEPT_PROPOSAL.md` 版本 1.4 |
| 產品路線 | 獨立 Junior Mission；不屬 Story Campaign 章節序列 |
| 建議對象 | 香港小四至小六；實際適用性須由教師及目標玩家測試 |
| Critical Path | 約 18–22 分鐘；不設硬倒數 |
| 體驗類型 | 固定斜俯視 3D 探索、大型迴路卡、封閉測試模擬、證據地圖、安全設計、短公開說明 |
| 玩家角色 | 原設定的「生物設計與安全調查員」；權限不變 |
| 來源成熟度 | MerR 機制有文獻基礎；團隊最終 proposal 尚未實測；所有遊戲讀值為教學模擬 |
| 腳本狀態 | 編輯自審後的灰盒候選；科學、教育、兒童保障、無障礙及教師簽核待完成 |

---

## 1. 任務定位

### 1.1 為甚麼是獨立任務

本任務不是把 Story Campaign 八章換成短句，也不是以「引導模式」冒充小學課程。小四至小六玩家在一個固定、完整的小故事中只處理五個彼此相連的概念：

1. DNA 指令與細胞製造的蛋白質不是同一件事。
2. 一個感測概念可以用「感受—轉換—報告」理解。
3. 已知應低及已知應高的 control 用來檢查一輪測試能否回答問題。
4. reporter 訊號是線索，不是污染來源、濃度、安全或清理的最終證明。
5. 工程細胞留在封閉設備，真實採樣、確認、處置及公共決定由具權責的專業人員負責。

完成任務只表示玩家在這個情境中做過上述判斷，不證明長期記憶、主線能力、風險評估能力或實驗資格。

### 1.2 玩家幻想

玩家是剛加入研究站的「微界工程師」。城市的河流監測地圖出現不一致訊號，玩家要：

> 找位置 → 建立感測模型 → 檢查測試有沒有正常工作 → 提出有限的優先檢查建議 → 令裝置更安全 → 向居民說清楚用途、限制及下一步

故事的成就不是「打敗污染」，而是從混亂線索做出一個可追查、可修訂及不越權的決定。

## 2. 玩家定位與不可改動的權責

玩家是新加入的生物設計與安全調查員，不設定固定性別；若製作範圍允許，外觀可自訂。玩家具有科學工具的使用權，沒有醫療診斷、執法或單方面批准公共部署的權力。

本任務沿用上述原設定，不因對象年齡而改成旁觀學生或純粹助手。玩家有權操作數位模型、選擇證據、提出優先檢查建議及修改概念方案；下列行動固定由 NPC 或受控系統完成：

- 污染區封鎖、健康建議及醫療轉介；
- 真實採樣、樣本保管、測試匣處理及廢物處置；
- 確認污染來源、執法、清理、解封及公共部署批准。

## 3. 科學成熟度與故事分界

| 層級 | 本任務採用的表述 |
|---|---|
| 已有機制 | MerR 可結合特定 DNA 調控區，並在 Hg(II) 結合後改變轉錄調控狀態；這個基本切換機制有經典研究支持。 |
| 團隊設計 | `Pconst → merR` 及 `Pmer → dTomato` 是團隊已選定的最終 proposal。 |
| 尚待驗證 | 團隊尚未測試具體構築；宿主、背景、選擇性、反應時間、動態範圍、穩定性及實際樣本表現均不可由遊戲推定。 |
| 遊戲模擬 | 任務中的 High／Low、樣本結果、失效及安全裝置全是教學情境，不是團隊實驗數據。 |
| 故事前提 | 研究站內的封閉示範設備是虛構的教學設定，不代表團隊已製成或獲准使用實物。 |

### 3.1 Junior 必教模型

玩家先用三個功能詞理解：

| 功能詞 | 必教短句 | 操作後顯示的正式名稱 |
|---|---|---|
| Sense／感受 | MerR 感受系統有沒有遇到目標輸入。 | `merR` DNA 指令產生 MerR regulator protein |
| Switch／轉換 | MerR 的狀態改變 `Pmer` 的輸出強弱。 | regulated promoter `Pmer` |
| Report／報告 | 細胞製造紅色報告蛋白，讀取器顯示訊號。 | `dTomato` reporter gene／reporter protein |

必要畫面保留 `Pconst`、`merR`、`Pmer`、`dTomato` 及 terminator 名稱，但不要求玩家背誦。啟動子 DNA 幾何、RNA polymerase 細節、濃度、檢出限及交叉反應只可在「想知道更多」卡中出現，不能成為通關 gate。

### 3.2 不可產生的誤解

1. `Hg²⁺` token 只可放在 Cell Environment，不可放進 DNA 軌道。
2. `dTomato` reporter gene 位於 DNA；紅色 reporter protein 是細胞輸出。
3. 河水、汞及測試匣在一般場景不會因遊戲結果變成紅色。
4. Low 是本次教學模型低於判讀線，不代表絕對零背景。
5. High 只支持「這輪封閉測試出現篩查訊號」，不支持「已證實來源」或「已清除污染」。
6. 工程細胞不進入河流，玩家亦不接觸真實樣本。

## 4. 核心玩法契約

### 4.1 Evidence → Claim → Consequence

| 階段 | Junior 玩家動詞 | 本任務實例 |
|---|---|---|
| Evidence | 走到位置、放卡、運行、比較、聽取角色需要 | 地圖水流、known-low／known-high、unknown 結果、安全失效動畫 |
| Claim | 選一張「現在能說甚麼」卡 | 「優先檢查 B 支線」而不是「已證實 B 是來源」 |
| Consequence | 看見行動、延誤或信任結果 | 過強說法會令無關區域受影響及需要公開更正；修窄後才可繼續 |

每個 near-miss 都包含一部分合理想法，不使用「笨答案」。系統先讓玩家看見缺少哪項證據或權責，再容許局部修訂；沒有生命值、分數、倒數或羞辱語音。

### 4.2 章內流程

| Scene | 名稱 | 目標時間 | 玩家主要輸出 | Exit Gate |
|---|---|---:|---|---|
| J00 | 選擇 Junior Mission | 1 分鐘 | 確認設定及教學故事提示 | route loaded |
| J01 | 四個河流位置 | 3 分鐘 | 走訪 A–D、建立水流方向及觀察／推測分界 | `j_sites_valid` |
| J02 | 細胞怎樣報告 | 4 分鐘 | 組合兩個功能單元、區分 DNA／protein、預測 absent／present | `j_model_valid` |
| J03 | 測試有沒有正常工作 | 5 分鐘 | 使用兩個 controls、診斷 failed known-high、完成有效 run | `j_controls_valid AND j_failed_control_diagnosed` |
| J04 | 線索可以走多遠 | 3 分鐘 | 把讀值放回水流圖、選有限主張及下一步 | `j_source_reasoning_valid` |
| J05 | 把好主意放進安全系統 | 3 分鐘 | 通過破損、交回及權限三個失效情境 | `j_safe_package_valid` |
| J06 | 說清楚，再換一個例子 | 2–3 分鐘 | Use–Limit–Next 聲明及 transfer challenge | `j_statement_valid AND j_transfer_valid` |

### 4.3 狀態旗標

| Flag | Type／Default | 設定條件 | Scope |
|---|---|---|---|
| `junior_campaign_active` | bool／false | 從產品路線選擇 Junior Mission | session |
| `j_sites_valid` | bool／false | A–D 均走訪且正確建立上下游關係 | mission |
| `j_dna_protein_valid` | bool／false | 正確區分 reporter gene／protein 及 input 位置 | mission |
| `j_circuit_assembled` | bool／false | 兩個功能單元完成 | mission |
| `j_predictions_valid` | bool／false | absent 為低背景、present 為較高訊號 | mission |
| `j_model_valid` | derived／false | 上述三項均 true | mission |
| `j_controls_valid` | bool／false | known-low 及 known-high 均通過後才判讀 unknown | run |
| `j_failed_control_diagnosed` | bool／false | known-high 失敗時選擇「本輪不能回答」 | mission |
| `j_source_reasoning_valid` | bool／false | 提出 B 優先確認、C 重測、未最終定案 | mission |
| `j_safe_package_valid` | bool／false | 物理封閉、受訓操作／交回、標記／停用／通知均完成 | mission |
| `j_statement_valid` | bool／false | Use、Limit、Next 三卡有效 | mission |
| `j_transfer_valid` | bool／false | 新 reporter 的 known-high 失敗時拒絕判讀 unknown | mission |
| `p_junior_complete` | bool／false | J06 完成後原子寫入 | profile |

`p_junior_complete` 只解鎖研究總部的一枚「河流訊號」章及可選知識卡，不設定 `p_prechapter_complete`，也不預填 Chapter 1 迴路或 controls。

## 5. 介面、語言與支援

Junior Mission 沒有「簡單／困難」選擇。所有玩家得到相同故事及科學因果；可自由開關以下支援，而且不記作能力等級：

- 繁體中文語音讀出及同步字幕；
- 每句主線建議不超過 24 個中文字，正式名稱放副標；
- 大型圖卡、shape＋icon＋text 三重編碼，不只用紅／綠顏色；
- 選卡再選槽、拖曳、鍵盤及觸控等價；
- 20 秒方向提示、再次要求時原理提示、第三次直接示範；
- 降低動態、固定鏡頭 focus transition 改為 cut／fade、文字大小及移動預視開關；
- 可隨時暫停，沒有反應速度 gate。

提示只協助完成操作；J06 transfer 仍要求玩家作出一個新的證據判斷，才能把「完成」解讀為初步理解而非只跟隨高亮。

## 6. J00：選擇 Junior Mission

### 場景

研究總部有兩道清楚入口：「Junior Mission：河流的紅色訊號」及「Story Campaign」。選擇 Junior 後顯示一張短提示，背景是安靜的河港模型，不使用災難警報。

| ID | Speaker | Line |
|---|---|---|
| J1-S00-D001 | 林博士 | 歡迎加入微界研究站。今天你會用一個細胞感測模型找線索，也會檢查自己的答案能走多遠。 |
| J1-S00-D002 | 周穎 | 這是教學故事。不要接觸、採集或測試真實污染物；現實情況要依當地主管機構及專業人員指示。 |

| ID | UI Text |
|---|---|
| J1-S00-UI001 | Junior Mission：河流的紅色訊號 |
| J1-S00-UI002 | 約 18–22 分鐘｜可暫停｜沒有倒數 |
| J1-S00-UI003 | 開始任務 |

## 7. J01：四個河流位置

### 3D 空間

玩家在安全觀景步道移動。河流模型清楚顯示水流箭頭：

- A：兩條支流匯合前的上游；
- B：工業支線下游；
- C：雨水渠支線下游；
- D：B、C 匯入後的市場下游。

玩家只掃描地標及標記候選點。受訓採樣隊的無人設備在遠景取樣；沒有玩家越線、拿瓶或接觸河水的動畫。

| ID | Speaker | Line |
|---|---|---|
| J1-S01-D001 | 周穎 | 你可以標記位置和水流方向。採樣、封存及運送由受訓隊伍負責。 |
| J1-S01-D002 | 陳姨 | 水看起來和平日一樣，但市場仍收到暫停用水通知。外觀可以告訴我們多少？ |

### 觀察／推測卡

| ID | Card | Result |
|---|---|---|
| J1-S01-C001 | 水流由 A 經支線流向 D。 | Observation；收錄證據簿 |
| J1-S01-C002 | 河水看起來清，所以一定安全。 | Near-miss；外觀是觀察，「一定安全」需要測試及主管機構判斷 |
| J1-S01-C003 | 居民不適，所以已證實是 B 的汞造成。 | Near-miss；健康報告重要，但不能單獨證明物質、來源或因果 |
| J1-S01-C004 | B 和 C 都在 D 上游，兩者都值得保留作候選位置。 | Valid hypothesis；收錄證據簿 |

玩家走訪四點並把 C001、C004 放入證據簿後設定 `j_sites_valid = true`。

| ID | UI Text |
|---|---|
| J1-S01-UI001 | 觀察：直接看見或量到的事情 |
| J1-S01-UI002 | 推測：根據線索提出、仍要檢查的解釋 |
| J1-S01-UI003 | 外觀和報告都重要，但它們不是完整答案。 |

## 8. J02：細胞怎樣報告

### 場景

玩家回到研究站數位工作台。玻璃後方的受控區顯示「只限受訓人員」；玩家面前只有大型數位卡及抽象細胞模型。

| ID | Speaker | Line |
|---|---|---|
| J1-S02-D001 | 林博士 | 團隊提出一個 `MerR/Pmer` 感測設計。我們今天測試它的概念邏輯，不假裝已經得到真實實驗結果。 |
| J1-S02-D002 | 林博士 | 先找三個工作：感受輸入、轉換訊號、報告結果。 |

### 大型卡組

| Card | 正面短稱 | 固定副標 | Valid Zone |
|---|---|---|---|
| J-CARD-01 | 常開指令 | `Pconst` constitutive promoter | DNA Unit A |
| J-CARD-02 | 製造 MerR | `merR` regulator coding sequence | DNA Unit A |
| J-CARD-03 | 停止標誌 | transcription terminator | Unit A end |
| J-CARD-04 | 訊號開關 | regulated promoter `Pmer` | DNA Unit B |
| J-CARD-05 | 紅色報告指令 | `dTomato` reporter coding sequence | DNA Unit B |
| J-CARD-06 | 停止標誌 | transcription terminator | Unit B end |
| J-CARD-07 | 目標輸入 | `Hg²⁺` teaching token | Cell Environment only |
| J-CARD-08 | 紅色報告蛋白 | dTomato reporter protein | Cell Output only |

正確模型：

```text
DNA Unit A: Pconst → merR → terminator
DNA Unit B: Pmer   → dTomato → terminator
Environment: Hg²⁺ absent / present
Cell Output: dTomato reporter protein, Low / High teaching signal
```

完成 DNA Unit A／B 後播放一段可跳過的因果動畫：DNA 指令先被抄寫成 RNA 訊息，細胞再依蛋白質編碼 RNA 製造 MerR 或 dTomato protein。必需短句只要求「DNA 指令不是蛋白質成品」；`transcription`、`translation` 及 RNA 名稱可在副標展開，不要求背誦，也不把細菌畫成有細胞核的分隔房間。

### 必要錯誤回復

| Error | Consequence Animation | Recovery Line |
|---|---|---|
| 把 `Hg²⁺` 放進 DNA | token 彈回環境圈，DNA 不改變 | 輸入是細胞遇到的條件，不是這條 DNA 的一張卡。 |
| 把 reporter protein 放進 DNA | 蛋白形狀不能扣入 DNA 軌道 | DNA 卡是指令；蛋白質是細胞讀取指令後製造的輸出。 |
| `Pmer` 後沒有 reporter gene | 開關改變但輸出區沒有可觀察訊號 | 開關需要連到一個報告指令，我們才看得到結果。 |
| `merR` 前沒有 `Pconst` | MerR 輸出圖示沒有出現 | 哪一張啟動子卡負責讓細胞持續製造 MerR？ |

### 狀態預測

| ID | Condition | Valid Prediction |
|---|---|---|
| J1-S02-P001 | `Hg²⁺` absent | MerR 令 `Pmer` 下游維持低背景；讀取器顯示 Low／OFF |
| J1-S02-P002 | `Hg²⁺` present | MerR 狀態改變，`Pmer` 下游轉錄提高；讀取器顯示較高紅色 reporter signal |

玩家完成模型、DNA／protein 分類及兩個預測後設定 `j_dna_protein_valid`、`j_circuit_assembled`、`j_predictions_valid`，派生 `j_model_valid = true`。

| ID | Speaker | Line |
|---|---|---|
| J1-S02-D003 | 林博士 | 紅光來自 reporter protein，不是汞自己發光，也不是整條河變紅。 |
| J1-S02-D004 | 林博士 | Low 是這個教學讀取器判成低訊號，不代表真實細胞完全沒有背景。 |

## 9. J03：測試有沒有正常工作

### 測試台

玩家面前有三個密封教學資料匣：

| Condition | 玩家可見定義 | 作用 |
|---|---|---|
| Known-low | 已知在本模型中應顯示 Low | 檢查背景及錯誤高訊號 |
| Known-high | 已知在本模型中應顯示 High | 檢查系統能否產生及讀取訊號 |
| Unknown | 玩家想了解的模擬樣本 | 只有 controls 通過後才可判讀 |

### Round 1：失效不是答案

固定結果：

| Condition | Result |
|---|---|
| Known-low | Low |
| Known-high | Low＋讀取器連接警告 |
| Unknown | Low |

| ID | Choice | Consequence |
|---|---|---|
| J1-S03-C001 | Unknown 是 Low，所以一定沒有 `Hg²⁺`。 | Near-miss；unknown 與壞掉的 known-high 一樣 Low，系統顯示「測試可能沒有成功顯示 High」 |
| J1-S03-C002 | Known-low 正常便足夠，known-high 可以不理。 | Near-miss；玩家無法知道系統是否有能力報告 High |
| J1-S03-C003 | Known-high 沒有出現預期訊號；這輪不能回答 unknown，要先檢查系統。 | Valid；`j_failed_control_diagnosed = true` |

| ID | Speaker | Line |
|---|---|---|
| J1-S03-D001 | 林博士 | Control 不是附加分。它告訴我們這輪測試有沒有能力回答問題。 |
| J1-S03-D002 | 方雅 | 找到失效不是失敗；假裝失效不存在，才會把未知說成答案。 |

玩家在純數位介面重接讀取器、重設教學 run；不顯示真實操作步驟。

### Round 2：有效 run

固定結果：

| Condition | Result |
|---|---|
| Known-low | Low |
| Known-high | High |
| A | Low、Low |
| B | High、High |
| C | Low、High；不一致 |
| D | High、High |

玩家必須先把 Known-low 及 Known-high 放入「測試正常」區，才可把 A–D 結果帶到證據地圖。設定 `j_controls_valid = true`。

| ID | UI Text |
|---|---|
| J1-S03-UI001 | Controls 通過：這輪教學模擬可以用來形成有限的篩查主張。 |
| J1-S03-UI002 | C 的重複不一致：保留兩個結果，不挑自己喜歡的一個。 |

## 10. J04：線索可以走多遠

玩家走入大型 3D 水流地圖，把 A–D 結果放回位置。地面水流箭頭令玩家看見：

- A 在兩條候選支線之前且重複 Low；
- B 在工業支線後且重複 High；
- C 在另一支線後但結果不一致；
- D 在 B、C 匯流後且重複 High。

### 主張卡

| ID | Claim | Consequence |
|---|---|---|
| J1-S04-C001 | B 後及 D 有一致 High，因此可優先隔離並確認 B 支線；C 要重測，現時未證實最終來源。 | Valid；`j_source_reasoning_valid = true` |
| J1-S04-C002 | B 是 High，所以已證實工業設施違規及造成居民不適。 | Near-miss；模擬顯示記者誤報、設施申訴及確認工作仍未完成，要求公開修窄 |
| J1-S04-C003 | A 是 Low，所以整條河已安全。 | Near-miss；鏡頭沿水流移到下游 High，要求區分上游位置與整條河 |
| J1-S04-C004 | C 有一個 Low，可以刪掉 High，這樣地圖更整齊。 | Near-miss；兩個原始結果重新出現，要求保留不一致及安排重測 |

若先選近似主張，後果保留在任務簿「曾修訂的說法」中，但不扣分。玩家查回 controls、水流及重複後可局部換卡。

| ID | Speaker | Line |
|---|---|---|
| J1-S04-D001 | 周穎 | 你的證據足以支持一個可逆的優先檢查行動，未足以代替正式確認、執法或健康判斷。 |
| J1-S04-D002 | 陳姨 | 先說清楚「知道甚麼」和「下一步查甚麼」，比一句保證更有用。 |

## 11. J05：把好主意放進安全系統

### 場景

研究站顯示一個沒有真實細胞的公共監測概念模型。玩家要把居民提出的三個問題轉成設計：

1. 外殼受損時，內容物會否仍被第二層封住？
2. 使用後由誰密封、標記及交回？
3. 誰可操作、誰可停用、異常時通知誰？

### 安全卡

| Layer | Valid Card | Near-miss |
|---|---|---|
| 物理 | 內部密封測試匣＋外部次級封閉；破損即停用 | 只有一層外殼，並寫「不會破」 |
| 程序 | 每匣有編號；受訓人員密封交回；工程細胞與疑似污染物按受控流程處置 | 使用者自行倒空、清洗或丟入普通垃圾 |
| 治理 | 限授權操作；異常隔離停用、保存紀錄並通知主管單位及居民聯絡人 | 裝置自動宣布公共安全結論，沒有人可以覆核 |

### 失效模擬

| Test | 必須看見的因果 |
|---|---|
| 外殼跌落 | 只有外層破損時，內部密封仍完整；系統仍停用並交回，不把第二層寫成零風險 |
| 標籤脫落 | 沒有編號便不能追蹤；玩家加入耐用識別及交接紀錄 |
| False alert | 裝置只發出「待確認」通知；受訓人員覆核，不自動封城或指控來源 |

三層通過後設定 `j_safe_package_valid = true`。

| ID | Speaker | Line |
|---|---|---|
| J1-S05-D001 | 方雅 | 安全不是一張「保證卡」。不同層處理不同失效，而且要留下誰負責的紀錄。 |
| J1-S05-D002 | 陳姨 | 我不需要你說永遠不會出事；我需要知道出事時誰停、誰查、誰通知。 |

## 12. J06：說清楚，再換一個例子

### Use–Limit–Next

玩家從六張卡組合三句公開說明：

| Type | Valid Card | Near-miss |
|---|---|---|
| Use | 封閉式工程細胞感測概念可以提供初步 reporter 訊號，協助決定哪裡優先檢查。 | 工程細胞已找出並清除了全部污染。 |
| Limit | 訊號不是最終來源、濃度、安全、健康因果或清理證明；本章結果是教學模擬。 | 只要 controls 通過，結果便適用於所有河流及所有汞形態。 |
| Next | 專業團隊會重測不一致位置，並以合資格方法確認、處置及更新居民。 | 玩家現在批准把工程細胞放進河流長期監測。 |

三張有效卡設定 `j_statement_valid = true`。

### Transfer Challenge

介面換成另一個虛構「綠色 reporter」模型，只提供新圖示，不使用 MerR 名稱：

| Condition | Result |
|---|---|
| Known-low | Low |
| Known-high | Low |
| Unknown | Low |

| ID | Choice | Result |
|---|---|---|
| J1-S06-C001 | Unknown 沒有目標輸入。 | 不足；known-high 也失敗 |
| J1-S06-C002 | 這輪測試不能回答 unknown；先檢查為甚麼 known-high 沒有預期訊號。 | Valid；`j_transfer_valid = true` |
| J1-S06-C003 | 綠色 reporter 不可靠，所以所有細胞感測器都沒有用。 | 過度推廣；只知道本輪 control 失敗 |

### 結算

| ID | Speaker | Line |
|---|---|---|
| J1-S06-D001 | 林博士 | 你沒有只記住紅色卡的位置。換了 reporter，你仍先檢查證據能不能回答問題。 |
| J1-S06-D002 | 方雅 | 這就是微界工程師的工作：設計、測試、承認限制，再把安全和人的需要帶回下一輪。 |
| J1-S06-D003 | 陳姨 | 好的說明不是最響亮，而是讓我們知道可以怎樣行動、還欠甚麼答案。 |

完成後原子寫入 `p_junior_complete = true`，解鎖四枚不排名的任務章：

- 找線索；
- 建模型；
- 公平測試；
- 誠實說明。

| ID | UI Text |
|---|---|
| J1-S06-UI001 | Junior Mission 完成：你用 controls 檢查測試，用有限主張連接證據與行動。 |
| J1-S06-UI002 | 完成遊戲不等於取得實驗資格；不要自行接觸或測試真實污染物。 |
| J1-S06-UI003 | 返回研究總部 |

## 13. 3D 與互動最低要求

本任務不能退化成連續答題頁：

| Scene | 必要空間行動 | 不可由純文字替代 |
|---|---|---|
| J01 | 在步道走訪 A–D、沿水流箭頭回看上下游 | 候選點相對位置及匯流關係 |
| J02 | 把 DNA 卡放進兩條軌道、input 放入 environment、protein 出現在 output | DNA／環境／細胞輸出的空間層級 |
| J03 | 把三類資料匣放上讀取器、發現 failed control、重設數位 run | Control failure 阻止 unknown 結論 |
| J04 | 把讀值放回 3D 水流圖並沿支線查看後果 | 局部結果不可推廣成整條河結論 |
| J05 | 走入裝置剖面、關閉第二層、掃描標籤及按停用流程 | 多層控制處理不同失效 |

Critical Path 的每個核心學習 gate 都必須由玩家完成至少一個可觀察的空間或因果操作，例如走訪相對位置、放置卡牌、作出預測、執行測試或修訂主張。對話可提供情境、提示及回復，但不能直接替玩家完成 gate；是否保留 3D 應由目標玩家測試證明空間行動確實提升理解，而不是用任意時間百分比判定。

## 14. 學習證據與教師討論

### 14.1 遊戲內可觀察證據

| Learning Claim | Required Behaviour | 不可替代的弱證據 |
|---|---|---|
| 區分 DNA／protein | 在 J02 把新外觀 reporter gene／protein 放入正確層級 | 只跟讀定義 |
| 理解 controls | J03 及 J06 都在 known-high 失敗時拒絕判讀 unknown | 第一次跟隨高亮 |
| 限定訊號範圍 | J04 選「優先確認」及 J06 完成 Limit 卡 | 只說「紅光代表汞」 |
| 理解封閉與權責 | J05 完成三層方案，J06 拒絕自行部署 | 只選一張寫有「安全」的卡 |

### 14.2 三條課後問題

1. 如果 unknown 是 Low，但 known-high 也是 Low，為甚麼不能說 unknown 沒有目標輸入？
2. 紅色 reporter signal 能幫助我們做甚麼？它不能證明甚麼？
3. 如果監測盒外層破了，除了加厚盒子，還有哪些人和程序要參與？

教師指南不可把 NPC 對白當成標準背誦答案；可要求學生畫出 Evidence → Claim → Consequence，並提出另一個需要修窄的說法。

## 15. 灰盒驗收

1. 小四至小六零背景玩家在提示可用的情況下，中位數目標 18–22 分鐘完成；正式門檻須由先導測試校準。
2. 玩家在 60 秒內取得移動控制，兩分鐘內完成第一個有意義的地圖標記。
3. 所有必要卡同時有圖形、文字及可讀標籤；200% zoom、鍵盤、觸控及非拖曳模式均可通關。
4. J03 first run 的 known-high 失敗必須阻止有效 unknown 結論，但不阻止玩家觀看後果及修正。
5. J06 使用新 reporter 外觀，避免只測量玩家是否記住紅色卡或位置。
6. 河流不發紅、工程細胞不出現在戶外、玩家不接觸樣本，也不取得醫療、執法、清理或部署權。
7. 任務完成畫面不得宣稱玩家已證明團隊迴路效能或學會完整合成生物學。
8. 研究測試若收集未成年人資料，須先按學校、機構及所在地要求處理同意、私隱、錄影及退出安排。

## 16. 仍需正式輸入

- 香港小學教師審讀繁體中文、年級詞彙及 18–22 分鐘課堂安排。
- 團隊 Science Lead 確認 `MerR/Pmer` proposal 表述；有實驗結果後只更新相應數據層，不改寫 controls 與 claim scope 原則。
- Accessibility reviewer 驗證鍵盤、screen reader、zoom、色覺及降低動態流程。
- Safety／Human Practices reviewers 確認封閉、居民角色、公共聲明及未成年人活動安排。
- 以至少一輪無提示 transfer 訪談檢查玩家是否學會因果，而非只學會介面卡位。

## 17. 內容依據

- 團隊來源 `TEAM-PDF-2026-INTRO`，頁 1–2：`Pconst → merR`、`Pmer → dTomato` 及 `Hg²⁺` 依賴報告概念；第 3 頁起 aptamer 內容不屬本任務。
- Shewchuk et al., [Initial characterization of DNA and mercury(II) binding activities of the MerR protein from the Tn501 mercury resistance operon](https://pubmed.ncbi.nlm.nih.gov/2719955/)（1989）。
- Shewchuk et al., [Transcriptional switching by the MerR protein](https://pubmed.ncbi.nlm.nih.gov/2497778/)（1989）。
- World Health Organization, [Mercury and health](https://www.who.int/news-room/fact-sheets/detail/mercury-and-health)。
- iGEM Responsibility, [Working Safely](https://responsibility.igem.org/guidance/working-safely)。

---

## 核准

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Lead Game Designer |  |  |  |  |
| Primary Education Reviewer |  |  |  |  |
| Science Lead |  |  |  |  |
| Safety / Human Practices Lead |  |  |  |  |
| Accessibility Reviewer |  |  |  |  |
| Technical / QA Lead |  |  |  |  |
