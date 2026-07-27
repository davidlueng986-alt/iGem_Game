# 《微界工程師：生命迴路》前導章完整實作腳本

> 工作名稱｜前導章《第一條生命迴路》｜2D Card Tutorial & Narrative Script｜版本 1.2

| 文件欄位 | 內容 |
|---|---|
| 章節標記 | Pre-Chapter；完整故事首次遊玩位於第一章之前 |
| 對應 GCP | `00_GAME_CONCEPT_PROPOSAL.md` 版本 1.4 |
| 體驗類型 | 固定解題式 2D 卡牌、即時因果動畫、短敘事轉場 |
| Critical Path | 引導模式約 5–6 分鐘；標準模式約 6–7 分鐘；待灰盒計時驗證 |
| 首次遊玩上限 | 8 分鐘；不含模式及無障礙設定 |
| 玩家角色 | 剛到研究站報到的生物設計與安全調查員 |
| 遊戲模式 | 引導模式／標準模式，共用相同科學因果 |
| 來源成熟度 | 通用合成生物學入門教學；MerR 機制有文獻基礎，第一章橋接為團隊已選定但尚未實測的 proposal |
| 腳本狀態 | 編輯自審後可製作灰盒；科學、教育、無障礙及兒童測試簽核待完成 |

---

## 1. 體驗定位

### 1.1 設計目的

前導章解決一個明確問題：Story Campaign 的零生物學背景玩家若直接進入汞感測危機，可能記住卡牌答案，卻沒有建立「細胞如何讀取 DNA、基因迴路如何回應輸入、測試為何需要對照」的基本心智模型。本章以中一或以上及一般公眾為主要驗證對象；小四至小六使用獨立 `17_JUNIOR_MISSION_FULL_SCRIPT.md`，不以引導模式替代適齡驗證。

本章不是章前講義，也不是術語測驗。玩家要在研究站的數位訓練桌上完成一條從目的到證據的短循環：

> 定義需要 → 組合 DNA 功能 → 預測細胞輸出 → 使用對照測試 → 限定結論 → 進入第一章應用

### 1.2 玩家體驗承諾

- 玩家在 30 秒內完成第一個有意義的卡牌互動並看見 DNA 軌道，不先閱讀長篇定義。
- 每個正式術語都先由可見因果引出，再顯示名稱。
- 錯誤放置會播放「如果這樣設計會發生甚麼」，不扣分、不倒數、不羞辱。
- 卡牌沒有隨機抽取；所有玩家都能接觸相同的最低基礎知識。
- 完成後直接進入第一章，通用卡牌會轉化成 `Pconst/merR/Pmer/dTomato` 的具體案例。
- 本章不取代教師指南，但讓家中及標準模式玩家可在沒有真人逐句講解下開始遊戲。
- 引導模式是主線支架而非小學產品標籤；任何玩家均可選用，canonical 科學因果不變。

### 1.3 明確非目標

- 不教授真實基因序列、菌株建構、培養、轉染、誘導或量測操作。
- 不把生物系統描寫成可在任何宿主或環境自由互換的電子積木。
- 不要求玩家背誦分子名稱才可通關。
- 不把完成卡牌等同具備實驗資格或已製造真實工程生物。
- 不以紅光、ON 或一輪模擬結果證明真實樣本身分、濃度、安全或污染清除。

## 2. 玩家能學會的合成生物學知識

### 2.1 核心定義

本章建立的工作定義是：

> 合成生物學使用工程式的設計、建構、測試與學習循環來研究或改造生物系統，使它們在特定情境下執行有定義的功能；設計仍會受細胞、環境、量測、安全、倫理及使用者需要限制。

引導模式首次顯示：「我們可以設計生物系統去完成一個清楚任務，再測試它是否真的照預期工作。」正式定義可在知識圖鑑展開，不要求一次讀完。

### 2.2 概念、正確理解與遊戲證據

| Knowledge | 玩家應建立的正確理解 | 玩家在本章做出的可觀察證據 |
|---|---|---|
| 細胞 Cell／Chassis | 細胞是讀取生物指令並產生 RNA、蛋白質及其他功能的活系統；不是空盒或藥瓶 | 把 DNA 設計放入細胞模型後，依序觀察 transcription 與 translation 兩個不同分子過程；不暗示細菌內有細胞核分隔 |
| DNA | DNA 儲存可被細胞讀取的遺傳資訊；DNA 本身不是螢光蛋白 | 拒絕把「蛋白質輸出」卡放進 DNA 軌道 |
| 基因 Gene | 基因可產生功能 RNA，或包含製造蛋白質所需資訊；本章聚焦蛋白質編碼基因 | 把 reporter gene 放入 DNA 軌道，並在細胞輸出區看到 reporter protein 出現 |
| 啟動子 Promoter | promoter 是影響轉錄開始的調控 DNA 區域，不是製造蛋白質的基因，也不保證完美二元 ON/OFF | 把 promoter 放在被調控基因之前，並比較低背景與較高輸出 |
| 調控蛋白 Regulator | regulator 可依自身狀態改變特定 promoter 的轉錄；實際效果取決於系統與情境 | 建立 regulator 轉錄單元，讓 input 改變 regulator 對受調控 promoter 的作用 |
| 輸入 Input | input 是系統要回應的條件，不是必須被放進 DNA 的零件 | 把 input token 放在細胞環境端口，而不是 DNA 軌道 |
| 報告基因與報告蛋白 Reporter | reporter gene 是 DNA 指令；reporter protein 是可觀察輸出。訊號只報告迴路狀態，不等於目標物本身 | 在 DNA 區與細胞輸出區正確區分兩張卡 |
| 終止子 Terminator | terminator 在本教學模型中標示轉錄單元結束，協助界定兩個單元 | 在每條 DNA 軌道末端放置 terminator |
| 基因表達 Gene Expression | 細胞先從 DNA 產生 RNA，再依 protein-coding RNA 資訊產生蛋白質；兩者是不同分子過程，在細菌中可以在空間與時間上耦合 | 觀看 DNA → RNA → protein 的分段概念動畫並完成順序預測 |
| 基因迴路 Genetic Circuit | 多個調控元件可形成輸入、處理與輸出的關係；迴路是可測模型，不是必然成功的成品 | 組合兩個轉錄單元並預測 input absent／present 的輸出 |
| 低背景與 ON/OFF | OFF 代表低於本教學判讀界線，不代表絕對沒有轉錄、蛋白質或儀器背景 | 選擇「低背景／OFF」，而不是「完全零分子」 |
| 對照 Control | 已知預期結果的條件用來判斷一輪測試是否正常；未知樣本不能代替對照 | 同時選擇已知應低與已知應高的控制條件 |
| 篩查與確認 | reporter 訊號可提供篩查線索；樣本身分、濃度、安全及因果仍需合適確認 | 從有效模擬結果組成包含用途、限制與下一步的聲明 |
| DBTL | Design–Build–Test–Learn 是重複循環；本章只作第一次引入，後續章節再直接評量修訂能力 | 依序完成 need、design、predict、test、learn；若出現錯誤則保留因果並修正，不強迫玩家故意答錯 |
| 封閉與責任 | 改變生物系統要同時考慮使用邊界、暴露、廢物、授權及受影響者；「封閉」不等於零風險 | 選擇封閉數位／設備情境、確認包材與處置、拒絕直接環境釋放推論 |

