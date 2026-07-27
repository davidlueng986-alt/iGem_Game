# 《微界工程師：生命迴路》2026 遊戲製作文件包

> Production Pack｜版本 2.0｜建立日期 2026-07-26｜邏輯／鏡頭／Future Chapters 再審：2026-07-27｜語言：繁體中文

本文件包是在完整閱讀 GCP、Junior Mission、前導章、第一至第八章、跨章規格、原有兩份自審紀錄，以及團隊提供的汞感測迴路 PDF 後建立。版本 2.0 再次做跨文件邏輯審核，修正第三人稱／自由鏡頭矛盾、Future chapters 的科學與狀態問題，並把第二至第八章的整合製作腳本與技術契約正式寫入 GDD／TDD。

## 一句結論

**原有概念與腳本已具備優秀的編輯灰盒基礎，但「前導章＋八個主章＋Junior 3D 任務」不應被當作 2026 年 11 月前的單一製作承諾。** 本包將 2026 公開 Release Candidate 鎖定為：

1. 5–7 分鐘 2D DOM 前導章；
2. 24–25 分鐘第一章《紅色警報》3D 垂直切片；
3. 3–5 分鐘展覽快速路徑（由上述內容抽取，不另做第二套遊戲）；
4. 第二至終章保留為經審核的未來內容設計庫；
5. Junior Mission 先做紙面／2D／3D 灰盒，只有通過容量與目標玩家測試閘門才升級為 2026 公開 3D 內容。

這個範圍仍有野心，但可以被估算、測試、凍結與交付。AI 可加速規格、程式、測試與審查；它不能取代科學簽核、目標玩家實測、藝術整合、低階裝置效能驗證或產品責任。

## 建議閱讀順序

| 順序 | 文件 | 用途 |
|---:|---|---|
| 1 | [版本 2.0 邏輯、鏡頭與第二至第八章審核](24_LOGIC_CAMERA_AND_CHAPTER_2_8_AUDIT.md) | 先看本輪發現、固定斜俯視鏡頭決定、章節修正及仍待人類簽核事項 |
| 2 | [獨立製作就緒審核](18_INDEPENDENT_PRODUCTION_READINESS_AUDIT.md) | 查看 2026 範圍裁決、科學修正與 Go／No-Go 閘門 |
| 3 | [開放決策登記](20_OPEN_DECISIONS_REGISTER.md) | 把不可由文件作者代替團隊決定的事項分配 Owner 與期限 |
| 4 | [來源與科學宣稱登記](22_SOURCE_AND_CLAIM_REGISTER.md) | 分開文獻機制、團隊提案、團隊數據、故事原型與教學模擬；鎖定 MerR／aptamer 用語 |
| 5 | [GDD](02_GAME_DESIGN_DOCUMENT.md) | 鎖定玩家體驗、內容、系統、章節及驗收 |
| 6 | [TDD](03_TECHNICAL_DESIGN_DOCUMENT.md) | 建立可實作的前端架構、資料模型、效能、存檔與部署方案 |
| 7 | [資產清單與製作規範](04_ASSET_LIST_AND_PRODUCTION_GUIDELINES.md) | 估算、命名、預算、授權、交付及 P0 資產清單 |
| 8 | [專案管理計劃](05_PROJECT_MANAGEMENT_PLAN.md) | 路線圖、容量、RACI、風險、變更控制、Alpha／Beta／RC 閘門 |
| 9 | [QA 與測試計劃](06_QA_TEST_PLAN.md) | 測試矩陣、案例、科學誤解、可及性、效能及 Release 建議 |
| 10 | [AI 輔助開發手冊](19_AI_ASSISTED_DEVELOPMENT_PLAYBOOK.md) | Claude Code、Codex、OpenCode、Cursor 與前沿模型的安全工作流 |
| 11 | [AI 任務包模板](21_AI_TASK_PACKET_TEMPLATE.md) 與 [AGENTS.md](AGENTS.md) | 把每項工作轉成小、可驗證、可回退的 agent 任務 |
| 12 | [交付前驗證報告](23_DELIVERY_VALIDATION_REPORT.md) | 查看結構檢查、已修正問題、驗證邊界與最終結果 |
| 13 | [檔案 Manifest](MANIFEST.md) | 逐檔大小與 SHA-256；配合 `manifest.sha256` 驗證完整性 |

原始概念及腳本仍保留在同一資料夾；原本五份空白模板移至 `_original_templates/`，避免與已完成文件混淆。

## 文件權威順序

發生衝突時依下列順序處理：

1. 經團隊正式簽核的科學、安全、私隱、兒童保障與法規決定；
2. `24_LOGIC_CAMERA_AND_CHAPTER_2_8_AUDIT.md` 的最新修正裁決；
3. `18_INDEPENDENT_PRODUCTION_READINESS_AUDIT.md` 的 2026 範圍裁決；
4. `02_GAME_DESIGN_DOCUMENT.md` 與 `03_TECHNICAL_DESIGN_DOCUMENT.md` v2.0；
5. `15_SCRIPT_SYSTEM_AND_CONTINUITY.md`；
6. 各章完整腳本；
7. `00_GAME_CONCEPT_PROPOSAL.md`；
8. 已標示為歷史／被取代的自審紀錄與空白模板。

