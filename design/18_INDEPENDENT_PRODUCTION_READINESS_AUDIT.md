# 《微界工程師：生命迴路》獨立製作就緒審核

> Independent Production Readiness Audit｜版本 1.1｜審核日期 2026-07-27｜狀態：**有條件通過立項；原全量範圍不通過生產排程**

| 審核欄位 | 內容 |
|---|---|
| 審核範圍 | GCP 1.4、原 GCP 自審、Junior、前導章、第一至第八章、continuity、全腳本自審、五份空白製作模板、團隊汞感測器 PDF |
| 審核目的 | 判斷內容是否可直接進入真實遊戲製作，並建立 2026 年 11 月前可交付的 GDD／TDD／資產／PM／QA 基線 |
| 審核方法 | 文件逐頁／逐章閱讀、跨文件一致性檢查、Markdown 結構檢查、科學宣稱分層、製作量與時程推演、瀏覽器遊戲風險與 AI 工作流審核 |
| 外部查核日期 | 2026-07-27；AI 產品與 iGEM 日程屬易變資訊，需在每個里程碑重新核對 |
| 最終裁決 | **Concept／Editorial：通過。Science for public release：待簽核。Production scope as written：不通過。2026 P0 reduced slice：有條件通過。** |

## 1. 執行摘要

原始材料最強的部分不是「有很多章」，而是已建立一套一致且負責任的教育玩法語法：玩家蒐集證據、形成有限主張、看見後果，再修訂方案；安全、倫理、Human Practices 與溝通不是附加說明，而是通關機制。第一章也清楚分開團隊 proposal、文獻機制、遊戲虛構原型與未經驗證的效能。這些基礎值得保留。

然而，原有兩份自審的「Blocker／High／Medium = 0」只適用於**編輯結構與灰盒候選內容**，不能被解讀為「已可按全部章節進入 2026 生產」。在 2026-07-27 至 iGEM Grand Jamboree 的時間內，同時製作前導章、八個主章、Junior 3D 任務、兩種模式、完整可及性、平板、PWA、多語言、資產、目標玩家研究和科學簽核，對未提供人力與設備證據的高中團隊屬不可控承諾。前沿 AI 可以壓縮部分編碼與文件時間，但不會消除整合、內容審核、3D 資產、效能、瀏覽器差異、未成年人研究和真人 playtest 的臨界路徑。

因此本審核採用以下 2026 Scope Baseline：

- **P0 公開 RC：** 前導章＋第一章《紅色警報》＋同內容抽取的展覽快速路徑；
- **R&D：** Junior Mission 先以紙面／2D／共用場景灰盒驗證；
- **Future：** 第二至終章不進入 2026 公開 build，只保留腳本、資料 schema 與概念 proof；
- **不承諾：** 手機、完整平板、全配音、多人、後端帳號、完整英文八章、無縫世界或真實濕實驗模擬。

## 2. 審核結果總表

| 面向 | 分級 | 判定 | 核心理由 |
|---|---|---|---|
| 願景與差異化 | 強 | 通過 | 玩家角色、Evidence→Claim→Consequence、責任設計及公眾參與具清楚特色 |
| 前導章／第一章內容 | 強 | 有條件通過 | 已接近灰盒規格，但仍需科學、適齡、時長及操作實測 |
| 第二至終章腳本 | 強的設計庫 | 不列入 2026 P0 | 內容完整不等於具備所需系統、資產與 QA 容量 |
| Junior Mission | 教育概念良好 | R&D | 9–12 歲的詞彙、3D 控制、22 分鐘與 transfer 尚未經目標玩家驗證 |
| 科學準確性 | 中上 | 待正式簽核 | MerR 主線合理但簡化；aptamer 頁面需實質修訂；所有效能尚未實測 |
| 製作範圍 | 過大 | 原範圍不通過 | 章數、模式、3D、語言、裝置與 QA 的乘法效應未被容量證據支持 |
| 技術方向 | 合理 | 有條件通過 | Three.js＋DOM 適合；物理、PWA、平板、存檔和效能仍需 spike |
| 可及性 | 原則良好 | 待實作驗證 | 3D canvas 不能只靠文件宣稱可及；需要 DOM 替代、鍵盤、焦點與 guided path |
| 私隱／兒童保障 | 原則良好 | 待地區審核 | 無帳號是正確方向；研究同意、錄影、遙測仍需正式流程 |
| AI 開發計劃 | 可行但有風險 | 有條件通過 | 必須採小任務、獨立 review、資料邊界、成本上限和人工合併 |

