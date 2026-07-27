# 《微界工程師：生命迴路》來源與科學宣稱登記

> Source & Claim Register｜版本 1.1｜日期：2026-07-27｜狀態：第一章候選基線；公開前仍需具名 Science／Safety 簽核

## 0. 目的

本登記用來防止最常見的科學溝通錯誤：把文獻機制、團隊 proposal、團隊數據、遊戲虛構原型與教學模擬混成同一件事。任何對玩家、評審、wiki、海報、影片或社群公開的科學句子，都應能追溯到 Claim ID、Source ID、限制與具名核准人。

本文件不替團隊補寫未提供的宿主、序列、promoter variant、plasmid backbone、實驗條件、性能或安全結果。沒有來源便標為 Unknown／Unsupported，而不是由 AI 猜測。

## 1. 成熟度標籤

| Tag | 中文顯示 | 定義 | 可否公開 |
|---|---|---|---|
| `MECHANISM` | 文獻機制 | 由可追溯文獻支持的一般機制；仍需說明 context | 可，限於核准 wording |
| `TEAM_PROPOSAL` | 團隊設計提案 | 團隊想測試／建立的設計，尚不代表已工作 | 可，必須使用未完成語氣 |
| `TEAM_DATA` | 團隊實驗資料 | 有可查方法、版本、原始資料、分析與限制 | 只有正式簽核後 |
| `STORY_PROTOTYPE` | 故事原型 | 為敘事而虛構、合成或簡化的裝置／結果 | 可，必須明示虛構／教學用途 |
| `TEACHING_SIMULATION` | 教學模擬 | 用於玩法的合成數據或狀態 | 可，永久水印；不可當實驗結果 |
| `UNVERIFIED` | 未驗證 | 資料或 context 不足 | 不可作肯定宣稱 |
| `NOT_APPROVED` | 未核准公開 | 有實質科學、Safety 或來源問題 | 不可進公開 build／宣傳 |

## 2. Claim 狀態

| Status | 定義 |
|---|---|
| Draft | 候選句，尚未由 Science Lead 核准 |
| Approved with limits | 可按登記 wording 與限制使用 |
| Approved | 可在指定 scope 使用 |
| Needs source | 需要文獻／團隊文件／數據 |
| Needs construct detail | 一般機制可用，但團隊具體實作未定義 |
| Rejected | 科學或溝通上不可使用 |
| Retired | 曾核准但已由新版本取代 |

公開 build 只可使用 `Approved` 或 `Approved with limits`；本版本全部仍需具名簽核，因此表中即使寫 `Candidate: approve with limits`，仍不是正式核准。

## 3. Source Catalog

### 3.1 團隊來源

| Source ID | 文件／位置 | 類型 | 支持範圍 | 已知限制／動作 |
|---|---|---|---|---|
| `TEAM-GCP-1.4` | `00_GAME_CONCEPT_PROPOSAL.md` | 團隊設計文件 | 遊戲定位、玩家權限、章節、MerR 教學方向 | 不是實驗證據；完整範圍已被製作審核縮減 |
| `TEAM-PDF-2026-INTRO` | 團隊提供的 `iGEM 2026 intro(4).pdf` | 團隊 proposal 圖解 | p.1–2 MerR／Pmer 兩轉錄單元；p.3 aptamer 定義；p.4–5 aptamer-based concept | 檔名曾在 GCP 寫 `(5)`；以穩定 ID 管理。p.4–5 未定義 expression platform，暫不可公開使用 |
| `TEAM-SCRIPT-PRE` | `07A_PRE_CHAPTER_FULL_SCRIPT.md` | Canonical game script | Evidence／claim／control、科學成熟度教學 | 內容來源不等同科學核准 |
| `TEAM-SCRIPT-C1` | `07_CHAPTER_01_FULL_SCRIPT.md` | Canonical game script | 第一章 MerR、control、限制、居民／安全情境 | 對白需逐項對應 Claim ID |
| `TEAM-CONTINUITY-1.3` | `15_SCRIPT_SYSTEM_AND_CONTINUITY.md` | Content／state spec | 跨章變量、權限、限制、教學標籤 | 不是外部科學來源 |
| `TEAM-AUDIT-GCP` | `01_GCP_REVIEW_AUDIT.md` | 團隊／編輯自審 | 結構、一致性、灰盒 readiness | 「零 blocker」不代表 production／science release ready |
| `TEAM-AUDIT-SCRIPT` | `16_FULL_SCRIPT_REVIEW_AUDIT.md` | 團隊／編輯自審 | 腳本完整性、一致性 | 同上 |