各章完整腳本仍是逐句對白、Choice ID 與細部演出的權威來源；GDD v2.0 已加入並重新對齊第二至第八章的逐 Scene 整合製作腳本，TDD v2.0 已加入相應 route、canonical flags、fixtures、camera profile 與 build exclusion 契約。三者若有衝突，先依本頁權威順序處理，不可讓 agent 自動合併差異。科學宣稱仍須同時通過 [來源與科學宣稱登記](22_SOURCE_AND_CLAIM_REGISTER.md) 與具名 Science Lead 簽核。

## 開發前 72 小時

| 時限 | 必須完成 | 產出 |
|---|---|---|
| 第 1 天 | 指派 Product、Tech、Science／Safety、Education／HP、Art、QA Owner | `20_OPEN_DECISIONS_REGISTER.md` 的 Owner 欄不再是「待指派」 |
| 第 1 天 | 確認 2026 P0 範圍及「Junior 是否只做灰盒」 | 一頁 Scope Baseline，所有人簽核 |
| 第 1–2 天 | 取得三台實際學校電腦的 CPU／GPU／RAM／瀏覽器資料 | Device Baseline 表與測試機編號 |
| 第 1–2 天 | 做 Three.js＋DOM UI＋角色碰撞技術 spike | 60 秒可操作場景、效能截圖、Go／No-Go 記錄 |
| 第 2 天 | Science Lead 修訂／撤下 PDF 的 aptamer 頁面對外用法 | 核准版來源 PDF 或書面例外決定 |
| 第 2–3 天 | 建立儲存庫、`AGENTS.md`、CI、格式／型別／單元測試 | 綠色空專案 main branch |
| 第 3 天 | 把前導章 S00–S05 轉成資料表及首批驗收案例 | `content/prelude` fixture 與可追蹤 ticket |

## 目前不可替團隊填寫的資料

本包沒有捏造團隊成員、預算、正式宿主、元件序列、實測效能、研究同意、學校設備或品牌權利。這些欄位以「待決策／待指派」明示，並在開放決策登記中設定預設處置：若期限前仍未確認，範圍會自動縮減，而不是靠 AI 猜測。

## 版本基線

| 項目 | 基線 |
|---|---|
| 2026 P0 | 前導章＋第一章＋展覽快速路徑 |
| 主要語言 | 繁體中文；引擎需 localization-ready |
| 英文 | 先做 3–5 分鐘展覽／評審路徑；完整英文需通過容量 gate |
| 主要裝置 | 桌面 Chrome／Edge；鍵盤滑鼠 |
| 次要裝置 | Firefox best effort；平板／Safari 為 P1，不能阻擋 P0 |
| 技術 | TypeScript、Vite、Three.js、Preact＋Signals、Zod、npm、localStorage；語義化 DOM UI、無後端 |
| 3D 鏡頭與移動 | 固定斜俯視透視鏡頭（isometric-like）；方向不隨角色旋轉，只平移取景；螢幕相對步行、轉向、互動；無自由鏡頭、無跳躍 |
| 數據 | 教學模擬；不視為實驗、醫療、環境或監管結果 |
| 分析 | 預設關閉；本機 QA log；任何遙測另行同意與審核 |
| PWA | Beta 後才啟用；先確保一般靜態部署及離線 zip 可靠 |

## 狀態標記

- **P0：** 不完成便不能發行。
- **P1：** Beta 穩定後才加入；可被砍掉而不破壞核心承諾。
- **R&D：** 用來驗證未知，不可在通過 gate 前列入公開承諾。
- **Future：** 已保留設計價值，但不進入 2026 生產排程。
- **待簽核：** 文件已完成，但權責人尚未作正式決定。


## 固定斜俯視鏡頭基線

- 採 **perspective isometric-like**，不是肩後第三人稱，也不是可旋轉的自由鏡頭；畫面構圖參考 Hades／Diablo 類型，但本遊戲沒有戰鬥。
- 世界方向固定：yaw `45°`、向下角約 `50°`、FOV `40°`；玩家不能旋轉、俯仰或縮放鏡頭。
- 鏡頭會隨玩家**位置**沿世界平面平移，以玩家或 authored focus 為取景目標；不跟隨角色面向、不繞到背後。`W／↑` 永遠朝螢幕上方移動。
- 遮擋以屋頂／牆面切開、`CameraOccluder` 淡出及關卡構圖解決，不使用鏡頭臂碰撞或突然貼近角色。
- Future 第二至第八章已寫入 GDD／TDD，但 production manifest、P0 bundle、P0 QA gate 與 2026 排程仍只包含前導章、第一章及 Expo。


## C2–C8 權威來源

| 層級 | 負責內容 |
|---|---|
| `08_CHAPTER_02_FULL_SCRIPT.md` 至 `14_FINAL_CHAPTER_FULL_SCRIPT.md` | 逐句對白、Choice ID、章內 canonical flags、scene entry／exit |
| `02_GAME_DESIGN_DOCUMENT.md` 9.4 | 玩家行動、證據、near-miss、可見後果、zone 與章末輸出 |
| `03_TECHNICAL_DESIGN_DOCUMENT.md` 9.8 | route、schema、fixture、transaction、validation、Future build exclusion |

任何差異都要先修文件再開發；不得讓 AI agent 自行選一個版本。版本 2.0 的結構／邏輯 validator 通過，也不代表科學、產品或公開發行已核准。