### 2.3 完成本章後的最低學習成果

本文件中的「學會」是指玩家能在本章或緊接的 transfer prompt 中表現出一個初步、可修正的心智模型，不代表長期記憶或完整掌握。DNA／protein 層級、input-regulator-output、controls 及 claim scope 由玩家直接作答；terminator、chassis、DBTL 名稱與 context dependence 在本章引入，並由後續章節反覆鞏固。

玩家應能在不看標準答案時：

1. 用自己的話說明 DNA 指令、細胞及蛋白質輸出不是同一件事。
2. 指出 promoter、regulator、reporter gene、reporter protein 和 input 在簡單迴路中的不同角色。
3. 預測簡化感測迴路在「沒有輸入」與「有輸入」時的低／高輸出。
4. 選出一個已知應低及一個已知應高的對照，並說明缺少對照會令結論變弱。
5. 說明可觀察訊號是篩查線索，不是安全證明、濃度答案或污染清除。
6. 說明合成生物學包含設計、測試、修正及責任邊界，不只是「把基因放進細胞」。

### 2.4 本章不能證明玩家已學會的內容

- 不證明玩家理解完整分子生物學、所有 RNA 類型或所有 promoter 調控機制。
- 不證明玩家能進行真實實驗、風險評估、統計分析或法規判斷。
- 不證明第一章團隊迴路已有實測效能。
- 不應由完成時間或錯誤次數推論玩家能力、年齡或科學態度。

## 3. How It Works／遊戲如何運作

### 3.1 核心玩家循環

1. **Need：** 翻開一張功能需要卡，先知道系統要回答甚麼問題。
2. **Design：** 把 DNA 元件放到一或兩條轉錄單元軌道。
3. **Predict：** 在執行前選擇沒有／有 input 時的預期輸出。
4. **Test：** 用已知應低、已知應高及未知條件執行教學模擬。
5. **Learn：** 根據因果動畫修正卡牌或縮小結論。
6. **Scope：** 組合「能做甚麼、不能證明甚麼、下一步由誰負責」。

沒有抽牌機率、卡組構築、戰鬥或高分。挑戰來自建立正確因果，而不是運氣或反應速度。

### 3.2 2D 桌面區域

| Zone | 固定位置 | 功能 |
|---|---|---|
| Need Strip | 上方全寬 | 顯示目前要解決的需要及不可改寫的成功條件 |
| Card Hand | 左側／窄屏下方 | 依場景顯示可用卡；不以隨機順序隱藏關鍵卡 |
| DNA Rail A/B | 中央 | 只接受 DNA 元件；每格有 role 而非唯一卡名驗證 |
| Cell Environment Port | DNA 軌道左外側 | 接受 input token；用空間位置區分環境條件與 DNA |
| Cell Output Area | 右側 | 顯示 RNA、regulator protein、reporter protein 及讀取狀態 |
| Evidence Tray | 下方 | 放置控制條件、結果與結論卡 |
| Concept Stamps | 右上 | 顯示「指令、迴路、證據、責任」四個完成章，不顯示分數 |

### 3.3 操作規則

- 滑鼠可拖曳，也可先選卡再選槽位；兩種方式完全等價。
- 鍵盤以方向鍵移動 focus、Enter 選取、Escape 取消；不要求精細拖曳。
- 觸控使用單擊選卡、單擊槽位，不依賴 hover。
- 卡牌放錯區域時不會消失；系統播放 2–4 秒因果動畫後送回手牌。
- 玩家可隨時開啟「目前模型」，查看已出現過的術語與動畫，不暫停計時，因為本章沒有限時評分。

### 3.4 首次、重玩與單章行為

| Context | Rule |
|---|---|
| 新 profile 完整故事 | 模式／無障礙設定後必須完成一次；不能以未知知識狀態直接跳入第一章 |
| 已完成 profile | 可選「快速重溫」或直接開始第一章；前導章可由研究總部重玩 |
| 第一章工作坊單章 | 若 `p_prechapter_complete` 不存在，先提供 90 秒「核心三題」壓縮版或由導師啟動全班示範；不偽造已完成 |
| 第二至七章 standalone | 各章仍載入自己的必要前置概念；不要求先完成本章 |
| 展覽快速重設 | 工作人員可保留全域完成旗標但清除章內狀態；畫面必須標示「前導已由場地示範」 |

#### Loader 與版本路由

目前完整前導 schema version 為 `1`：

| Saved／Session State | Requested Route | Loader Result | Save Effect |
|---|---|---|---|
| `p_prechapter_complete = false`、完整故事 | 開始第一章 | 先進入完整前導；完成後進 Chapter 1 S00 | 原子寫入 complete、version、support |
| `p_prechapter_complete = false`、`pre_quick_primer_seen = false`、第一章 standalone | 開始第一章 | 先進入 90 秒核心三題版，再返回 Chapter 1 S00 | 只設定 session flag，不寫 profile completion |
| 同上、工作坊導師已在共用畫面完成三題示範 | 導師確認「本裝置已參與示範」 | 直接設定 session flag，再進 Chapter 1 S00；只在工作坊／展覽 preset 顯示 | 不寫 profile completion |
| `p_prechapter_complete = false`、`pre_quick_primer_seen = true` | 返回 Chapter 1 S00 | 不再呼叫 primer，避免循環 | 無 |
| `p_prechapter_complete = true`、`p_prechapter_version = 1` | 開始第一章 | 直接進 Chapter 1 S00；可從研究總部另選快速重溫或完整重玩 | 無 |
| `p_prechapter_complete = true`、version 小於目前版本 | 開始第一章 | 顯示內容更新，完成 90 秒核心重溫後進入；保留原 support | 只把 version 更新為 `1` |
| 已完成 profile | 快速重溫 | 執行核心三題，不改完成狀態或 support | 無 |
| 已完成 profile | 完整重玩 | 清除 pre-chapter local state；確認完成後才替換 support 及 version | 原子更新三個 profile fields |

玩家退出未完成的重玩時保留原 profile fields，不把半完成狀態當成新版完成。

#### 90 秒核心三題版

壓縮版只為維持第一章 15–30 分鐘工作坊時段，不取代完整前導，也不寫入 `p_prechapter_complete`：

| Time | Prompt | Required Response |
|---:|---|---|
| 30 秒 | 把 reporter gene 與 reporter protein 分到 DNA／Cell Output 兩區 | DNA 是指令層，protein 是細胞輸出層 |
| 30 秒 | 預測 generic input absent／present | absent 為低背景，present 為較高 reporter output |
| 30 秒 | 從 known-low、known-high、unknown 及 claim cards 選擇最低證據組合 | 兩個 controls 都要使用；High 只作篩查線索 |