### 3.2 外部機制來源（本審核新增；公開前由 Science Lead 閱讀全文）

| Source ID | 來源 | 用途 | 重要限制 |
|---|---|---|---|
| `EXT-MERR-1990` | Frantz & O’Halloran, “DNA distortion accompanies transcriptional activation by the metal-responsive gene-regulatory protein MerR,” *Biochemistry* 29 (1990), DOI `10.1021/bi00472a001`, PMID `2364056` | 支持 Hg–MerR 與 promoter DNA 結構改變、促進 transcriptionally competent open complex 的機制 | 歷史研究與特定系統；不等於團隊 construct 性能 |
| `EXT-MERR-REVIEW-2022` | “Bacterial MerR family transcription regulators: activation by distortion,” PMID `35130613` | 支持 MerR-family promoter 通常具有異常較長 -35／-10 spacer，透過 DNA distortion 調節 | 家族 review；具體 MerR、Pmer、宿主、spacer 仍要核對 |
| `EXT-RIBOSWITCH-2013` | Wachsmuth et al., “De novo design of a synthetic riboswitch that regulates transcription termination,” *Nucleic Acids Research* 41:2541–2551, DOI `10.1093/nar/gks1330` | 清楚區分 aptamer sensor 與 actuator／expression platform；展示 transcriptional switch 需要 spacer、aptamer-complementary terminator／U-rich element及 co-transcriptional design | Theophylline system，不支持任何特定 Hg²⁺ aptamer；用途是證明「裸 aptamer 不足以指定調控機制」 |

External URL snapshot：

- `https://pubmed.ncbi.nlm.nih.gov/2364056/`
- `https://pubmed.ncbi.nlm.nih.gov/35130613/`
- `https://academic.oup.com/nar/article/41/4/2541/2414752`

## 4. 第一章 Claim Register：MerR／Pmer