## 3. 嚴重度定義

| Severity | 定義 | Release 處理 |
|---|---|---|
| Blocker | 若未解決，無法合理開始或不能公開發行 | 不得進入相應 gate |
| High | 很可能造成重大延誤、科學誤導、資料／兒童風險或核心玩法失敗 | Alpha 前關閉或有正式例外 |
| Medium | 不會立即阻斷，但會造成返工、體驗或維護問題 | Beta 前關閉或排入已接受債務 |
| Low | 文案、流程或易用性改善 | 依容量處理 |

## 4. Blocker Findings

### B-01：2026 生產範圍沒有容量證據

**觀察：** 原文件描述 Junior、前導及八章主線，原文件曾把完整主線上限寫成 202 分鐘，但逐章明列的最小值相加為 192 分鐘、最大值為 203 分鐘；現行 GCP／GDD 已修正為 192–203 分鐘。除此之外還包括 3D 世界、兩種模式、平板方向、PWA、存檔、可及性、學習研究與多種資產。

**風險：** 團隊容易把「腳本已完成」誤當成「內容已接近完成」。遊戲生產的成本主要在實作、整合、資產、測試與修訂，而不是章節文字長度。AI 會令新增內容看似便宜，卻把未測試表面積快速放大。

**處置：** 2026 P0 只包含前導章與第一章。第二至終章在 2026 只可製作不影響 P0 的 schema、共用原型或 30–90 秒 proof，不可建立公開章節承諾。Junior 必須通過 PM-GATE-JR 才能升級。

**關閉條件：** 團隊在 2026-08-02 前提供角色名冊、每週有效工時、設備、預算與 Scope Baseline 簽核。

### B-02：正式 Owner、審批權與可用時間未提供

**觀察：** 原始核准表全部空白。Science、Safety、Education／HP、Technical、Art、QA 與 Product 的最終權責未被指派。

**風險：** AI 或最積極的開發者會在沒有權責人時默認作出科學、兒童研究、授權或產品決策；意見衝突只會在接近交付時出現。

**處置：** 使用 `20_OPEN_DECISIONS_REGISTER.md` 指派角色，姓名不可由 AI 代填。任何 Blocker Owner 未指派時，該範圍自動降級或停止。

### B-03：團隊 PDF 的 aptamer 迴路說明不可直接作對外科學基線

**來源：** 團隊 PDF 第 3–5 頁。

**觀察：** PDF 把「promoter → Hg²⁺ aptamer → dTomato → terminator」描述為：無汞時 aptamer 髮夾阻擋 transcription；有汞時形變清除阻擋。Aptamer 本身只是辨識域；要可靠控制轉錄或翻譯，通常還需要一個與其耦合的 expression platform，例如 terminator／anti-terminator、RBS sequestration 或其他經驗證的 switching architecture。RNA 亦要在轉錄開始後才形成，因此圖文若暗示 promoter 後的裸 aptamer 直接阻止 RNA polymerase 開始轉錄，會造成錯誤機制印象。

**風險：** 對外簡報、wiki 或遊戲若把該圖當成已定義 construct，會把未指定的調控機制說成完整設計。

**處置：** 第一章繼續只用 PDF 第 1–2 頁 MerR/Pmer 方案；aptamer 方案在 Science Lead 提供明確 expression platform、序列架構、宿主與引用前，不進入遊戲或宣傳。PDF 應改為「概念方向／需加入經驗證的表達平台」，或暫時撤下第 4–5 頁。

**關閉條件：** Science Lead 書面核准修訂版，並把源文件 ID 固定為 `TEAM-PDF-2026-INTRO`，不再依 `(4)`／`(5)` 檔名辨識版本。

### B-04：目標學校設備與目標玩家研究安排未建立

**觀察：** 文件有 30 FPS 目標與年齡分流，卻沒有實際學校電腦、瀏覽器管理限制、課堂網路、鍵盤配置、研究同意或招募名單。

**風險：** 開發者只在高階個人電腦測試；直到工作坊才發現 WebGL、GPU、下載、鍵盤、閱讀量或鏡頭不適用。

