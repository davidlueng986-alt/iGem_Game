# 《微界工程師：生命迴路》全腳本最終審核紀錄

> Full Script Review Audit｜版本 1.0｜審核日期 2026-07-22｜對應 GCP 1.1

## 1. 審核範圍

本輪審核涵蓋：

- `00_GAME_CONCEPT_PROPOSAL.md`
- `07_CHAPTER_01_FULL_SCRIPT.md` 至 `14_FINAL_CHAPTER_FULL_SCRIPT.md`
- `15_SCRIPT_SYSTEM_AND_CONTINUITY.md`

審核面向包括科學因果、安全與資訊危害、敘事與教學選項、跨章持久化、standalone 行為、Markdown 結構、ID 唯一性、相對連結及狀態序列化。

## 2. 結論

| Severity | Open Findings |
|---|---:|
| Blocker | 0 |
| High | 0 |
| Medium | 0 |

全部章節已達到「編輯自審後的灰盒候選」標準，可以交付灰盒實作與團隊正式評審。本結論不是科學、醫療、食品、法規、生物安全、生物保安或 Human Practices 正式核准；相關簽核仍須由具權責的人員完成。

## 3. 本輪關鍵修正

| Area | Resolution |
|---|---|
| 第一章來源與用詞 | 加入團隊概念成熟度；統一「偽陰性」；以 `TEAM-PDF-2026-INTRO` 取代使用者電腦絕對路徑 |
| 第一章更正與後果 | 依實際 Choice ID 載入因果、範圍、清理或治理更正；`response_delay_count` 產生額外監測、人力和隔離延遲後果 |
| 第二章評量 | 把明顯錯誤選項改為品質 gate、證據與放行權責的合理近似錯誤 |
| 第三章 reporter | 明確使用已表徵短壽命 GFP 教學抽象，不把一般穩定 GFP 當作快速可逆輸出 |
| 第四章科學設計 | 改用背景扣除、儀器校準及細胞量／狀態檢查後的每細胞輸出；穩健性配置直接測量 A/B × ON/OFF ×兩條件 |
| 第三至四章連續性 | `p_c3_repair` 會改變第四章可見條件與版本／cross-talk 提示，但不預先改寫 canonical 結果 |
| 第六章共同設計 | `c6_transition_plan` 使用兩個精確 package ID，且須由合作社確認，不由玩家策略自動決定 |
| 第七章序列化 | `p_c7_access` 定義為三案例 object，統一使用 `controlled_collaboration` |
| 終章架構決定 | S02 只建立基準／候選比較；`f_solution_architecture` 延至 S08 依證據設定，no-pilot 為完整合法結果 |
| 終章科學與品質 | 補充間斷／變動溫度規則、完整 edge cases、獨立評估及與架構相符的 5A／5B 最終聲明 |
| 終章 standalone | 加入中性結局對白，不虛構玩家曾經歷第一章或完整故事 |
| 共享契約 | 定義 shared flags、草稿階段 precedence、精確 source-to-profile schema、`p_final_access` 及所有承諾 consumer |
| 文件結構 | 修正 teaser 與觸發表欄數；統一腳本狀態；移除工作站專屬絕對來源路徑 |

## 4. 跨章序列化驗收

| Check | Result |
|---|---|
| Source chapter flag 有精確 profile schema | Pass |
| `p_c3_repair` 有 Chapter 4 consumer | Pass |
| `p_c1_monitoring`、`p_c4_question`、`p_c5_pilot` 有終章 consumer | Pass |
| `p_c6_transition` 有 Credits consumer | Pass |
| `p_c7_access` object key 與 enum 一致 | Pass |
| `p_final_architecture` 與 `p_final_access` 均寫入 Credits 狀態 | Pass |
| 沒有 summary 時使用 neutral fallback | Pass |
| `standalone_default` 不偽造歷史決策 | Pass |

## 5. 自動結構驗證

| Check | Result |
|---|---|
| Markdown files checked | 17 |
| Owning script IDs checked | 393 |
| Duplicate owning IDs | 0 |
| Broken relative Markdown links | 0 |
| Unbalanced fenced code blocks | 0 |
| Inconsistent table column counts | 0 |
| Stale absolute local source paths | 0 |

結構驗證只證明文件可被穩定解析及互相引用，不替代遊戲實作後的 loader、save migration、UI overflow、localization、accessibility 或 runtime QA。

## 6. 殘餘簽核風險

1. 第一章感測器宿主、選擇性、背景、閾值、反應時間、封存及廢物流程仍待團隊實測與安全審核。
2. 第二章是成熟歷史案例，但遊戲批次、工廠、品質結果與供應方案均為教學虛構。
3. 第五章 PET hydrolase、終章 cell-free 標籤及其 pilot gate 不得被宣傳成已驗證部署產品。
4. 第六章 2026 年植物與半合成青蒿素實際市場角色仍須以當期來源查核。
5. 兒童資料、食品、醫療、環境、生物安全、生物保安、隱私及申訴流程須按實際地區規則簽核。

## 7. 灰盒進入條件

- 章節 loader 實作 `mode_primary`、`standalone_default` 及 profile summary 缺省行為。
- Save schema 依 `15_SCRIPT_SYSTEM_AND_CONTINUITY.md` 實作 enum、object 與重玩覆寫規則。
- 每章 Critical Path 至少 40% 保留移動、觀察或世界物件操作。
- 灰盒計時驗證完整故事 186–195 分鐘，以及各章 15–30 分鐘範圍。
- 正式對外版本保留來源成熟度、模擬標示、限制及簽核狀態。

---

## 核准

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Lead Game Designer |  |  |  |  |
| Narrative / Education Lead |  |  |  |  |
| Science Lead |  |  |  |  |
| Safety / Security Lead |  |  |  |  |
| Human Practices / Stakeholder Lead |  |  |  |  |
| Technical / QA Lead |  |  |  |  |