| Claim ID | Maturity | Candidate status | 可使用的候選 wording（繁中） | 必須同時顯示的限制 | 禁止／需避免 wording | Sources | Gate／Owner |
|---|---|---|---|---|---|---|---|
| `HG-MECH-001` | MECHANISM | Approve with limits | 「MerR 是一類可感應金屬離子的轉錄調控蛋白；在適當 promoter context 中，其狀態會影響轉錄。」 | 說明為一般機制，不代表任何 Pmer 都相同 | 「MerR 在所有系統都像普通開關一樣工作」 | EXT-MERR-1990；EXT-MERR-REVIEW-2022 | Alpha／Science |
| `HG-MECH-002` | MECHANISM | Approve with limits | 「MerR-family promoter 常以非典型的 -35／-10 間距與 DNA 幾何參與調控。」 | `常`、`context-dependent`；不要給團隊未提供的確切 spacer | 「只要把 MerR 放在 promoter 前便會啟動」 | EXT-MERR-REVIEW-2022 | Alpha／Science |
| `HG-MECH-003` | MECHANISM | Approve with limits | 「在無目標 Hg²⁺ 的狀態，MerR 結合調控區時，Pmer 的輸出維持低背景。」 | 用低背景，不用絕對零；教學閾值是遊戲設定 | 「完全沒有轉錄／完全沒有 dTomato」 | TEAM-PDF p.1–2；EXT sources；team script | Alpha／Science |
| `HG-MECH-004` | MECHANISM | Approve with limits | 「Hg²⁺ 與 MerR 作用後，MerR／promoter DNA 的構形關係可改變，使 Pmer 的轉錄增加。」 | 具體反應依蛋白、promoter、宿主與條件；避免把 MerR 描述成單純離開 DNA | 「Hg²⁺ 令 MerR 從 repressor 變成會直接把 RNA polymerase 拉來的通用 recruiter」 | EXT-MERR-1990；EXT-MERR-REVIEW-2022；TEAM-PDF p.2 | Alpha／Science |
| `HG-MECH-005` | MECHANISM | Approve with limits | 「dTomato 作為紅色螢光 reporter，可把基因表達狀態轉成可觀察訊號。」 | 需要表達、摺疊／成熟；訊號依系統與讀取方式 | 「dTomato 一生成便立即顯示準確濃度」 | TEAM-PDF p.1–2；team script | Alpha／Science |
| `HG-MECH-006` | MECHANISM | Approve with limits | 「螢光訊號反映 reporter output；要推論 Hg²⁺ 濃度，需要校準、controls 與實驗驗證。」 | 遊戲沒有提供真實校準 | 「紅色越亮就等於 Hg²⁺ 濃度是某個數字」 | General measurement logic；TEAM script | Alpha／Science＋Education |
| `HG-MECH-007` | MECHANISM | Needs source／construct | 「選擇性、背景、反應時間、dynamic range、limit of detection 與 matrix effect 必須以團隊 construct 實測。」 | 目前 unknown | 任何具體性能數字、`highly sensitive`、`field-ready` | Team data required | Beta／Science |
| `HG-MECH-008` | MECHANISM | Approve with limits | 「positive、negative 與 no-template／blank 等 controls 幫助判斷訊號是否可解讀。」 | 實際 control 名稱需配合團隊方法；遊戲只教概念 | 「有一個紅光就已確認污染」 | TEAM-SCRIPT-PRE／C1；Science approval | Alpha／Science＋Education |
| `HG-MECH-009` | MECHANISM | Approve with limits | 「單一 reporter 結果不足以取代正式環境採樣、分析、監管或公共決策。」 | 對外 disclaimer；玩家權限受限 | 「本遊戲／此細胞可確認河水污染」 | GCP／scripts；Safety decision | Beta／Science＋Safety |

## 5. 團隊設計 Proposal Claims

| Claim ID | Maturity | Candidate status | 可使用 wording | 必須限制 | 不可使用 | Required evidence／owner |
|---|---|---|---|---|---|---|
| `HG-TEAM-001` | TEAM_PROPOSAL | Needs construct detail | 「團隊提出以 constitutive MerR 調控單元配合 Pmer–dTomato reporter 的設計方向。」 | 明示 `提出／計劃／候選設計` | 「團隊已建立可工作的汞感測器」 | 實際 design record；Science |
| `HG-TEAM-002` | TEAM_PROPOSAL | Needs construct detail | 「團隊圖示包含兩個轉錄單元：`Pconst → merR → terminator` 與 `Pmer → dTomato → terminator`。」 | 這是圖示層；未提供具體 promoter、RBS、host、vector、sequence | 把箭頭圖當完整可重現 construct | TEAM-PDF p.1–2；Science |
| `HG-TEAM-003` | TEAM_PROPOSAL | Needs source | 「團隊將測試目標有無時的 reporter output，以及 controls 與限制。」 | 不預告結果 | 「系統必定亮紅／必定不漏訊號」 | Experimental plan；Science |
| `HG-TEAM-004` | TEAM_DATA | Needs source | 只有當資料 package 通過簽核後才填寫 | 方法、replicates、analysis、uncertainty、version、date | 從簡報圖、單次照片或遊戲 simulation 反推 performance | Team raw data＋analysis＋Science |
| `HG-TEAM-005` | TEAM_DATA | Rejected until evidence | 暫無公開 wording | 未提供校準／LOD／selectivity／response time | `detects low levels`、`rapid`、`accurate`、`selective`、`real-world ready` | Team validation required |