三題完成設定 session-only `pre_quick_primer_seen = true`，第一章照常開始。答錯可立即觀看因果再重選；90 秒是目標中位數，不設硬倒數。研究總部仍把完整前導標成「尚未完成」。

全班示範不會由一部主機靜默替其他裝置完成。每部 client 必須由導師在受限工作坊／展覽 preset 明確確認「本裝置已參與示範」，才設定同一 session flag；一般家用介面不顯示此控制。

### 3.5 雙模式差異

| Dimension | 引導模式 | 標準模式 |
|---|---|---|
| DNA 軌道 | 顯示 role 輪廓與逐格 snap；兩個 terminator 已附在單元尾端但仍顯示名稱 | 玩家獨立放置 promoter、gene、terminator，無卡名輪廓 |
| 正式術語 | 圖像短稱先出現，正式名稱固定顯示於副標 | 正式名稱先出現，可展開機制說明 |
| 表達動畫 | 「抄寫指令」與「製作蛋白質」圖像，加上 transcription／translation 標籤 | 分開顯示 DNA、RNA、protein 及背景輸出 |
| 預測 | OFF／ON 兩格，使用低／高圖示 | 低背景、判讀閾值、input absent／present |
| 對照 | 已知應低、已知應高、未知三張卡 | 加入「陽性控制失敗」的第二輪診斷 |
| 錯誤卡 | 每個 gate 最多一張核心近似錯誤 | 每個 gate 兩至三張含範圍、證據或角色錯誤的近似答案 |
| 文字量 | 主線每句建議不超過 24 個中文字 | 主線每句建議不超過 46 個中文字，可展開延伸內容 |

### 3.6 提示梯度

| Hint Level | Trigger | Response |
|---|---|---|
| 方向提示 | 20 秒沒有有效操作或第一次要求提示 | 高亮正確區域，不高亮特定卡 |
| 原理提示 | 同一概念兩次錯誤或再次要求 | 重播相關因果，例如「蛋白質出現在輸出區，不在 DNA 軌道」 |
| 直接示範 | 三次錯誤、讀寫輔助開啟或玩家主動要求 | 系統放置一張卡，玩家完成剩餘因果 |

使用直接示範仍可完成，不降低章末文字、不標記失敗。`pre_support_level` 只用於調整第一章提示起點，不顯示給其他玩家或教師作能力排名。

### 3.7 與第一章的重複邊界

- 前導章只組 generic role model；翻牌只預告第一章名稱，不讓玩家完成 `MerR/Pmer` 的具名組裝 gate。
- 第一章 S03 仍要求玩家在新介面中重建兩個具名轉錄單元並解釋 MerR 的具體 absent／present 狀態，形成 transfer evidence。
- 前導章只有兩個基礎 controls；第一章標準模式加入程序空白、基質背景／反應、重複與地圖證據，不得剪成同一題重播。
- 除 `p_prechapter_support = demonstrated` 的 role 輪廓外，第一章不預填任何卡牌或答案。

## 4. 科學模型與內容界線

1. DNA 軌道是概念圖，不表示真實序列長度、方向比例、染色體位置或建構方法。
2. DNA Rail 與 Cell Output 是介面上的資訊層級，不代表細菌具有細胞核或 transcription／translation 必須位於分隔空間；兩個過程在細菌中可以耦合。
3. 本章聚焦 protein-coding gene；知識圖鑑補充有些基因產生功能 RNA，不把所有基因定義成蛋白質配方。
4. promoter 以低／高輸出教學，不宣稱背景為零或調控完全二元。
5. input 改變 regulator 狀態的動畫是抽象機制，不顯示結合常數、濃度、反應時間或分子操作。
6. 卡牌看似模組化不代表元件在不同宿主與條件中必然保持性能；S02 必須明說 context dependence。
7. 所有讀值標示「教學模擬」，沒有真實濃度或檢出限。
8. 第一章橋接只說明團隊已選定 proposal 的邏輯；MerR 機制有文獻基礎，但具體團隊構築尚未實測，不宣稱已完成菌株、產品或公共部署。
9. 工程細胞只存在於數位模型或後續封閉設備；前導章不呈現環境釋放作可選實作。

## 5. 角色與演出方向

| 角色 | 功能 | 表演方向 |
|---|---|---|
| 玩家 | 透過放卡、預測及聲明表達理解 | 無固定姓名、無配音；錯誤不觸發嘲笑反應 |
| 林博士 | 引出好奇心及具體機制，但不替玩家完成結論 | 語速稍快、願意承認模型限制，不把玩家當兒童說話 |
| 方雅 | 在最後一輪加入用途、安全及權責邊界 | 平靜、具體；不以恐嚇方式介紹生物安全 |
| 訓練系統 | 顯示狀態、因果及提示 | 中性短句；只判斷模型是否支持結論，不作倫理權威 |

## 6. 文案、ID 與狀態

### 6.1 ID 格式

```text
P-S##-D###   對白
P-S##-D###P  引導模式變體
P-S##-C###   玩家選項／結論卡
P-S##-C###P  同一 owning Choice 的引導模式短文案變體
P-S##-UI###  介面文字
P-S##-EV###  Gameplay event
PRE-CARD-### 卡牌資產／authoring ID
```

### 6.2 主要狀態旗標

| Flag | Type／Default | Set Condition | Scope／Reset | Consumer |
|---|---|---|---|---|
| `pre_expression_valid` | bool／false | DNA 元件與蛋白質輸出區分正確 | pre-chapter／重玩重設 | S02 解鎖 |
| `pre_circuit_valid` | bool／false | 兩個轉錄單元及 input 位置正確 | pre-chapter／重玩重設 | 狀態預測 |
| `pre_prediction_valid` | bool／false | absent 低背景、present 較高輸出 | pre-chapter／重玩重設 | S03 解鎖 |
| `pre_current_controls_valid` | bool／false | 當前 run 的已知應低及已知應高均符合預期 | run／每次重測重設 | 控制當前結論 badge |
| `pre_controls_valid` | bool／false | 至少完成一次兩個 controls 均符合預期的 run | pre-chapter／重玩重設 | 完成 milestone；後續 failed-control run 不清除 |
| `pre_failed_control_diagnosed` | bool／false | 玩家正確處理陽性控制失敗；兩種模式均預設 false | pre-chapter／重玩重設 | 概念摘要與完成 gate |
| `pre_test_claim_valid` | bool／false | 第一輪選擇有邊界的篩查結論 C001 | pre-chapter／重玩重設 | S03 exit gate |
| `pre_scope_valid` | bool／false | 用途、限制及下一步三卡正確 | pre-chapter／重玩重設 | 完成 gate |
| `pre_support_level` | enum／`independent` | 使用提示後依序為 `hinted`／`demonstrated` | pre-chapter／重玩重設 | 第一章初始提示，不作分數 |
| `pre_quick_primer_seen` | bool／false | 第一章 standalone 完成核心三題，或工作坊／展覽 preset 由導師逐裝置確認已參與示範 | session／離開第一章重設 | 允許進入 Chapter 1 S00；不寫 profile completion |
| `pre_complete` | derived／false | `pre_expression_valid AND pre_circuit_valid AND pre_prediction_valid AND pre_controls_valid AND pre_failed_control_diagnosed AND pre_test_claim_valid AND pre_scope_valid` | pre-chapter | 寫入 profile |
| `p_prechapter_complete` | bool／false | 首次完成 `pre_complete` | profile／工作人員可重設 | 首次 gate、重玩及單章壓縮版 |
| `p_prechapter_version` | int／0 | 完成時寫入本章 save schema version `1` | profile／版本遷移 | 內容更新後判斷是否需重溫 |
| `p_prechapter_support` | enum／`independent` | 完成時複製 `pre_support_level` | profile／下次完整重玩更新 | 第一章提示起點；不顯示為分數 |