**處置：** 8 月首週至少取得三台低階／中階學校裝置資料，並在 Alpha 前完成 5–8 名中學生／公眾灰盒測試。Junior 若要公開，另需 5–8 名 P4–P6 及教師的獨立研究；較年長玩家不能代替。

## 5. High Findings

### H-01：原自審「零高風險」需要重新定義

原有 `01_GCP_REVIEW_AUDIT.md` 與 `16_FULL_SCRIPT_REVIEW_AUDIT.md` 的結論在其限定範圍內成立：Markdown 結構、內容一致性和編輯灰盒沒有未解高風險。但它們沒有估算真實生產容量、資產量、瀏覽器實作、AI 治理或外部簽核。因此本包保留原紀錄，並把它們標為 **Editorial Readiness Audit**；公開簡報不得只引用「Blocker = 0」而省略限制。

### H-02：MerR/Pmer 機制可用，但圖文仍需更精確

PDF 第 1–2 頁與 GCP 的兩轉錄單元一致：`Pconst → merR` 及 `Pmer → dTomato`；無 Hg²⁺ 時低訊號，有 Hg²⁺ 時轉錄提高。第一章把 MerR 與 promoter DNA 幾何變化寫入說明，是比「由 repressor 直接變成 recruiter」更穩健的表述。

仍需注意：

- MerR family 的切換依賴具體 promoter、spacer geometry、宿主和 context，不能把任何 `Pmer` 標籤視為可直接互換；
- OFF 應稱「低背景／低於教學閾值」，不應說絕對零；
- dTomato 需要表達與螢光團成熟，訊號不是即時、也不等同濃度；
- 未有校準、選擇性、交叉反應、基質效應、反應時間和檢出限資料前，不能宣稱真實監測性能；
- 統一寫作 `Hg²⁺`，避免 `Hg++`；`MerR/Pmer` 的大小寫需固定。

### H-03：兩種模式、兩條路線與多語言會造成乘法成本

引導／標準模式共用成功條件是正確的，但每個 UI、提示、對話、圖表、焦點路徑和 QA 都需要兩種內容狀態。Junior 又是獨立產品路線。同步完整中英版本會進一步增加文字溢出、科學術語與 LQA 表面積。

**處置：** P0 canonical language 為繁體中文；資料結構從第一天支援 locale key。英文只先做展覽快速路徑與核心 UI。完整英文第一章要在 2026-09-14 由容量 gate 決定。Junior 不與主線同時進入 polishing。

### H-04：PWA 不應成為 Alpha 的必要相依

Service worker 的舊版快取、半更新 bundle、學校代理伺服器與離線回復會引入新的 release failure。P0 先提供可靠靜態站與可下載的離線 zip；PWA 只在 Beta 後以獨立 build flag 開啟，並須通過更新、rollback、cache corruption 和多版本 migration 測試。

### H-05：3D 可及性不能只靠 DOM overlay 宣稱完成

將前導與文字 UI 放入語義化 DOM 是正確方向，但固定斜俯視 3D 導航仍會排除部分使用者。P0 必須提供：完整鍵盤、焦點可見、互動清單／目標指引、無鏡頭操作要求、降低動態、移動預視開關、無需精準平台操作、隨時回到安全節點。對關鍵學習步驟，應有 point-and-click／guided fallback，而不是要求 screen reader 操作 3D canvas。文件不得在未經使用者測試前宣稱「符合完整 WCAG」。

### H-06：AI 不能同時當作者、測試者與唯一核准人

多個 coding agent 能並行增加吞吐，但也會產生架構漂移、重複抽象、未被理解的依賴、測試假陽性和科學文案變更。每一項 agent 變更必須採「Plan → 小範圍實作 → 自動測試 → 不同模型／人員 review → 人工 merge」。Science、Safety、未成年人資料、授權和對外宣稱不可由模型自動核准。

## 6. Medium Findings

