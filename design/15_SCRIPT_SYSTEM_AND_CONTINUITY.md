# 《微界工程師：生命迴路》腳本系統與跨章連續性規格

> Script Bible Supplement｜版本 1.3｜對應 GCP 1.4／GDD 2.0

## 1. 適用範圍

本文件是 `17_JUNIOR_MISSION_FULL_SCRIPT.md`、`07A_PRE_CHAPTER_FULL_SCRIPT.md`、`07_CHAPTER_01_FULL_SCRIPT.md` 至 `14_FINAL_CHAPTER_FULL_SCRIPT.md` 的共用契約。各腳本負責場景與內容；本文件負責產品路由、模式載入、2D 前導例外、核心玩法語法、3D 體驗最低要求、跨章狀態、獨立遊玩預設和來源成熟度。草稿階段若有衝突，共用狀態與載入規則以本文件為準，章內場景與文案以對應腳本為準；未能依此消解的差異必須記入審核紀錄，不得自行猜測。正式簽核後，以最新 GDD 決策紀錄及其引用的簽核版本為準。

## 2. 遊玩結構

| 模式 | 規則 |
|---|---|
| Junior Mission | 小四至小六的獨立 18–22 分鐘任務；共用世界、角色及 MerR 案例，但不載入或完成主線 gate |
| 完整故事 | 新 profile 先完成前導章，再依第一至七章、終章順序遊玩；決策保存並在後章形成可見結果 |
| 前導章 | 首次完整故事必須完成一次；完成後可重玩或直接開始第一章，不作能力分數 |
| 工作坊單章 | 第一至七章可獨立遊玩；第一章在未完成前導時載入 90 秒核心三題版，或由導師在工作坊／展覽 preset 逐裝置確認已參與全班示範並設定 session flag；其他章載入中性前情與章內所需能力教學 |
| 第八章（終章） | 建議完成前七章後進入；亦可用「導師模式」載入中性決策摘要 |
| 展覽重設 | 清除 chapter scope，不刪除全域設定；可由工作人員重設 profile summary |

Junior Mission Critical Path 約 18–22 分鐘。完整故事 Critical Path 約 192–203 分鐘，應分多次遊玩；前導章為 5–7 分鐘，每個主章維持 15–30 分鐘的工作坊單元。兩條路線的完成率、學習證據及適齡性分開驗證。

## 3. Chapter Loader

產品首頁先選擇 Junior Mission 或 Story Campaign。Junior Mission 直接載入固定腳本及無障礙設定，不顯示引導／標準模式；Story Campaign 新 profile 在前導章前顯示一次完整模式與無障礙設定，後續每次載入主章前均可確認或更改：

1. 「引導模式：更多圖像、短句及逐步提示」。
2. 「標準模式」。
3. 字幕、文字大小、降低動態、移動預視開關和控制設定；固定鏡頭角度不可旋轉。
4. 「沿用上章模式」只作預設，玩家可更改；不影響已完成決策。

`mode_primary` 是既有內部 schema 識別碼，玩家介面及對外文件不得解讀成「小學資格」；`true` 代表引導模式。切換模式只改變文字、卡片數、資料複雜度和提示，不改變 canonical 科學因果、故事結果或可取得章節。

| Shared Flag | Type／Default | Scope／Reset | 用途 |
|---|---|---|---|
| `mode_primary` | bool／false | profile／手動改模式 | 引導模式內容層 |
| `junior_campaign_active` | bool／false | session／離開 Junior 重設 | 將 route 與主線 profile 分開 |
| `p_junior_complete` | bool／false | profile／工作人員明確重設 | Junior 完成章及可選知識卡；不解鎖主線 gate |
| `standalone_default` | bool／false | chapter load／離開章節重設 | 標記工作坊單章或導師模式使用中性前情，不偽造歷史決策 |
| `p_prechapter_complete` | bool／false | profile／工作人員明確重設 | 前導首次 gate、重玩與第一章 standalone 壓縮版 |
| `p_prechapter_version` | int／0 | profile／內容 migration | 判斷重大前導更新後是否需要重溫 |
| `p_prechapter_support` | enum／`independent` | profile／完整重玩更新 | `independent`／`hinted`／`demonstrated`；只調整第一章提示起點 |
| `pre_quick_primer_seen` | bool／false | session／離開第一章重設 | 防止未完成完整前導的 Chapter 1 standalone 反覆呼叫核心三題版 |

