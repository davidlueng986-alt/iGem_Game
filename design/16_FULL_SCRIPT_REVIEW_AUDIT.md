# 《微界工程師：生命迴路》全腳本再審核

> Full Script Review Audit｜版本 2.0｜審核日期 2026-07-27｜對應 GCP 1.4／GDD 2.0／TDD 2.0｜狀態：**文件邏輯修正完成；科學、教育、安全、裝置與真人測試簽核未完成**

## 1. 審核範圍與方法

本輪逐檔核對 `00_GAME_CONCEPT_PROPOSAL.md`、前導章、第一至第八章、Junior Mission、`15_SCRIPT_SYSTEM_AND_CONTINUITY.md`、GDD、TDD、來源／Claim Register 及團隊汞感測 PDF。方法包括：

- scene 流程、entry／exit、flag set／use、profile write 與 standalone default 交叉檢查；
- 章節時間加總、玩家權限、角色同意、release／pilot gate 與失敗回復的常識檢查；
- 固定斜俯視鏡頭、3D 空間行動、DOM 工作台與可及性契約一致性檢查；
- 科學用語、來源成熟度、教學模擬、未驗證 proposal 及禁止公開宣稱分層；
- Future 內容與 2026 P0 production manifest／bundle／QA surface 的隔離檢查。

## 2. 先前 v1.2 結論已被取代

v1.2 曾把 Blocker／High／Medium 全部判為 0。這個結論過度樂觀，因為它未發現或未完整處理：

1. 同一產品同時出現肩後／自由鏡頭與固定斜俯視意圖；
2. 完整主線上限寫成 202 分鐘，但逐章加總為 203 分鐘；
3. Junior 原以固定的百分比移動時數作 3D 合格標準，屬任意數字而非學習證據；
4. GDD／TDD C2–C8 使用多個不存在於 canonical scripts 的 flag，會令內容資料與程式契約分叉；
5. C3 把移除輸入後的新 reporter 表達寫成絕對「先停止」，忽略轉錄／翻譯與讀值反應窗；
6. C4 未把 controls、replication、follow-up、outlier 和 data package 的獨立旗標完整對齊；
7. C6 腳本定義 `c6_chain_valid`，但 S01 沒有 set event，會造成 S02 gate 永遠不能可靠驗證；
8. C8 曾出現多餘 problem-context flag，且須明示 `D` 為由連續 `T` 派生、no-pilot 為合法成功；
9. WebGL2 fallback 文案暗示已有等價 2D 遊戲，但文件並沒有設計或預算支持；
10. TDD／Decision Register 對技術 stack 的「已鎖定／仍 Proposed」表述互相矛盾。

因此 v1.2 只保留作歷史紀錄；本文件與 `24_LOGIC_CAMERA_AND_CHAPTER_2_8_AUDIT.md` 為最新審核。

## 3. 修正結果