| ID | 發現 | 影響 | 已採處置 |
|---|---|---|---|
| M-01 | GCP 完整主線上限寫 202 分鐘，但逐章最大值合計 203 分鐘 | 版本與工作坊估算不一致 | GDD 記錄為 192–203 分鐘，待灰盒後重估 |
| M-02 | GCP 內曾引用 `iGEM 2026 intro(5).pdf`，實際提供檔名為 `(4)` | 檔名版本漂移 | 使用穩定 Source ID `TEAM-PDF-2026-INTRO` |
| M-03 | GCP 系統表列「跳躍」，腳本沒有平台需求 | 增加碰撞、動畫、相機與 QA 成本 | P0 移除跳躍；必要坡道以 walkable slope 解決 |
| M-04 | 30 MB「首章下載」未分 shell、前導與章節 | 難以追責效能回歸 | TDD 改為 shell ≤3 MB、前導增量 ≤5 MB、第一章增量 ≤25 MB、P0 cached ≤35 MB |
| M-05 | 平板列為次要支援但沒有 touch UX | 容易在宣傳時被誤稱支援 | P1；只有通過獨立 touch playtest 才列入支援矩陣 |
| M-06 | 章末四維回饋可能被玩家理解成總分 | 與責任取捨理念衝突 | 不計總分、不設排行榜；每維只顯示證據與下一步 |
| M-07 | 對話與科學內容量大 | 24–25 分鐘可能超時 | 每段先操作後解釋；可選延伸資訊預設收合；Alpha 真時計時 |
| M-08 | 完整配音未有成本／語言計劃 | 資產與 LQA 爆量 | P0 無全配音；只做非語義聲音、短確認音與可選重要句 |
| M-09 | 分析需求未明確 | 兒童資料風險 | 公開 build 預設無遙測；QA event 只存在本機並可匯出 |
| M-10 | 模擬資料可能被截圖脫離脈絡 | 對外誤認為實驗結果 | 每個圖表永久顯示「教學模擬」水印與 source maturity tag |

## 7. 設計審核

### 7.1 主要優點

1. **核心玩法語法一致。** Junior、前導及每個主章都能追蹤 Evidence、Claim、Consequence／Revision，避免把遊戲退化為選擇題集合。
2. **責任不是結尾字幕。** 安全層、權責邊界、居民意見、品質 gate、供應與治理會改變玩家方案。
3. **權限設定成熟。** 玩家可以設計、判讀與提案，但不能自行診斷、執法、確認污染、清理或批准部署。
4. **錯誤可修復。** near-miss 先展示後果再讓玩家局部修改，適合學習而非懲罰。
5. **科學成熟度有分層。** 機制、團隊 proposal、團隊實驗、故事原型與教學模擬被區分。
6. **章節可獨立討論。** 後續章節涵蓋製造、品質、數據、環境、供應、公平、雙重用途及共同設計，構成有價值的未來設計庫。

### 7.2 需要縮減或改寫的部分

- P0 不做跳躍、外觀自訂、完整總部、章間世界狀態、全配音、教師後台、雲端存檔或公開遙測。
- 第一章場景合併為三個可重用模組：河港、安全研究站、公民會議／報告；不建造完整城市。
- NPC 採共享 rig、有限姿勢和對話標記，不做面部捕捉或專屬動畫樹。
- 所有延伸科學資料預設收合，Critical Path 的每一段必須在 30 秒內出現玩家操作。
- 展覽模式只建立 session reset、快速入口及 3–5 分鐘節點，不另做專屬內容分支。

## 8. 技術審核

### 8.1 通過的方向

- TypeScript＋Vite＋Three.js；
- 2D 卡牌、對話、證據與設定使用語義化 DOM；
- 任務與內容資料驅動；
- 小型獨立場景與 lazy load；
- 本機 versioned save；
- 無後端、無帳號、無公開聊天；
- 靜態部署及離線包。

### 8.2 必須先做的技術 spike

| Spike | 時限 | Pass 條件 | Fail 時 fallback |
|---|---:|---|---|
| Three.js＋DOM Overlay | 1 天 | 低階測試機 60 秒場景 ≥30 FPS；鍵盤焦點不被 canvas 吞掉 | 降低材質／光源；更多教學改為 2D |
| 角色碰撞 | 1 天 | 樓梯／斜坡／牆角無穿透；重置可用；WASM 啟動符合預算 | 改用簡化 capsule/AABB、無動態物理 |
| GLB pipeline | 0.5 天 | Blender→壓縮 GLB，材質、scale、pivot、動畫一致 | 減少材質、改靜態 props、固定 exporter |
| Save migration | 0.5 天 | v1→v2 fixture 不丟進度；corrupt save 可回復 | 只保存章節級 summary，不保存場景細節 |
| PWA update | Beta 後 1 天 | offline／update／rollback 全通過 | 2026 build 不啟用 service worker |

### 8.3 建議 UI 架構