各章簡表中的完成條件若未另標型別，預設為 `bool／false`；列出固定候選值的決策預設為 `enum／unset`。兩者均屬 chapter scope，重玩重設，並只在章節完成時依下表序列化為 profile summary。

## 4. 引導模式實作矩陣

本節是 Story Campaign 的可及性／支架矩陣，不是小學課程清單。引導模式可由任何年齡選用；它沒有把八章時長、議題及學習負荷驗證為小四至小六適用。小學路線只以 `17_JUNIOR_MISSION_FULL_SCRIPT.md` 為 canonical 腳本。

| 章節 | 必要卡片／資料上限 | 必要主句 | 回復方式 |
|---|---:|---|---|
| 前導章 | 兩條 role 軌道、3 condition cards、3 statement cards | DNA 指令、細胞輸出、測試證據與責任是不同層次 | role 輪廓、因果動畫、三級提示；不計分 |
| 1. 紅色警報 | 迴路分兩組、2 對照、4 公共圖卡 | 感測、確認、清理是三件事 | 三級提示；錯誤先播因果 |
| 2. 細胞工廠 | 5 生產卡、4 品質圖示、3 聲明卡 | 細胞是工廠，不是藥瓶 | 沿輸送線找錯路，不讀品質術語表 |
| 3. 壞掉的開關 | 4 元件、3 狀態、2 修復卡 | 沒輸入低、有輸入高、之後回低 | 光點路徑指向故障位置 |
| 4. 數據迷霧 | 每組 5 點、3 對照圖卡 | 一個點是發生過，多個點才看通常怎樣 | 先顯示所有點，再顯示平均 |
| 5. 離開實驗室之前 | 3 材料類、4 風險節點、2 封閉方案 | 實驗室有效不等於可倒進環境 | 先播放路徑後果，再命名原則 |
| 6. 誰能得到成果 | 2 來源、3 衝擊、3 公平指標 | 多一條來源不會自動令所有人得到 | 角色以地圖動畫說明缺貨與生計 |
| 7. 雙面設計 | 3 申請、4 風險問題、5 事件步驟 | 不同能力需要不同開放方式 | 以門和權限圖示，不顯示制度長句 |
| 第八章（終章） | 4 需求卡、5 狀態測試、5 最終卡 | 熱度和時間觸發後，提示不能被降溫擦掉 | 模擬物流箱重播；可選 no-pilot |

### 第六章引導主句

| 節點 | 主句 |
|---|---|
| 兩條來源 | 植物和工程酵母都只是完整供應鏈的一部分。 |
| 供應衝擊 | 只靠一條路，那條路中斷便沒有備援。 |
| 公平 | 價格低但沒有貨，仍然拿不到。 |
| 轉型 | 新技術前進時，要讓受影響的人有時間和選擇。 |

### 第七章引導主句

| 節點 | 主句 |
|---|---|
| 風險 | 先問做甚麼、誰使用、在哪裡、有哪些保護。 |
| 教材 | 低風險教材可以公開，也要附安全和限制。 |
| 合作 | 科學資料盡量公開；個人或設施資料先妥善處理。 |
| 未知申請 | 資料不足時先暫停和查證，不代表先定罪。 |
| 事件 | 先停下異常、留下紀錄、通知、查證，再決定。 |

## 5. Evidence → Claim → Consequence 共用契約

每個主題節點必須留下三個可追查物件：

| Object | 最低 schema | 實作要求 |
|---|---|---|
| Evidence | `source`、`quality`、`scope`、`uncertainty` | 由玩家操作取得或整理；不能只由 NPC 朗讀後自動加入 |
| Claim | `statement`、`strength`、`applies_to`、`next_action`、`responsible_actor` | 至少一個 near-miss 只缺範圍、對照、權責或持份者其中一項 |
| Consequence | `trigger_claim_id`、`world_effect`、`recovery` | 顯示具體科學、營運、安全、社會或資源後果，並提供可理解的修訂路徑 |

共同規則：

1. 選擇 near-miss 後先播放因果，再容許玩家查看證據及局部換卡；不可只顯示紅叉。
2. 可逆修訂不等於後果消失。任務簿可保留延誤、更正或額外監測，但不以羞辱或永久鎖死懲罰學習。
3. 合理分支可以有不同取捨；只有違反 canonical 科學因果、安全底線或必要證據的主張才阻止 gate。
4. 章末報告分開顯示 evidence、design、responsibility 及 communication，不壓成一個「正確人格」總分。
5. Junior Mission 使用相同語法但較少證據種類；引導模式只減少資料量及文字，不刪除 Claim scope 或 Consequence。

