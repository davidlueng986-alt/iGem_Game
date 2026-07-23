# 《微界工程師：生命迴路》腳本系統與跨章連續性規格

> Script Bible Supplement｜版本 1.0｜對應 GCP 1.1

## 1. 適用範圍

本文件是 `07_CHAPTER_01_FULL_SCRIPT.md` 至 `14_FINAL_CHAPTER_FULL_SCRIPT.md` 的共用契約。各章腳本負責場景與內容；本文件負責模式載入、3D 體驗最低要求、跨章狀態、獨立遊玩預設和來源成熟度。草稿階段若有衝突，共用狀態與載入規則以本文件為準，章內場景與文案以對應章節腳本為準；未能依此消解的差異必須記入審核紀錄，不得自行猜測。正式簽核後，以最新 GDD 決策紀錄及其引用的簽核版本為準。

## 2. 遊玩結構

| 模式 | 規則 |
|---|---|
| 完整故事 | 建議依第一至七章、終章順序遊玩；決策保存並在後章形成可見結果 |
| 工作坊單章 | 第一至七章可獨立遊玩；載入中性前情與章內所需能力教學 |
| 終章 | 建議完成前七章後進入；亦可用「導師模式」載入中性決策摘要 |
| 展覽重設 | 清除 chapter scope，不刪除全域設定；可由工作人員重設 profile summary |

完整故事 Critical Path 約 186–195 分鐘，應分多次遊玩。每章仍維持 15–30 分鐘的工作坊單元。

## 3. Chapter Loader

每次載入章節前均顯示：

1. 「小學模式：更多圖像、短句及逐步提示」。
2. 「標準模式」。
3. 字幕、文字大小、鏡頭、降低動態和控制設定。
4. 「沿用上章模式」只作預設，玩家可更改；不影響已完成決策。

`mode_primary` 儲存在 profile。切換模式只改變文字、卡片數、資料複雜度和提示，不改變 canonical 科學因果、故事結果或可取得章節。

| Shared Flag | Type／Default | Scope／Reset | 用途 |
|---|---|---|---|
| `mode_primary` | bool／false | profile／手動改模式 | 小學模式內容層 |
| `standalone_default` | bool／false | chapter load／離開章節重設 | 標記工作坊單章或導師模式使用中性前情，不偽造歷史決策 |

各章簡表中的完成條件若未另標型別，預設為 `bool／false`；列出固定候選值的決策預設為 `enum／unset`。兩者均屬 chapter scope，重玩重設，並只在章節完成時依下表序列化為 profile summary。

## 4. 小學模式實作矩陣

| 章節 | 必要卡片／資料上限 | 必要主句 | 回復方式 |
|---|---:|---|---|
| 1. 紅色警報 | 迴路分兩組、2 對照、4 公共圖卡 | 感測、確認、清理是三件事 | 三級提示；錯誤先播因果 |
| 2. 細胞工廠 | 5 生產卡、4 品質圖示、3 聲明卡 | 細胞是工廠，不是藥瓶 | 沿輸送線找錯路，不讀品質術語表 |
| 3. 壞掉的開關 | 4 元件、3 狀態、2 修復卡 | 沒輸入低、有輸入高、之後回低 | 光點路徑指向故障位置 |
| 4. 數據迷霧 | 每組 5 點、3 對照圖卡 | 一個點是發生過，多個點才看通常怎樣 | 先顯示所有點，再顯示平均 |
| 5. 離開實驗室之前 | 3 材料類、4 風險節點、2 封閉方案 | 實驗室有效不等於可倒進環境 | 先播放路徑後果，再命名原則 |
| 6. 誰能得到成果 | 2 來源、3 衝擊、3 公平指標 | 多一條來源不會自動令所有人得到 | 角色以地圖動畫說明缺貨與生計 |
| 7. 雙面設計 | 3 申請、4 風險問題、5 事件步驟 | 不同能力需要不同開放方式 | 以門和權限圖示，不顯示制度長句 |
| 終章 | 4 需求卡、5 狀態測試、5 最終卡 | 熱度和時間觸發後，提示不能被降溫擦掉 | 模擬物流箱重播；可選 no-pilot |