使用 Preact 管理 DOM UI、screen registry、焦點與設定；Three.js 只負責世界呈現。兩者透過 typed event／command bus 連接，不讓 3D scene 直接查找 DOM，也不讓 UI 直接修改 scene object。這是本審核新增的技術選擇，源文件只指定語義化 DOM，沒有指定 UI framework；選擇 Preact 是為了以較小 runtime 取得組件、狀態和可測試性。若首週 spike 顯示團隊對框架不熟，允許改為原生 DOM custom elements，但必須保留相同 public contracts。

## 9. 資產與製作量審核

2026 P0 應使用一套共享角色比例、三個小型場景 kit、有限環境 props、少量 VFX、DOM UI 與沒有完整 VO 的聲音方案。目標不是「看起來像大型商業 3D 遊戲」，而是讓科學因果與公共空間清楚、穩定、可讀。

| 類別 | 原概念容易膨脹的方向 | P0 裁決 |
|---|---|---|
| 世界 | 近未來城市、研究總部、多地區 | 只做河港、研究站、公民會議三個載入單元 |
| 角色 | 玩家自訂、各章 NPC | 一個中性玩家 avatar、5–6 個 NPC、共享 skeleton |
| 動畫 | 高成本完整 locomotion、表情 | 固定斜俯視可讀的 idle／walk／turn／interact／talk gesture；無跳躍、無 facial rig |
| 科學裝置 | 每章專屬工作台 | 只做 circuit bench、test bench、safety bench；UI 承擔複雜度 |
| 音訊 | 多狀態音樂及配音 | 3–4 個短 loop、必要 SFX、字幕；無完整 VO |
| 本地化 | 全章中英同步 | zh-Hant P0；英文展覽路徑；其餘 locale-ready |

## 10. AI 開發能力審核（截至 2026-07-27）

前沿模型已能處理長距離程式任務、多檔案 refactor、工具呼叫與 review；Codex、Claude Code、OpenCode 與 Cursor 也能提供 repo 級 agent workflow。但能力越高，越需要明確界線：模型會很快把含糊設計「完成」成一套難以驗證的實作，並可能把來源文件中的未核准科學文字視為事實。

本專案應以**能力層級**而非品牌鎖定：

- 長時間架構／跨檔任務：使用團隊當下可取得的最高可靠 coding model，例如 GPT‑5.6 Sol、Claude Fable 5，或在實際可用、授權與成本通過後的 Kimi K3；
- 快速單檔實作／測試補齊：使用較便宜模型；
- 獨立 review：盡量使用不同模型或至少不同 session／subagent；
- 科學、HP、兒童與發行決策：只可整理證據，不可自動核准。

Moonshot 官方 quickstart 表示 Kimi K3 full weights 會在 2026-07-27 前／當日發布；本交付沒有獨立完成可下載權重 artifact、license、推理供應商、成本與高中硬體可承載性的驗證，因此仍不得把本地部署或完整 1M context 視為既定交付能力。即使權重按期發布，超大型模型的本地部署也不應成為 P0 的必要相依。

## 11. 2026 建議範圍與 Gate

### 11.1 Scope Baseline

| Tier | 內容 | 公開承諾 |
|---|---|---|
| P0 | 前導 S00–S05、第一章 S00–S08、設定、存檔、章末報告、展覽快速入口 | 必須完成並通過 RC |
| P1 | PWA、英文完整第一章、平板、教師摘要、少量配音 | Beta 後按容量加入 |
| R&D | Junior 紙面／2D／共用場景灰盒、第二章 schema proof | 不宣稱為完成產品 |
| Future | 第二至終章完整實作 | 2027 或另立項 |
| Won't 2026 | 多人、帳號、後端、全城市、戰鬥、濕實驗步驟、環境釋放、完整手機 | 明確排除 |

### 11.2 硬閘門