## 6. 3D 體驗最低要求

所有 3D 路線使用 GDD／TDD 定義的固定斜俯視透視鏡頭：方向與角度不隨角色旋轉，只平移取景；沒有自由鏡頭、肩後追尾或玩家 zoom。關卡須用 cutaway／occluder fade 保持必要物件可見。

| 章節 | 可步行空間 | 核心空間動詞 | 不可全部替換成 UI 的節點 |
|---|---|---|---|
| Junior Mission | 河港步道、研究站、3D 水流圖、裝置剖面 | 走訪、放置、比較、沿水流追查、關閉安全層 | A–D 空間關係、DNA／environment／output、failed control、封閉失效 |
| 前導章 | 2D 卡牌桌；Three.js 研究站只作背景 | 放置、預測、比較、限定聲明 | DNA／cell／environment 空間層級與 control failure |
| 1 | 河港、研究站、議會 | 調查、追蹤水流、走入安全剖面 | 四個候選位置、裝置失效 |
| 2 | 生產觀察走廊 | 拉隔離桿、沿輸送線追偏差、改路由 | 批次隔離與根本原因 |
| 3 | 細胞城 | 跟隨 mRNA／reporter 光點、修閘門 | 兩個故障位置 |
| 4 | 資料劇場 | 從總覽選取原始點、按需要走到批次室、配置實體槽位 | 異常值、批次來源與預先規則 |
| 5 | 回收設施與管廊 | 追蹤細胞／酵素／廢物流、改反應器路線 | 暴露路徑與封閉方案 |
| 6 | 世界供應網 | 搬運供應 token、開關來源、配置 buffer | 三場衝擊與偏遠配送 |
| 7 | 存取中心 | 分流申請、關閉佇列、封存 audit log | 異常下載事件 |
| 第八章（終章） | 食物銀行物流線 | 跟隨模擬箱、比較基準、回收標籤 | 基準比較、鎖存測試、pilot gate |

前導章是刻意設計的 2D 基礎教學例外；Critical Path 應以放置、預測、執行或修正為主，而不是長篇讀取。Junior Mission 及第一至第八章必須保留**有意義的空間因果**，例如比較水流、隔離批次、追蹤故障、檢查生命週期或供應節點；不設任意「40% 走路」配額，也不以強迫逐點步行填充時長。每個 Scene 是否需要 3D，依下列問題判定：

1. 空間關係是否本身是要學習／推理的 evidence？
2. 世界互動是否產生可見後果，而非只把 UI 按鈕放遠？
3. 固定斜俯視下是否清楚、可鍵盤完成、可由 interaction list 替代搜尋？
4. 若答案皆否，該步驟應改為 DOM／對話，而不是保留無意義移動。

## 7. 跨章持久化契約

| Profile Summary | Source Flag(s) | Type／Serialized Values | Later Consumer |
|---|---|---|---|
| `p_junior_complete` | `j_statement_valid` AND `j_transfer_valid` | bool：`true` | Junior 完成章、研究總部可選知識卡；無主線 consumer |
| `p_prechapter_complete`／`p_prechapter_version`／`p_prechapter_support` | `pre_complete`／script schema／`pre_support_level` | bool：`true`；int：`1`；enum：`independent`／`hinted`／`demonstrated` | 第一章 loader、S03 初始提示及研究總部重玩 |
| `p_c1_monitoring` | `monitoring_architecture` | enum：`fixed`／`portable` | 終章 S06 包材與追蹤提示、Credits |
| `p_c1_reporting` | `public_report_mode` | enum：`dashboard`／`direct` | 終章 S00 社區報告介面 |
| `p_c2_batch` | `c2_batch_decision` | enum：`validated_rework`／`reject_restart` | Credits 的資源與時間結果 |
| `p_c2_access` | `c2_access_plan` | enum：`redundant_supply`／`public_partnership` | 終章 S00 取得方案提示 |
| `p_c3_repair` | `c3_repair_strategy` | enum：`restore_laci`／`replace_module` | 第四章 S02 資料條件、Credits 展品狀態 |
| `p_c4_question` | `c4_question` | enum：`mean_output`／`robustness` | 終章 S05 圖表預設，但可切換 |
| `p_c5_containment` | `c5_contained_strategy` | enum：`enzyme_only`／`closed_whole_cell` | 終章 S00 生命週期提示、Credits 設施模型 |
| `p_c5_pilot` | `c5_lifecycle_choice` | enum：`local_pilot`／`shared_facility` | 終章 S08 pilot 治理提示 |
| `p_c6_supply` | `c6_strategy` | enum：`dual_source_buffer`／`regional_partnership` | 終章 S00 分發方案提示 |
| `p_c6_transition` | `c6_transition_plan` | enum：`notice_transition_purchase`／`notice_new_roles` | Credits 農場／供應節點 |
| `p_c7_access` | `c7_case_education`、`c7_case_environment`、`c7_case_unverified` | object：`{ education: open, environment: controlled_collaboration, unverified: hold_escalate }` | 終章 S00 公開資料包預設 |
| `p_final_architecture` | `f_solution_architecture` | enum：`workflow_baseline`／`cell_free_hybrid` | Credits 最終物流世界狀態 |
| `p_final_access` | `f_access_choice` | enum：`shared_kiosk`／`distributed_kits` | Credits 最終取得與支援節點 |