## 7. 卡牌系統規格

### 7.1 卡牌視覺語法

每張卡固定包含：role icon、正式名稱、短稱、所屬區域形狀、單句功能和非顏色狀態符號。DNA 卡左／右邊使用拼接缺口；環境 input 為六角 token；protein output 為圓形結果卡；evidence card 為有缺角的文件形狀。顏色只作輔助。

### 7.2 核心卡牌清單

| Card ID | Formal Label | 引導短稱 | Valid Zone | Function／Boundary |
|---|---|---|---|---|
| `PRE-CARD-001` | Functional Need | 任務 | Need Strip | 「只在特定 input 條件出現時提供可觀察訊號」 |
| `PRE-CARD-002` | Constitutive promoter | 常開啟動子 | DNA Rail A；S01 可放 Rail B | S01 支持 reporter gene；S02 移到 Rail A 支持 regulator gene；不表示輸出完全固定 |
| `PRE-CARD-003` | Regulator gene | 調控員指令 | DNA Rail A | 讓細胞產生 regulator protein |
| `PRE-CARD-004` | Regulated promoter | 受控啟動子 | DNA Rail B | 活性受 regulator 狀態影響 |
| `PRE-CARD-005` | Reporter gene | 報告員指令 | DNA Rail B | 讓細胞產生可觀察 reporter protein |
| `PRE-CARD-006A` | Transcription terminator A | 停止標誌 A | DNA Rail A | 界定第一轉錄單元末端 |
| `PRE-CARD-006B` | Transcription terminator B | 停止標誌 B | DNA Rail B | 界定第二轉錄單元末端 |
| `PRE-CARD-007` | Input condition | 輸入條件 | Cell Environment Port | 改變 regulator 狀態；不是 DNA 元件 |
| `PRE-CARD-008` | Regulator protein | 調控蛋白 | Cell Output／動畫 | 由 regulator gene 表達；不可手動放入 DNA |
| `PRE-CARD-009` | Reporter protein | 可觀察訊號 | Cell Output／動畫 | 由 reporter gene 表達；訊號不等於 input 本身 |
| `PRE-CARD-010` | Known expected-low control | 已知應低 | Evidence Tray | 檢查背景是否維持在教學低狀態 |
| `PRE-CARD-011` | Known expected-high control | 已知應高 | Evidence Tray | 檢查系統是否能產生預期高輸出 |
| `PRE-CARD-012` | Unknown condition | 未知 | Evidence Tray | 只有在控制條件有效時才可形成篩查結論 |
| `PRE-CARD-013` | Use statement | 能做甚麼 | Claim Tray | 封閉模型在受測條件下提供篩查訊號 |
| `PRE-CARD-014` | Limitation statement | 不能證明甚麼 | Claim Tray | 不證明身分、濃度、安全、因果或清除 |
| `PRE-CARD-015` | Responsibility statement | 下一步 | Claim Tray | 封閉、確認、處置、授權與溝通仍需負責 |

## 8. 前導章總流程

| Scene | 名稱 | 引導模式 | 標準模式 | Player Output | Exit Gate |
|---|---|---:|---:|---|---|
| S00 | 一張空白任務卡 | 25–30 秒 | 25–30 秒 | 接受功能需要，不先選零件 | Need card revealed |
| S01 | 指令不是成品 | 55–65 秒 | 60–70 秒 | 區分 DNA 元件與 protein output | `pre_expression_valid` |
| S02 | 只在需要時回應 | 85–95 秒 | 95–105 秒 | 組合兩個單元並預測 absent／present | `pre_circuit_valid AND pre_prediction_valid` |
| S03 | 沒有對照就沒有答案 | 70–80 秒 | 85–95 秒 | 配置控制條件並限定篩查結論 | `pre_controls_valid AND pre_failed_control_diagnosed AND pre_test_claim_valid` |
| S04 | 訊號不是保證 | 50–60 秒 | 60–70 秒 | 組合用途、限制及責任聲明 | `pre_scope_valid` |
| S05 | 第一個真實問題 | 25–30 秒 | 25–30 秒 | 取得四枚概念章並轉入第一章 | `pre_complete` |

## 9. S00：一張空白任務卡

### 場景與演出

模式與無障礙設定完成後，畫面由黑轉入研究站訓練桌。Three.js 只顯示低成本靜態背景：林博士站在桌旁、遠處設備慢速運作；主要互動是置中的 HTML 2D 卡牌層。桌上沒有預先組好的迴路，只放一張背面朝上的 Need card。

### 主線對白

| ID | Speaker | Line | Direction |
|---|---|---|---|
| P-S00-D001 | 林博士 | 歡迎來到研究站。先別急著拿零件；設計從「需要系統做甚麼」開始。 | 句末翻開 Need card |
| P-S00-D001P | 林博士 | 先問任務，再選零件。今天的任務是：只在特定條件出現時給我們一個看得到的訊號。 | 引導模式 |
| P-S00-D002 | 訓練系統 | 功能需要已鎖定：特定 input 出現時提高可觀察輸出；沒有 input 時維持低背景。 | 標準模式 |

### UI

| ID | Text | Notes |
|---|---|---|
| P-S00-UI001 | 前導章：第一條生命迴路 | 章名 |
| P-S00-UI002 | 需要：只在特定條件出現時提供可觀察訊號 | Need Strip，不使用操作教學句 |
| P-S00-UI003 | 所有結果都是教學模擬，不是實驗或安全證明。 | 固定可展開標示 |

### Gameplay Event

| ID | Event | Result |
|---|---|---|
| P-S00-EV001 | 玩家翻開 Need card | DNA Rail A/B、Card Hand 及第一枚「指令」概念章淡入；進入 S01 |

## 10. S01：指令不是成品

### Round Goal