### 第六章小學主句

| 節點 | 主句 |
|---|---|
| 兩條來源 | 植物和工程酵母都只是完整供應鏈的一部分。 |
| 供應衝擊 | 只靠一條路，那條路中斷便沒有備援。 |
| 公平 | 價格低但沒有貨，仍然拿不到。 |
| 轉型 | 新技術前進時，要讓受影響的人有時間和選擇。 |

### 第七章小學主句

| 節點 | 主句 |
|---|---|
| 風險 | 先問做甚麼、誰使用、在哪裡、有哪些保護。 |
| 教材 | 低風險教材可以公開，也要附安全和限制。 |
| 合作 | 科學資料盡量公開；個人或設施資料先妥善處理。 |
| 未知申請 | 資料不足時先暫停和查證，不代表先定罪。 |
| 事件 | 先停下異常、留下紀錄、通知、查證，再決定。 |

## 5. 3D 體驗最低要求

| 章節 | 可步行空間 | 核心空間動詞 | 不可全部替換成 UI 的節點 |
|---|---|---|---|
| 1 | 河港、研究站、議會 | 調查、追蹤水流、走入安全剖面 | 四個候選位置、裝置失效 |
| 2 | 生產觀察走廊 | 拉隔離桿、沿輸送線追偏差、改路由 | 批次隔離與根本原因 |
| 3 | 細胞城 | 跟隨 mRNA／reporter 光點、修閘門 | 兩個故障位置 |
| 4 | 資料劇場 | 走到原始點查紀錄、配置實體槽位 | 異常值與批次位置 |
| 5 | 回收設施與管廊 | 追蹤細胞／酵素／廢物流、改反應器路線 | 暴露路徑與封閉方案 |
| 6 | 世界供應網 | 搬運供應 token、開關來源、配置 buffer | 三場衝擊與偏遠配送 |
| 7 | 存取中心 | 分流申請、關閉佇列、封存 audit log | 異常下載事件 |
| 終章 | 食物銀行物流線 | 跟隨模擬箱、比較基準、回收標籤 | 基準比較、鎖存測試、pilot gate |

每章 Critical Path 至少 40% 時間在角色移動、空間觀察或直接操作世界物件；對話卡和表格可作輔助，不得成為唯一玩法。

## 6. 跨章持久化契約

| Profile Summary | Source Flag(s) | Type／Serialized Values | Later Consumer |
|---|---|---|---|
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

## 7. 來源成熟度

| 章節 | 分類 | 對外表述 |
|---|---|---|
| 1 | 團隊概念 | 迴路來自團隊 PDF；效能與正式菌株待實測／核准 |
| 2 | 成熟實例 | 重組人類胰島素是成熟案例；遊戲工廠和批次虛構 |
| 3 | 經典教學模型 | LacI／Plac 與 GFP 是教學抽象；不等於具體產品 |
| 4 | 通用方法 | 所有數據虛構，只教授研究設計與報告原則 |
| 5 | 新興技術 | PET 酵素回收具潛力與工業進展；遊戲方案未獲部署驗證 |
| 6 | 歷史成熟案例 | 半合成青蒿素曾工業化；2026 實際供應角色需當期查核 |
| 7 | 虛構平台 | 案例抽象，不含可執行高風險內容 |
| 終章 | 虛構教學概念 | cell-free 標籤未驗證；no-pilot 是合法結果 |

## 8. 正式簽核狀態

全部腳本目前是**編輯自審後的灰盒候選**，不是正式科學、法規、醫療、食品或安全核准內容。每章核准表完成前，對外版本必須保留成熟度與限制標示。