### 寫入與重玩

- Junior 完成只寫 `p_junior_complete`；不得設定 `p_prechapter_complete`、Chapter 1 flags 或任何 `p_c*` summary。
- Junior 重玩在完成前不覆寫既有狀態；它可重設 mission scope，但保留主線 profile。
- 新 profile 的完整故事在 `p_prechapter_complete = true` 前不得進入 Chapter 1；第一章 standalone 只要求 session `pre_quick_primer_seen = true`，不偽造完整完成。
- `p_prechapter_version` 低於目前版本時載入 90 秒核心重溫並只更新 version；完整重玩確認完成後才原子更新 complete、version、support，未完成重玩保留舊值。
- 章節完成時才把 chapter flags 轉成 profile summary。
- 重玩未完成不覆寫既有 summary；新結局確認後詢問是否更新。
- 沒有已完成章節時不寫入對應 summary；Standalone mode 使用章內中性提示並標記 `standalone_default = true`，不偽造玩家曾作決策。
- Profile summary 只改變可見場景、提示和回顧，不使某條路線成為唯一正確路線。

### 終章條件支援

終章 S00 可載入最多三個前章口述回響，避免所有角色同時朗讀歷史：

1. 依 `p_c1_reporting` 顯示公告方式。
2. 依 `p_c2_access` 或 `p_c6_supply` 提供取得方案提示。
3. 依 `p_c5_containment` 或 `p_c7_access` 提供生命週期／資料分級提示。

其他 summary 仍可在指定場景成為非口述的介面預設或 Credits 展品：`p_c1_monitoring` 用於 S06、`p_c4_question` 用於 S05、`p_c5_pilot` 用於 S08、`p_c6_transition` 用於 Credits。沒有 summary 時，由對應角色提供中性教學句，不影響通關。

## 8. 來源成熟度

| 章節 | 分類 | 對外表述 |
|---|---|---|
| Junior Mission | 團隊 proposal 的教學情境 | MerR 機制有文獻基礎；團隊兩單元設計尚未實測；讀值及封閉示範均為教學虛構 |
| 前導章 | 通用入門模型 | DNA、expression、regulation 與 controls 為教學抽象；不等於實驗資格或可執行構築 |
| 1 | 團隊最終 proposal | MerR 機制有文獻基礎；團隊兩單元設計尚未實測；遊戲既有原型是敘事前提，不是團隊成果 |
| 2 | 成熟實例 | 重組人類胰島素是成熟案例；遊戲工廠和批次虛構 |
| 3 | 經典教學模型 | LacI／Plac 與 GFP 是教學抽象；不等於具體產品 |
| 4 | 通用方法 | 所有數據虛構，只教授研究設計與報告原則 |
| 5 | 新興技術 | PET 酵素回收具潛力與工業進展；遊戲方案未獲部署驗證 |
| 6 | 歷史成熟案例 | 半合成青蒿素曾工業化；2026 實際供應角色需當期查核 |
| 7 | 虛構平台 | 案例抽象，不含可執行高風險內容 |
| 第八章（終章） | 虛構教學概念 | cell-free 標籤未驗證；no-pilot 是合法結果 |

## 9. 正式簽核狀態

Junior Mission、前導章至終章全部腳本目前是**編輯自審後的灰盒候選**，不是正式科學、教育成效、法規、醫療、食品或安全核准內容。每章核准表完成前，對外版本必須保留成熟度與限制標示。