先建立最小表達模型，讓玩家看見 promoter、reporter gene 和 terminator 位於 DNA 軌道，而 reporter protein 出現在細胞輸出區。此輪暫不加入 input 與 regulator。

### 正確配置

```text
DNA Rail B：PRE-CARD-002 constitutive promoter → reporter gene → terminator
Cell Output：DNA → RNA → reporter protein／可觀察訊號
```

S01 明確允許 `PRE-CARD-002` 暫時放入 Rail B 作最小 constitutive reporter；S02 開始時它會移到 Rail A，Rail B 改用 regulated promoter。引導模式 terminator 已附在軌道末端，玩家仍需點擊它查看名稱；標準模式由玩家放置三張 DNA 卡。

### 玩家放置與回復

| Trigger | System Animation | Feedback Line |
|---|---|---|
| reporter protein 放入 DNA Rail | 圓形蛋白卡無法接上 DNA 缺口，移到 Cell Output | `P-S01-D003` |
| reporter gene 放入 Cell Output | DNA 指令卡保持未讀狀態，不產生訊號 | `P-S01-D004` |
| promoter 放在 gene 後方 | RNA 起點找不到，軌道不執行 | `P-S01-D005` |
| 未放 terminator 便執行 | 單元末端保持「未界定」，可看動畫但不通過 | `P-S01-D006` |
| 配置正確 | 顯示抽象 transcription，再顯示 translation 與 protein output | `P-S01-D007` |

### 對白

| ID | Speaker | Line |
|---|---|---|
| P-S01-D001 | 林博士 | DNA 保存可被細胞讀取的資訊。這一輪我們用一個 protein-coding reporter gene 看見輸出。 |
| P-S01-D002P | 林博士 | DNA 像指令；細胞讀取 reporter gene 後，才製作看得見的 reporter protein。 |
| P-S01-D003 | 訓練系統 | 這張是 reporter protein，屬於細胞產生的輸出，不是放進 DNA 的指令。 |
| P-S01-D004 | 訓練系統 | reporter gene 是 DNA 指令。把它放回 DNA 軌道，細胞才有可讀取的資訊。 |
| P-S01-D005 | 林博士 | promoter 是調控轉錄開始的位置。把結果卡放亮，不會補回缺少的調控起點。 |
| P-S01-D006 | 林博士 | 這個概念模型還缺少轉錄單元的終點。terminator 幫我們界定單元，但真實表現仍要測試。 |
| P-S01-D007 | 訓練系統 | 路徑完成：DNA 資訊先轉成 RNA，再產生 reporter protein。指令、細胞和輸出是三個不同層次。 |

配置完成設定 `pre_expression_valid = true`，點亮「指令」概念章。

## 11. S02：只在需要時回應

### Round Goal

訓練系統把「一直產生訊號」標成不符合 Need card。玩家把第一輪擴充成兩個轉錄單元，並把 input 放在細胞環境端口。

### 正確概念配置

```text
Transcription Unit A：constitutive promoter → regulator gene → terminator
Transcription Unit B：regulated promoter → reporter gene → terminator
Environment：input condition → 改變 regulator protein 狀態
Output：regulated promoter 活性改變 → reporter output 改變
```

這是功能層級模型，不表示所有 regulator 都以相同方式工作。

### 主線對白

| ID | Speaker | Line |
|---|---|---|
| P-S02-D001 | 林博士 | 第一輪會一直產生訊號，但任務要求系統回應一個條件。我們需要 regulator 和受它影響的 promoter。 |
| P-S02-D001P | 林博士 | 加入一個「感受條件的調控員」，讓報告訊號不是一直開著。 |
| P-S02-D002 | 林博士 | input 不屬於 DNA 軌道。它在細胞所處的環境中出現，再改變 regulator 的狀態。 |
| P-S02-D003 | 訓練系統 | 兩個轉錄單元已界定。下一步：執行前預測 absent／present 狀態。 |

### 錯誤回復

| Trigger | Consequence | Line |
|---|---|---|
| input token 放入 DNA Rail | input 保持外部六角形，DNA 軌道拒絕 | `P-S02-D004` |
| regulator protein 代替 regulator gene | Unit A 沒有 DNA 指令，重設 | `P-S02-D005` |
| reporter 接到 constitutive promoter | absent 狀態仍顯示高輸出，不符合 Need | `P-S02-D006` |
| 只組 Unit B、缺少 regulator source | regulated promoter 狀態未定，不能預測 | `P-S02-D007` |

| ID | Speaker | Line |
|---|---|---|
| P-S02-D004 | 訓練系統 | input 是環境條件，不是這條 DNA 設計的一部分。把它放到 Cell Environment Port。 |
| P-S02-D005 | 林博士 | 調控蛋白是細胞產生的結果；DNA 軌道需要的是 regulator gene 指令。 |
| P-S02-D006 | 訓練系統 | reporter 仍由常開 promoter 控制，所以沒有 input 時也維持高輸出。這不符合 Need card。 |
| P-S02-D007 | 林博士 | 受控 promoter 要有相應 regulator 的來源，否則我們連預期狀態也說不清楚。 |

### 狀態預測

| ID | State | Choice | Result |
|---|---|---|---|
| P-S02-C001 | Input absent | 低背景／OFF，不宣稱絕對零 | Correct |
| P-S02-C002 | Input absent | 完全沒有任何 RNA 或 protein | Near miss；忽略背景與既有分子 |
| P-S02-C003 | Input present | reporter output 高於本教學判讀界線／ON | Correct |
| P-S02-C004 | Input present | input 本身變成 reporter protein | Incorrect layer；input 與 output 混淆 |

玩家完成 C001 與 C003 後，系統依序執行 absent／present 動畫，設定 `pre_circuit_valid = true` 及 `pre_prediction_valid = true`。

### 第一章橋接翻牌

動畫暫停，通用卡牌翻到背面的第一章案例名稱：

| Generic Role | Chapter 1 Concept Card | Boundary |
|---|---|---|
| constitutive promoter | `Pconst` | 概念上支持 `merR` 表達；實際強度待資料 |
| regulator gene／protein | `merR`／MerR | MerR 對 `Hg²⁺` 的調控反應依團隊最終 proposal 轉化；具體構築尚未實測 |
| regulated promoter | `Pmer` | 受 MerR 狀態影響，不宣稱背景為零 |
| reporter gene／protein | `dTomato` reporter coding sequence／dTomato reporter protein | coding sequence 是 DNA 指令；protein 才產生需由讀取器觀察的紅色螢光訊號 |
| input condition | `Hg²⁺` in a sealed teaching model | 第一章只作封閉篩查概念，不是環境釋放或濃度證明 |

| ID | Speaker | Line |
|---|---|---|
| P-S02-D008 | 林博士 | 第一章會把同一種功能關係套到團隊的 `MerR/Pmer` 概念迴路。名稱變具體了，證據責任也會變得更重要。 |
| P-S02-D009 | 林博士 | 元件不是萬用積木。宿主、連接方式、背景、環境和量測都可能改變表現，所以設計之後一定要測試。 |