## 6. 教學模擬與故事原型 Claims

| Claim ID | Maturity | Candidate status | 可使用 wording／label | 必須限制 | 禁止 wording | Owner |
|---|---|---|---|---|---|---|
| `SIM-001` | TEACHING_SIMULATION | Approve with limits | 「教學模擬：數值只用來練習 controls、證據與有限主張。」 | 永久水印；圖表匯出仍保留 | 「實驗結果」或無標示圖表 | Design＋Science＋QA |
| `SIM-002` | TEACHING_SIMULATION | Approve with limits | 「訊號低／中／高」可作相對遊戲狀態 | 不給真實單位、濃度、LOD | 把 arbitrary units 當真實 calibration | Science＋Design |
| `SIM-003` | STORY_PROTOTYPE | Approve with limits | 「故事中的便攜裝置是虛構教學原型。」 | 不暗示已獲監管批准或可現場決策 | 「現場即時確認污染」 | Product＋Science＋Safety |
| `SIM-004` | STORY_PROTOTYPE | Approve with limits | 「玩家整理 evidence package，交由有權責的角色／機構判讀。」 | 玩家不是執法人員／診斷者 | 「玩家已證實河流受污染」 | HP＋Safety |
| `SIM-005` | TEACHING_SIMULATION | Approve with limits | 「near-miss 顯示過度主張可能造成的溝通與治理後果。」 | 後果是教學情境，不是對任何真實社群的預測 | 把居民描述成阻礙科學或單一態度 | Education／HP |

## 7. Aptamer／Riboswitch Claims

| Claim ID | Maturity | Status | 判定 | Sources／理由 | Public action |
|---|---|---|---|---|---|
| `APT-001` | MECHANISM | Candidate approve | Aptamer 是可摺疊並與特定 target 結合的短單鏈 DNA／RNA 辨識元件；結合可造成構形改變 | TEAM-PDF p.3；需另加合適 review | 可在概念頁使用，但不要等同完整 switch |
| `APT-002` | MECHANISM | Candidate approve with limits | 能辨識 ligand 的 aptamer domain 不自動等同能控制基因表達的完整 riboswitch | EXT-RIBOSWITCH-2013 區分 sensor 與 adjacent actuator | 可作審核修正說明 |
| `APT-003` | MECHANISM | Candidate approve with limits | 轉錄型 riboswitch 需要定義 expression／regulatory platform，例如可形成／避免 intrinsic terminator 的結構與 co-transcriptional folding context | EXT-RIBOSWITCH-2013 | 可作設計需求，不可推論 Hg²⁺ 系統已工作 |
| `APT-004` | TEAM_PROPOSAL | `NOT_APPROVED_FOR_PUBLIC_USE` | PDF p.4–5 的 `promoter → Hg²⁺ aptamer → dTomato → terminator` 未指定 actuator／terminator-switch architecture，卻描述 aptamer hairpin 在無 Hg²⁺ 時直接阻擋 transcription | TEAM-PDF p.4–5 與 EXT-RIBOSWITCH-2013 的架構要求不相符／不足 | 從 Ch1、公開遊戲、wiki／海報候選中移除，直至修訂簽核 |
| `APT-005` | TEAM_PROPOSAL | Needs source／construct | 若團隊仍要發展 Hg²⁺ aptamer 路線，需定義：aptamer identity／sequence、binding evidence、expression platform、host、promoter、RBS／terminator、switch logic、controls、co-transcriptional／translation mechanism | 目前未提供 | 只可稱 R&D question，不可稱設計完成 |
| `APT-006` | TEAM_DATA | Rejected until evidence | 無團隊數據前不可聲稱 aptamer route 有 red fluorescence、selectivity、sensitivity 或 ON／OFF ratio | 無來源 | 不公開性能 claim |

### 7.1 PDF 建議修訂文字

原 p.4–5 不宜使用「aptamer forms a hairpin right after the promoter and blocks transcription」作完整機制。候選修訂：