| Gate | 日期 | 必須證據 | 不通過時處置 |
|---|---:|---|---|
| G0 Scope／Owner | 2026-08-02 | 名冊、容量、範圍、Science Owner、三台裝置 | 只做前導 2D＋展覽 demo |
| G1 Technical Spike | 2026-08-09 | 30 FPS、角色碰撞、DOM focus、GLB pipeline、CI | 降低 3D、移除 Rapier／PWA／平板 |
| G2 Core Greybox | 2026-08-30 | 前導完整；第一章可從 S00 走到 S04；save／reset | 停止新資產與新章，修核心 loop |
| G3 Alpha | 2026-09-14 | 第一章全流程、首輪中學生 playtest、science issue list | 砍英文／Junior／裝飾資產 |
| G4 Beta／Content Freeze | 2026-10-11 | 科學核准、核心 bug 關閉、低階裝置、可及性回歸 | 不增加功能；必要時縮短 S05–S08 |
| G5 Release Candidate | 2026-10-21 | build、離線包、source／license、QA report、rollback | 延後公開或只發展覽受控 build |
| G6 Jamboree Freeze | 2026-11-01 | 演示腳本、影片備份、無 Blocker／High | 只修 blocker；保留已驗證 RC |

iGEM 2026 Grand Jamboree 為 2026-11-13 至 11-16；官方 software deliverable 指引如適用，應以 2026-10-21 為外部交付檢查點，但團隊必須按其參賽 village／track 和當屆 deliverables 再確認，不得只依本文件。

## 12. 審核後已完成的文件變更

| 變更 | 文件 |
|---|---|
| 把 2026 P0 與完整 design bible 分開 | GDD、PM、README |
| 移除 P0 跳躍、完整 VO、帳號、遙測與手機承諾 | GDD、TDD、Asset、QA |
| 建立 Preact＋Three.js 分層與 Rapier spike gate | TDD |
| 量化 shell／chapter、draw call、triangle、memory、FPS 預算 | TDD、Asset、QA |
| 建立具 ID 的 P0 資產清單與授權／AI provenance 流程 | Asset Guidelines |
| 建立 7/27–11/16 時程、容量級別、RACI、風險和 change control | PM |
| 建立功能、科學誤解、可及性、效能、存檔與 release 測試案例 | QA |
| 建立多 agent 的 Plan／Build／Review／Merge 規則 | AI Playbook、AGENTS.md |
| 把未能代填的決策轉成有期限、有 fallback 的 register | Open Decisions |
| 建立 MerR／aptamer 的 source-to-claim gate、核准 wording 與禁止主張 | [Source & Claim Register](22_SOURCE_AND_CLAIM_REGISTER.md) |

## 13. 最終判定

### 13.1 可以立即開始

- 建立 repo、CI、資料 schema 與前導章 DOM prototype；
- 製作一個小型河港 greybox 和角色移動；
- 把第一章 S00–S04 轉成資料驅動流程；
- 建立科學宣稱登記、模擬水印與對照失敗測試；
- 招募並安排中學生／公眾 playtest；
- 由 Science Lead 修訂 aptamer 頁面。

### 13.2 在簽核前不可做成公開宣稱

- 團隊的具體 MerR construct 已成功、靈敏、選擇性高或可現場監測；
- aptamer 頁面代表可工作的完整 riboswitch；
- 遊戲已適合所有小四至小六玩家；
- 3D 體驗完整符合某個可及性標準；
- 工程細胞或任何單一 containment 能保證零風險；
- AI 產生的程式、圖像或文字不需人工、授權與來源審核。

### 13.3 Decision

**GO（有條件）：** 按本包 P0 進入 12 週垂直切片製作。  
**NO-GO：** 把全部現有章節、Junior 3D、完整雙語與平板同時承諾為 2026 發行內容。  
**強制重審：** 2026-08-02、09-14、10-11、10-21。

## 14. 正式簽核

| 角色 | 姓名 | 決定 | 日期 | 必須確認的事項 |
|---|---|---|---|---|
| Product Owner | 待指派 | 待決定 | — | P0 範圍與外部承諾 |
| Technical Lead | 待指派 | 待決定 | — | 架構、裝置、容量、部署 |
| Science Lead | 待指派 | 待決定 | — | MerR／aptamer、claims、模擬標示 |
| Safety／Security Lead | 待指派 | 待決定 | — | 生物安全、雙重用途、資料與 agent 邊界 |
| Education／HP Lead | 待指派 | 待決定 | — | 目標玩家、研究、居民角色與學習證據 |
| Art Lead | 待指派 | 待決定 | — | 資產範圍、授權與風格 |
| QA／Release Lead | 待指派 | 待決定 | — | Gate、測試證據、release recommendation |


> **v1.1 補充：** 鏡頭與第二至第八章的最新邏輯裁決以 `24_LOGIC_CAMERA_AND_CHAPTER_2_8_AUDIT.md`、GDD 2.0 與 TDD 2.0 為準。