| ID | 原問題 | 影響 | 已採修正 | 狀態 |
|---|---|---|---|---|
| SCR-001 | 自由／肩後鏡頭與斜俯視意圖衝突 | 關卡、美術、輸入、可及性與 QA 全部倍增 | 統一 `IsometricPerspectiveRig`：固定 yaw／pitch／FOV，隨位置平移、不跟隨面向；無玩家 camera input | 已修正 |
| SCR-002 | 原文件所列總時長上限比逐章加總少 1 分鐘 | 時數與範圍估算不可信 | 統一為 192–203 分鐘，並維持 Future 非 P0 | 已修正 |
| SCR-003 | Junior 40% 移動時間配額 | 可鼓勵無意義走路填時 | 改為每個核心 learning gate 必須有可觀察空間／因果操作，並以目標玩家 transfer 測試決定是否保留 3D | 已修正 |
| SCR-004 | C2 invented flags | content／runtime 不能對接 | 對齊 `c2_cells_product_separated`、`c2_process_order_valid`、四品質 flags、批次／root cause／statement／access 及 profile writes | 已修正 |
| SCR-005 | C3 invented flags／絕對停止 | 科學誤導及 state mismatch | 對齊 expected behavior、兩故障、repair、truth table、failure reported；改為輸出開始下降並依反應窗回低 | 已修正 |
| SCR-006 | C4 flags 不完整 | controls／replication／outlier／package gate 可能互相替代 | 對齊九個 canonical states；全部 raw points 可由總覽存取，不強迫逐點步行 | 已修正 |
| SCR-007 | C5 overclaim／pathway flags 命名分叉 | 安全與內容驗證失效 | 對齊 release rejected、claim scope、pathways、contained strategy、maturity、lifecycle、public statement | 已修正 |
| SCR-008 | C6 S01 未 set `c6_chain_valid`；entity 名稱含糊 | 章節鎖死或 precursor／drug 混淆 | S01 完成兩鏈後明確 set；schema 用 `artemisinic_acid_precursor`、`artemisinin`、`derivative`、`ACT_product` | 已修正 |
| SCR-009 | C7 case loader 被寫成 invented flag | canonical script 與 TDD 分叉 | S00 為 fixture input，不 set flag；S01–S06 對齊風險、三案例、controls、incident、public summary | 已修正 |
| SCR-010 | C8 多餘 context flag與時間狀態風險 | gate 不一致；tab／pause 可能錯誤累加時間 | S00 直接 set problem statement；D 由 T 連續時間派生；用 monotonic simulation step；no-pilot 合法 | 已修正 |
| SCR-011 | WebGL2 fallback 誇大 | 使用者可能以為有完整 2D 版 | 改為明確不支援提示＋來源／逐字稿／靜態摘要／預錄 walkthrough 或受控展示 | 已修正 |
| SCR-012 | stack 狀態矛盾 | agent 可能自行換框架或 dependency | Decision Register 新增 `Baseline v2.0`：實作不可任意更換，但仍待具名 Owner 簽核 | 已修正 |

## 4. 逐章再審結論

| 章節 | 文件邏輯 | 仍待正式核准／測試 |
|---|---|---|
| PRE | 因果卡、control failure、claim limit 與 C1 bridge 一致 | 零背景玩家理解、200% zoom、鍵盤／觸控等價、MerR wording |
| C1 | 感測／確認／清理、居民修訂、多層安全與權責一致 | 團隊 construct、宿主、效能、Science／Safety／HP 簽核；真機效能與目標玩家 misconception test |
| C2 | 生產、品質、批次、供應與獨立放行鏈一致 | 醫療／品質／法規專家；四分類只能作教學框架 |
| C3 | 診斷、repair、時間趨勢與公開失敗一致 | 特定構築／reporter 反應窗不可由遊戲虛構外推 |
| C4 | 研究問題、controls、replication、追加、outlier、claim、package 分開 | 教育資料量、圖表可讀性、統計與科學方法 reviewer |
| C5 | PET 材料範圍、暴露、封閉與成熟度一致 | PET 專家、LCA／TEA、biosafety、地方受影響者 review |
| C6 | precursor→artemisinin→derivative／ACT、供應衝擊及合作社同意一致 | 2026 市場角色、公共健康／供應鏈／合作社代表重新查核 |
| C7 | 能力／用途／控制與程序公平一致；身份不作 proxy | Security／Safety／Privacy／公平 reviewer；高後果案例保持抽象 |
| C8 | 共同定義問題、衍生連續時間、controls、edge cases、quality、access、no-pilot／pilot 一致 | Food safety、cell-free、packaging、HP、accessibility 與 pilot governance review |
| Junior | 每個 learning gate 有不可被對話取代的操作 | 9–12 歲獨立樣本、教師／ safeguarding、3D 是否真的帶來 transfer |

## 5. 最終裁決

修正後，**未發現仍開放的文件結構或跨章狀態 Blocker**；GDD／TDD 已可用來建立 Future backlog，不會因未寫 C2–C8 而遺失設計方向。但這不代表第二至第八章已準備進 production，也不代表任何科學或產品宣稱已核准。

2026 P0 仍只有 PRE＋C1＋Expo。以下項目在正式公開前仍是必要外部 gate：具名 Science／Safety／HP／Education／Privacy／Accessibility 簽核、三台學校裝置效能、目標玩家 playtest、資產授權、browser／offline／rollback 測試，以及 iGEM 當期交付要求確認。