> 「Aptamer 可作為辨識 Hg²⁺ 的 sensor domain；要把 ligand binding 轉成 reporter output，還需把它與經驗證的 expression platform 耦合，例如控制 transcription termination 或 translation initiation 的結構。此頁為待設計／待驗證方向，並非完整 construct。」

Science Lead 仍需確認所選 Hg²⁺ aptamer 是否真有足夠來源，以及具體 switching architecture；本段不是核准任何特定序列。

## 8. Safety、權限與公共溝通 Claims

| Claim ID | Candidate status | 可使用 wording | 禁止 wording | Sources／Owner |
|---|---|---|---|---|
| `SAFE-001` | Approve with limits | 「Safety 措施降低風險，但不能保證零風險。」 | 「完全安全／零風險」 | GCP／scripts；Safety |
| `SAFE-002` | Approve with limits | 「是否部署需更多安全、效能、治理與 stakeholder evidence。」 | 「遊戲通關即表示可部署」 | GCP／scripts；Safety＋HP |
| `ROLE-001` | Approve | 「玩家是生物設計／安全調查者，負責蒐證、比較方案與提出有限建議。」 | 「玩家是監管人員／醫師／環境執法人員」 | GCP／scripts；Product＋HP |
| `ROLE-002` | Approve | 「正式污染確認、執法、清理或公共警報由有權責機構處理。」 | 「玩家按一下即可確認污染並發布警報」 | Scripts；Safety＋HP |
| `COMM-001` | Approve with limits | 「公開聲明包含 Use／Limit／Next：可用證據、限制、下一步。」 | 只有結論、無限制；恐慌式標題 | GDD／scripts；Comms＋HP |
| `COMM-002` | Approve with limits | 「不同 stakeholder 可能有合理而不同的證據需求與風險容忍。」 | 將居民／政策角色寫成無知、反科學或單一群體 | Scripts；HP |

## 9. UI 必須固定顯示的文字

下列字串應進 localization，而不是散落 hard-code：

| Locale key | zh-Hant 候選 | 使用條件 |
|---|---|---|
| `science.tag.mechanism` | 文獻機制 | 一般機制卡 |
| `science.tag.teamProposal` | 團隊設計提案（尚待驗證） | 團隊 construct／plan |
| `science.tag.teamData` | 團隊實驗資料 | 只有 approved data |
| `science.tag.storyPrototype` | 故事原型（虛構） | 裝置／故事結果 |
| `science.tag.simulation` | 教學模擬 | 所有 synthetic chart／numbers |
| `science.limit.notMeasurement` | 此遊戲不是實際汞檢測、診斷或監管工具。 | 啟動、圖表、報告 |
| `science.limit.reporterDelay` | Reporter 訊號需要表達與成熟；此處只表示相對教學狀態。 | dTomato UI |
| `science.limit.lowBackground` | OFF 代表低背景／低於教學閾值，不代表絕對零表達。 | OFF explanation |
| `science.limit.noConcentration` | 未經校準，螢光不能直接換算 Hg²⁺ 濃度。 | 圖表／claim panel |
| `science.limit.proposalNotResult` | 團隊提出此設計；尚未在本內容中證明其性能。 | team proposal |
| `science.limit.aptamerNotApproved` | 此 aptamer 路線仍需定義並驗證 expression platform。 | 只在 internal／R&D，不進 public Ch1 |

## 10. 圖表／截圖離開遊戲後的保護

每張可匯出、可截圖的圖表應在畫面內部而非 tooltip 顯示：

- Game title／build version；
- `教學模擬 / Teaching simulation`；
- maturity tag；
- units 若是 arbitrary，明寫 `相對訊號（任意單位）`；
- 不含真實濃度／LOD，除非有正式 approved data；
- `Use／Limit／Next` 或明確限制；
- Source IDs／「來源與限制」入口。

QA 必須在窄視窗、英文 Expo、截圖裁切情境確認水印仍可見。

## 11. Future Chapters：尚未完成的來源工作