點亮「迴路」概念章。

## 12. S03：沒有對照就沒有答案

### Round Goal

玩家把三張 condition card 放入 Evidence Tray：已知應低、已知應高、未知。引導模式可自由執行任何組合並觀看後果；標準模式亦加入控制失敗診斷。

### 第一輪 canonical 模擬

| Condition | Expected Role | Simulated Output |
|---|---|---|
| Known expected-low | 檢查低背景 | Low／低於教學界線 |
| Known expected-high | 檢查系統能否產生較高輸出 | High／高於教學界線 |
| Unknown | 待判讀條件 | High／高於教學界線 |

第一輪開始時重設 `pre_current_controls_valid = false`。只有前兩張控制條件符合預期後才設定 `pre_current_controls_valid = true` 及 milestone `pre_controls_valid = true`。沒有控制仍可執行未知，但結果標記「本輪無法判斷測試是否正常」，且不載入 C001 結論卡；玩家要補足控制後才進入正式結論選擇。後續 failed-control run 只重設 current flag，不清除已完成 milestone。

### 結論選項

| ID | Choice Text | Result |
|---|---|---|
| P-S03-C001 | 本輪兩個控制條件符合預期；未知在這個教學模型中出現高於界線的篩查訊號，仍需合適方法確認。 | Correct；`pre_test_claim_valid = true` |
| P-S03-C002 | 未知訊號較高，所以已確認目標物身分、精確濃度及危險程度。 | Over-scope；訊號不能支持三項額外結論 |
| P-S03-C003 | 已知應高的控制正常，所以不需要已知應低的控制。 | Incomplete；不能檢查背景是否異常升高 |
| P-S03-C004 | 三張卡都亮過，代表這個迴路在任何細胞和環境都有效。 | Context error；本輪不能推廣到所有系統 |

引導模式第一輪同時顯示 C001 及一張輪替 near-miss（C002、C003 或 C004），每次只有兩張結論卡；標準模式顯示四張。任何 near-miss 都先播放缺少的 evidence／scope，再要求選擇有邊界結論；沒有 C001 不得進入 failed-control round。

| ID | 引導模式短句 |
|---|---|
| P-S03-C001P | 兩個對照都正常。未知有較高訊號：這是要再確認的線索。 |
| P-S03-C002P | 未知較高，所以我們已經知道它是甚麼和有多少。 |
| P-S03-C003P | 已知應高的卡正常，已知應低的卡可以拿走。 |
| P-S03-C004P | 這次正常，所以它在所有細胞和地方都一樣。 |

### 標準模式第二輪：控制失敗

教學模擬把 known expected-high 改成 Low，unknown 亦為 Low，並重設 `pre_current_controls_valid = false`；`pre_controls_valid` milestone 保留。

| ID | Choice Text | Result |
|---|---|---|
| P-S03-C005 | 未知是 Low，所以確認 input 不存在。 | Incorrect；系統本輪未證明能產生應有高輸出 |
| P-S03-C006 | 陽性控制未符合預期；本輪不能用未知 Low 排除 input，先調查測試系統。 | Correct；`pre_failed_control_diagnosed = true` |
| P-S03-C007 | 把判讀界線調低，直到陽性控制看起來通過。 | Incorrect；看到結果後移動規則不能修正測試 |

| ID | 引導模式短句 |
|---|---|
| P-S03-C005P | 未知沒有亮，所以 input 一定不存在。 |
| P-S03-C006P | 已知應亮的卡也沒亮。這次測試不能回答未知。 |

引導模式在第一輪後以短動畫示範「已知應高卻不亮」的後果，只顯示 C006 與一張 C005 圖像 near-miss。玩家選擇「這次測試不能回答」後才設定 `pre_failed_control_diagnosed = true`。

### 對白

| ID | Speaker | Line |
|---|---|---|
| P-S03-D001 | 林博士 | 未知結果不會自己告訴我們儀器、背景和迴路有沒有正常工作。控制條件就是這輪測試的檢查點。 |
| P-S03-D001P | 林博士 | 一張已知應低、一張已知應高。兩張都照預期，我們才知道這輪測試有沒有正常工作。 |
| P-S03-D002 | 訓練系統 | 控制條件有效；目前可支持「本教學條件下有高篩查訊號」，不能支持身分、濃度、安全或因果。 |
| P-S03-D003 | 林博士 | 好的測試不只產生結果，也告訴我們這個結果有資格走多遠。 |

點亮「證據」概念章。

## 13. S04：訊號不是保證

### Round Goal

方雅把第一章即將使用的「封閉感測概念」放到桌面。玩家從卡池組合三張公開說明：Use、Limit、Responsibility。卡牌可以先放錯，再按角色回復局部替換。引導模式固定顯示三張短句有效卡和一張輪替 invalid 圖像卡；標準模式顯示完整六張。

### 聲明卡

| ID | Category | Text | Valid／Issue |
|---|---|---|---|
| P-S04-C001 | Use | 封閉系統可在受測條件下提供可觀察的篩查訊號，協助決定下一步。 | Valid |
| P-S04-C002 | Limit | 訊號本身不證明樣本身分、濃度、安全、健康因果或污染已清除。 | Valid |
| P-S04-C003 | Responsibility | 工程生物材料保持封閉；包材、失效、廢物、確認、授權與通知仍要設計及審查。 | Valid |
| P-S04-C004 | Use | 只要控制通過，單一未知訊號便可直接代表整個城市狀況。 | Invalid scope；樣本與地理範圍不足 |
| P-S04-C005 | Limit | 裝置只要是封閉式，便不再有破損、處置或誤用風險。 | Invalid safety；封閉是控制，不是零風險 |
| P-S04-C006 | Responsibility | 為避免公眾誤解，所有限制和失敗只在研究站內保存。 | Invalid governance；隱藏限制破壞問責 |

| ID | 引導模式短句 |
|---|---|
| P-S04-C001P | 能做：在封閉盒中提供一個要再確認的線索。 |
| P-S04-C002P | 不能保證：訊號不等於安全，也不會清除問題。 |
| P-S04-C003P | 下一步：保持封閉，檢查盒子、廢物、確認和通知。 |
| P-S04-C004P | 一張未知卡有訊號，就代表整座城市。 |
| P-S04-C005P | 有盒子，所以風險已經是零。 |
| P-S04-C006P | 不告訴大家限制，便不會有人誤解。 |

### 對白

| ID | Speaker | Line |
|---|---|---|
| P-S04-D001 | 方雅 | 合成生物學設計要同時回答三件事：工具有甚麼用途、證據不能證明甚麼、出問題時由誰負責。 |
| P-S04-D001P | 方雅 | 一張說能做甚麼，一張說不能保證甚麼，一張說怎樣安全地繼續。 |
| P-S04-D002 | 方雅 | 封閉降低暴露，但盒子可能破、程序可能錯、結果可能被誤讀。安全要靠多個可以檢查的層次。 |
| P-S04-D003 | 林博士 | 這不是替技術寫廣告。把限制說清楚，才知道下一輪應測甚麼和應聽誰的意見。 |