第二至終章腳本已具教學設計價值，但本次 audit 沒有取得每一章所需的完整外部 source package。它們不可因腳本已寫好便被視為科學已核准。

| Claim family | 章節 | 目前狀態 | 進入生產前最低工作 |
|---|---|---|---|
| Insulin manufacturing／quality | C2 | Needs dedicated source audit | production／quality／patient safety 來源；不提供濕實驗步驟 |
| LacI／Plac switch／reporter timing | C3 | Needs dedicated source audit | construct context、reporter lifetime、temporal response、controls |
| Promoter data／statistics | C4 | Needs dedicated source audit | measurement context、controls、replicates、outliers、reproducibility |
| PET hydrolase／environment | C5 | Needs dedicated source audit | enzyme／polymer context、material composition、environmental limits、containment |
| Artemisinin／supply | C6 | Needs dedicated source audit | precursor→artemisinin→derivative／ACT pathway、manufacturing、current supply／access evidence |
| Dual-use／security | C7 | Needs Safety review | 避免可操作 misuse；禁止 identity proxy；governance／responsible communication |
| Cell-free continuous-time／latched logic | C8 | Needs dedicated source audit | sensor／time integration／latch mechanism、false positive／negative、cell-free／food-safety limits |

狀態保持 `Future／Needs source`；不加入 2026 public route。

## 12. Claim Review Workflow

1. Writer／agent 提交候選句＋Claim ID；
2. Source checker 確認來源實際支持句子的每個動詞、範圍、數字與 context；
3. Science Lead 判定 Approved／Limits／Needs source／Rejected；
4. Safety／HP／Comms 視影響 review；
5. Localization 只翻譯已核准 meaning，不擴大 certainty；
6. QA 用 automated lint 找 banned phrases／缺 maturity tag，並做畫面 review；
7. Release manifest 記錄 Claim Register version；
8. 來源、construct 或數據版本改變時，重新開啟相關 Claim IDs。

## 13. Automated Claim Lint 候選

自動檢查不能取代 Science review，但可攔截明顯漂移。

### 13.1 需人工 review 的詞

`100%｜完全安全｜零風險｜必定｜證實污染｜即時檢測｜準確濃度｜高度靈敏｜高度選擇性｜可現場部署｜診斷｜批准部署｜沒有任何表達｜works｜validated｜proven`

### 13.2 規則

- public content 含數字＋單位時必須有 Source／Claim ID；
- `TEAM_DATA` tag 必須指向 approved data package；
- simulation chart 必須含 `science.tag.simulation`；
- aptamer public route 任何文案在 `DEC-SCI-002` 未關閉時 build fail；
- `Hg++` lint 為 `Hg²⁺`；
- `dtomato／Dtomato` lint 為 `dTomato`；
- `pMER／Pmer promoter` 依 glossary 統一；
- 「沒有訊號」在機制說明中提示改為「低背景／未達教學閾值」，除非只描述 UI 顯示狀態。

## 14. 第一章公開前簽核表

| Review | 姓名 | 日期 | 決定 | Evidence／version |
|---|---|---|---|---|
| Science Lead：MerR mechanism | 待指派 | — | 待決定 |  |
| Science Lead：team construct wording | 待指派 | — | 待決定 |  |
| Science Lead：aptamer page action | 待指派 | — | 待決定 |  |
| Safety／Security | 待指派 | — | 待決定 |  |
| Education／HP：misconception／authority | 待指派 | — | 待決定 |  |
| Communications／Localization | 待指派 | — | 待決定 |  |
| QA：build tags／watermarks／banned wording | 待指派 | — | 待決定 |  |
| Product：public release scope | 待指派 | — | 待決定 |  |

## 15. 版本變更記錄

| Version | Date | Change | Author | Science approval |
|---|---|---|---|---|
| 1.0 | 2026-07-27 | 由團隊 GCP／scripts／PDF 與獨立外部機制查核建立第一章候選 register；aptamer 路線標為未核准 | Production audit | 待簽 |