玩家完成 C001+C002+C003，設定 `pre_scope_valid = true`，點亮「責任」概念章。

## 14. S05：第一個真實問題

### 完成畫面

桌面把玩家的操作整理成四枚不評分概念章：

| Stamp | Player-facing Summary |
|---|---|
| 指令 | DNA 指令、細胞和 protein output 是不同層次 |
| 迴路 | input 可透過 regulator 改變受控 reporter output |
| 證據 | 預測、對照和模型邊界決定結論可信範圍 |
| 責任 | 有效功能仍需要封閉、處置、確認、授權和溝通 |

### 可選反思

玩家可選一張「我現在會先問」卡，不設正誤，也不寫入能力評分：

| ID | Text |
|---|---|
| P-S05-C001 | 這張卡是 DNA 指令、環境 input，還是細胞輸出？ |
| P-S05-C002 | 沒有／有 input 時，我預期看見甚麼？ |
| P-S05-C003 | 哪些控制條件能告訴我這輪測試是否正常？ |
| P-S05-C004 | 這個訊號能支持甚麼，不能支持甚麼？ |

### 轉入第一章

研究站燈光由訓練白轉為低強度警示黃。卡牌收回桌面側邊，但「迴路、證據、責任」三個標籤保留在玩家 Evidence Notebook。遠處通訊器響起，不以倒數催促。

在播放事件內容前顯示並等待玩家確認：

| ID | Text |
|---|---|
| P-S05-UI001 | 下一章：《紅色警報》 |
| P-S05-UI002 | 下一章涉及環境污染及居民身體不適，不包含血腥畫面。這是教學故事，不是醫療、飲用水或實驗操作指引。 |
| P-S05-UI003 | 繼續 |

| ID | Speaker | Line | Direction |
|---|---|---|---|
| P-S05-D001 | 訓練系統 | 前導章完成。這代表你完成了概念模型，不代表已製造或核准任何真實生物系統。 | 固定顯示 |
| P-S05-D002 | 林博士 | 訓練桌給了我們乾淨的答案。真正的問題會有不完整資料、受影響的人和不能跳過的安全邊界。 | 收起卡牌 |
| P-S05-D003 | 周穎（通訊） | 河港部分區域暫停取水。公共衛生部門正在調查居民不適與疑似工業污染。 | 玩家確認內容提示後；取代第一章黑屏新聞句 |
| P-S05-D004 | 林博士 | 第一個真實問題來了。先看現場需要甚麼，不要因為剛學會一條迴路便把它當成所有答案。 | 轉入 Chapter 1 S00 compact settings confirmation |

完成時寫入 `p_prechapter_complete = true`、`p_prechapter_version = 1` 及 `p_prechapter_support = pre_support_level`。第一章沿用已選模式；若 `p_prechapter_support = demonstrated`，第一章 S03 初始顯示 role 輪廓，但不自動完成任何卡牌。

## 15. 全域錯誤與學習回復矩陣

| Misconception | Detection | Required Feedback | Later Reinforcement |
|---|---|---|---|
| DNA 直接變成 protein | 把 protein 放入 DNA 或跳過 RNA 動畫 | 分開 DNA、RNA、protein 三層，不說「DNA 變蛋白質」 | Chapter 2 生產鏈、Chapter 3 reporter |
| promoter 是 protein gene | 把 promoter 放到 Cell Output | 顯示 promoter 留在 DNA 並影響轉錄開始 | Chapter 3 Plac/operator、Chapter 4 promoter 表徵 |
| input 是 DNA 零件 | 把 input token 放入 DNA Rail | 用形狀與位置顯示 environment ≠ construct | Chapter 1 `Hg²⁺`、Final time／temperature input |
| reporter signal 就是 input | 選 C004 或把 output card放到 input port | 同時顯示 input icon 與 reporter output icon | Chapter 1 dTomato 不是汞 |
| OFF 等於絕對零 | 選 C002 | 顯示低背景與判讀界線，不加入虛構數值 | Chapters 1、3、4 |
| 一次結果就是證明 | 缺控制或選 C002 | 允許看結果，但把 conclusion badge 降為「無法判讀／篩查」 | Chapters 1、4、Final |
| 封閉等於零風險 | 選 C005 | 顯示破損、廢物、誤讀與授權四條剩餘路徑 | Chapters 1、5、Final |
| 元件可在任何情境直接複製 | 選 C004 或快速跳過限制 | 顯示 host／context／measurement 三個未驗證標籤 | Chapters 3、4、5 |

## 16. UI、視覺與聲音規格

### 16.1 卡牌尺寸與響應式限制

- 桌面卡牌使用固定 aspect ratio `5:7`，標準顯示寬度 112–144 px；不得因 hover、長術語或狀態 badge 改變版面尺寸。
- DNA Rail 使用兩行固定 grid；窄屏改為可切換 Rail A／B，不以水平縮小字體塞入同一列。
- 卡名最多兩行，正式術語不縮寫成無法辨識的單字；最小正文 16 CSS px，文字不按 viewport 寬度連續縮放。
- 可觀察輸出同時用圓形 icon、脈衝動畫、`LOW/HIGH` 文字及聲音，不只依賴綠／紅色。
- 卡牌正確 placement 使用短吸附動畫；錯誤使用輕微回彈，不震動整個畫面。

### 16.2 視覺語言

- DNA：有方向缺口的深色軌道；RNA：單線移動 token；protein：圓形折疊 icon。
- promoter、gene、terminator 使用不同輪廓；相同 role 在全遊戲保持形狀一致。
- 訓練輪不使用 `dTomato` 紅色作通用正確色；紅色只在 S02 橋接後代表具體 reporter 訊號或警示。
- 背景保持研究站功能空間，不用漂浮裝飾卡、漸層球或與科學無關的動效。

### 16.3 聲音

| Event | Sound | Accessibility Pair |
|---|---|---|
| Card selected | 短紙卡／數位 click | 2 px focus outline＋卡牌輕抬 |
| Valid role connection | 柔和雙音 | 插槽邊框轉為實線＋role icon |
| Invalid layer | 低音單響，不使用失敗警報 | 因果區高亮＋文字回復 |
| Reporter low／high | 相同音色、不同節奏 | LOW/HIGH 文字與靜止／脈衝形狀 |
| Chapter transition | 訓練音樂淡出、河港環境音淡入 | 背景明度及章名同步變化 |

## 17. 無障礙、閱讀與本地化

1. 所有卡牌為可 focus 的語義化按鈕；插槽有 role label、`aria-describedby` 及放置結果公告。
2. 拖曳不是唯一操作；switch、keyboard、touch 均可選卡再選槽位。
3. 提供「降低動態」：DNA→RNA→protein 動畫改成三張靜態連續圖，不失去因果資訊。
4. 提供「延長閱讀」與任意暫停；沒有自動關閉台詞。
5. 所有音效有可見替代，所有顏色有形狀及文字替代。
6. 引導模式可啟用語音讀卡；標準模式也可使用，不與難度綁定。
7. 英文術語與繁體中文名稱分開 authoring，不能把整句寫進圖片資產。
8. `Hg²⁺`、RNA、DNA 等符號需有 screen-reader label，例如「二價汞離子」。

## 18. 技術實作規格

### 18.1 建議架構

- 卡牌、插槽、對白及 evidence tray 使用 HTML/CSS DOM，確保文字縮放、鍵盤及 screen reader 支援。
- Three.js 只負責研究站背景、角色與 S05 轉場；前導章進行時可低更新率運行並在背景預載第一章河港資產。
- 卡牌規則由資料驅動 state machine 驗證 `role`、`zone`、`prerequisite` 及 `result`，不以顯示文字作判斷。
- 每次操作只寫 chapter-local state；達成 `pre_complete` 才原子寫入三個 profile fields。
- 離線快取必須包含全部卡牌文字、icon、語音替代及第一章入口，不依賴伺服器回傳答案。

### 18.2 State Machine

```text
MODE_READY
  → NEED_REVEALED
  → EXPRESSION_ASSEMBLED
  → CIRCUIT_ASSEMBLED
  → PREDICTIONS_CONFIRMED
  → CONTROLS_CONFIRMED
  → TEST_CLAIM_CONFIRMED
  → FAILED_CONTROL_DIAGNOSED
  → SCOPE_CONFIRMED
  → PRECHAPTER_COMPLETE
  → CHAPTER_1_S00
```

返回上一輪只清除該輪 run state，不清除已解鎖的術語與可查看動畫。頁面意外重新整理時從最近完成 scene 開始，不把半完成配置寫成完成。

### 18.3 Card Authoring Schema

```json
{
  "id": "PRE-CARD-005",
  "role": "reporter_gene",
  "validZones": ["dna_rail_b"],
  "formalLabelKey": "pre.card.reporterGene.label",
  "shortLabelKey": "pre.card.reporterGene.short",
  "descriptionKey": "pre.card.reporterGene.description",
  "shape": "dna_gene",
  "nextStateEffect": "reporter_expression_available"
}
```

本 schema 不保存真實序列、濃度或操作參數。

## 19. 教師與工作坊輸出

章末只輸出概念完成狀態，不輸出排名：

| Field | Meaning | Privacy Rule |
|---|---|---|
| 四枚 Concept Stamps | 玩家已完成對應互動 gate | 只存本機 profile |
| `pre_support_level` | 下一章由哪一級提示開始 | 不顯示為成績、不上傳 |
| 可選反思卡 | 玩家想帶入第一章的問題 | 預設不保存；教師模式可匿名統計 |
| Completion time | 灰盒及可用性測試 | 正式版預設不保存個人時間 |

教師一頁指南應提供：本章六項最低成果、DNA／protein 常見混淆、三條討論題、第一章橋接方式，以及「遊戲完成不等於實驗資格」聲明。

## 20. 灰盒驗收與 QA

### 20.1 必須通過

1. 首次零背景玩家中至少 80% 能在提示後正確區分 reporter gene 與 reporter protein；此數值是可用性目標，不是科學學習成效證明。
2. Critical Path 引導模式 5–6 分鐘、標準模式 6–7 分鐘，中位數待測；95% 玩家不超過 8 分鐘。
3. 玩家不能在未完成 Use＋Limit＋Responsibility 三卡時寫入 `p_prechapter_complete`。
4. 所有錯誤配置均有特定因果回復，沒有「錯了，再試一次」空白訊息。
5. 引導與標準模式得到相同的 canonical absent／present、control 及 scope 結論。
6. 玩家使用 keyboard、touch 或非拖曳操作均能完整通關。
7. 200% browser zoom、320 CSS px 寬度及長英文／繁體中文卡名不重疊、不裁切必要文字。
8. 降低動態模式仍能看懂 DNA→RNA→protein 及 input→regulator→output 因果。
9. 重新整理不會跳過未完成 gate，也不會清除已完成 scene checkpoint。
10. 完成後第一章沿用模式與無障礙設定；新聞句只播放一次。

### 20.2 科學與教育測試題

灰盒訪談不用要求背術語，以三個 transfer prompts 檢查理解：

1. 「這張 reporter protein 卡為甚麼不放進 DNA 軌道？」
2. 「未知樣本是 Low，但已知應 High 的控制也是 Low，你能說未知沒有 input 嗎？」
3. 「封閉感測器出現 High，還欠哪些資訊才可以作公共決定？」

若多數玩家只能重複卡牌位置，不能回答上述因果，代表 tutorial 只教會 UI 規則，必須重做動畫或回復文案。

## 21. 製作清單

| Discipline | Required Deliverable |
|---|---|
| Game Design | 卡牌 rule data、scene state machine、提示及 checkpoint 規格 |
| Narrative | 本文件主線、模式變體、錯誤回復及第一章無縫轉場 |
| Science | DNA→RNA→protein、regulator、背景、controls 及 MerR bridge 審核 |
| Education | 年齡語言、transfer prompts、教師指南及可用性研究 |
| UI/UX | 響應式卡桌、focus order、非拖曳操作及 200% zoom |
| 2D Art | 15 張核心卡、role shapes、四枚 Concept Stamps、狀態 icon |
| 3D Art | 輕量研究站背景、林博士 idle、S05 河港轉場 |
| Audio | 卡牌狀態音、環境 loop、字幕時間與可選語音 |
| Engineering | DOM card engine、save schema、loader、offline cache、Three.js preload |
| QA | 科學因果、雙模式、輸入方式、localization、reload 及 transition matrix |

## 22. 待正式核准項目

- 團隊 Science Lead 確認第一章 bridge 對 `MerR/Pmer` 團隊最終 proposal 及尚未實測狀態的表述。
- Education Lead 與中一或以上 Story Campaign 目標玩家完成理解與閱讀測試；小四至小六測試由 Junior Mission 獨立執行。
- Accessibility reviewer 驗證 keyboard、screen reader、zoom、色覺及降低動態流程。
- Safety／Human Practices reviewers 確認封閉、篩查與公共責任文案不造成錯誤保證。
- Technical Lead 以目標學校設備驗證 DOM 卡牌與 Three.js 預載不造成記憶或載入問題。

---

## 核准

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Lead Game Designer |  |  |  |  |
| Narrative Designer |  |  |  |  |
| Science Lead |  |  |  |  |
| Education Lead |  |  |  |  |
| Safety / Human Practices Lead |  |  |  |  |
| Accessibility Reviewer |  |  |  |  |
| Technical / QA Lead |  |  |  |  |
