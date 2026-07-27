# 《微界工程師：生命迴路》開放決策登記

> Open Decisions Register｜版本 1.1｜日期：2026-07-27｜用途：把文件作者不能代替團隊決定的事項轉成 Owner、期限與自動縮減規則

## 0. 使用規則

本表中的「建議基線」是經審核後的**推薦預設**，不是已獲團隊批准的事實。每一項決策必須由實際姓名簽署；AI、文件作者或單一未授權開發者不能替團隊填入決定。

### 狀態

| 狀態 | 定義 |
|---|---|
| Open | 尚未作出決定；到期前需處理 |
| Proposed | 已有建議基線，但尚未進入實作鎖定，等待 Accountable Owner 核准 |
| Baseline v2.0 | 文件已選作目前實作假設，agent／開發者不得自行改動；仍須具名 Accountable Owner 正式簽核，不能當作團隊已核准 |
| Decided | 已核准，需記錄日期、理由、影響文件 |
| Deferred | 明確延後並設定重審日期；不是忘記處理 |
| Rejected | 某選項被正式否決 |
| Superseded | 被另一 Decision ID 取代 |

### 嚴重度

| 等級 | 定義 |
|---|---|
| B | Blocker；未決便不能進入相應 gate／公開 release |
| H | High；很可能造成重大返工、科學／資料／交付風險 |
| M | Medium；應在 Beta／Freeze 前處理 |
| L | Low；可依容量排程 |

### 關閉一項決策所需欄位

`Decision｜Owner name｜Approver name｜Date｜Rationale｜Evidence link｜Affected docs/tickets｜Review date`。

如未在期限前決定，必須執行「逾期預設／縮減」，不可讓 agent 自動選一個較大的方案。

## 1. G0 必須關閉的核心決策

| ID | Sev | 決策問題 | 建議基線 | Accountable | Due | 逾期預設／縮減 | Status |
|---|---|---|---|---|---:|---|---|
| DEC-GOV-001 | B | 2026 公開 P0 範圍是甚麼？ | 前導章＋第一章＋同內容 Expo 路徑 | Product Owner | 2026-08-02 | 只做前導 2D＋3–5 分鐘受控 demo | Proposed |
| DEC-GOV-002 | B | Product、Delivery、Tech、Science、Safety、Education／HP、Art、QA、AI Owner 的實際姓名與 backup？ | 按 PM 名冊指派；高風險決定至少第二人 review | Product Owner | 2026-08-02 | 未指派領域停止；不由 AI／其他人默認代管 | Open |
| DEC-GOV-003 | B | 每位成員每週可投入的有效工時？ | 只計可承諾、包含 meeting／review 的時數 | Delivery Owner | 2026-08-02 | 以已證明最低容量排程；砍 Junior、英文完整章、PWA | Open |
| DEC-GOV-004 | B | 三台目標學校設備及瀏覽器基線？ | 低／中／代表性三台；Chrome／Edge 主支援 | Tech＋QA | 2026-08-02 | 不宣稱學校設備支援；3D 範圍降級 | Open |
| DEC-GOV-005 | B | 正式科學／安全顧問能否在 Alpha、Beta、RC 簽核？ | 以書面 gate 排期 | Science／Safety | 2026-08-02 | 只公開已簽核的機制層；移除未核 claim | Open |
| DEC-GOV-006 | H | 實際 iGEM track／village、software deliverable 與外部 deadline？ | 由團隊按 2026 官方頁面確認並截圖存檔 | Product／Delivery | 2026-08-02 | 以 2026-10-21 作內部 RC hard date，不宣稱正式符合特定 track | Open |
| DEC-GOV-007 | H | 專案預算與可採購工具上限？ | 分 AI、hosting、asset、audio、testing、contingency | Product／Delivery | 2026-08-02 | 採免費／既有工具；不購買新依賴；縮減資產 | Open |
| DEC-GOV-008 | H | Repo、issue board、文件單一來源在哪裡？ | 一個受保護 Git repo＋一個 backlog | Tech／Delivery | 2026-07-30 | 不開始多 agent 寫入；只做文件／spike | Open |
| DEC-GOV-009 | H | 誰有 main merge、release、hosting、AI billing 權限？ | 最少權限；2FA；至少兩位 release backup | Product＋Tech | 2026-08-02 | 不做公開 deploy；只產生本機 build | Open |

## 2. 範圍、玩家與內容決策

| ID | Sev | 決策問題 | 選項 | 建議基線 | Accountable | Due | 逾期預設／縮減 | Status |
|---|---|---|---|---|---|---:|---|---|
| DEC-SCOPE-001 | B | Junior Mission 是否進入 2026 公開 3D build？ | 公開 3D／共用灰盒／紙面或 2D／Future | R&D：紙面／2D／共用灰盒；獨立 gate 後才升級 | Product＋Education | 2026-08-30 | Future；不進公開 RC | Proposed |
| DEC-SCOPE-002 | H | 第二至終章是否有任何 2026 實作承諾？ | 完整章／短 proof／schema only／Future | Future；最多 30–90 秒不影響 P0 的 proof | Product | 2026-08-02 | 不排程、不宣傳為可玩章節 | Proposed |
| DEC-SCOPE-003 | H | 完整第一章的目標時長？ | 18–20／24–25／其他 | 24–25 分鐘上限；Alpha 以真人計時修訂 | Design＋Product | 2026-09-14 | 砍可選說明與 S05–S08 重複段落 | Proposed |
| DEC-SCOPE-004 | H | Expo 路徑如何形成？ | 獨立內容／P0 節點抽取／影片 | 由 PRE＋C1 節點抽取，不建第二套邏輯 | Design＋Tech | 2026-08-16 | 使用受控 checkpoint＋備份影片 | Proposed |
| DEC-SCOPE-005 | M | 是否保留兩種難度／引導模式？ | Guided＋Standard／單一模式 | 共用成功條件，Guided 只改提示與導航 | Design＋QA | 2026-08-30 | 只保留 Guided，確保活動可完成 | Proposed |
| DEC-SCOPE-006 | M | 玩家 avatar 是否可自訂？ | 完整／有限／固定 | 固定中性 avatar；最多顏色選項 P1 | Design＋Art | 2026-08-09 | 固定 avatar | Proposed |
| DEC-SCOPE-007 | H | 3D 移動是否需要跳躍／平台操作？ | 有／無 | P0 無跳躍；只做 walk／turn／interact | Design＋Tech | 2026-08-09 | 無跳躍 | Proposed |
| DEC-SCOPE-008 | M | 是否做完整 VO？ | 全配音／關鍵句／無語義 VO | 無完整 VO；必要 SFX＋可選短確認音 | Product＋Art | 2026-08-16 | 無 VO，完整字幕 | Proposed |
| DEC-SCOPE-009 | M | 世界規模？ | 完整城市／hub＋多區／3 個小場景 | 河港、研究站、會議／報告三個載入單元 | Design＋Art＋Tech | 2026-08-09 | 進一步合併為 2 個場景＋DOM 報告 | Proposed |
| DEC-SCOPE-010 | M | 章末四維是否合成總分／排行榜？ | 總分／四維敘事／只記證據 | 不合成總分；不設排行榜 | Design＋Education | 2026-08-16 | 四維敘事卡＋下一步 | Proposed |

## 3. 科學、Safety 與 Human Practices 決策

| ID | Sev | 決策問題 | 建議基線 | Accountable | Due | 逾期預設／縮減 | Status |
|---|---|---|---|---|---:|---|---|
| DEC-SCI-001 | B | 第一章公開 construct 的正式表示？ | 只使用 `Pconst → merR → terminator` 與 `Pmer → dTomato → terminator`；實際序列／宿主／context 待團隊提供 | Science Lead | 2026-08-09 | 只展示抽象調控模組，不稱團隊 construct | Open |
| DEC-SCI-002 | B | 團隊 PDF 第 4–5 頁 aptamer 圖的處置？ | 修訂為「aptamer＋經驗證 expression platform 的概念方向」或撤下；不進 Ch1 | Science Lead | 2026-08-02 | 標記 `NOT_APPROVED_FOR_PUBLIC_USE` 並從公開 build 移除 | Open |
| DEC-SCI-003 | B | MerR／Pmer source package 是否足以公開？ | 至少 mechanism primary/review＋team construct source；Claim Register 簽核 | Science Lead | 2026-09-14 | 只保留低風險概念卡；不顯示 performance | Open |
| DEC-SCI-004 | H | OFF 狀態用語？ | 「低背景／低於教學閾值」，不寫絕對 zero | Science Lead＋Comms | 2026-08-16 | 使用 register 核准句 | Proposed |
| DEC-SCI-005 | H | dTomato 訊號如何表述？ | reporter 需要表達／成熟；教學中為延遲且定性；不可直接換算濃度 | Science Lead | 2026-08-16 | 不顯示濃度數字，只顯示相對 signal | Proposed |
| DEC-SCI-006 | H | 是否有任何團隊實驗數據可進遊戲？ | 只有完成來源、方法、限制、同意與 Science sign-off 的資料才可；否則全為教學模擬 | Science Lead | 2026-09-01 | 不使用團隊數據；synthetic only | Open |
| DEC-SCI-007 | H | 教學模擬水印與 maturity tag 的正式文字？ | 永久顯示「教學模擬」＋ Mechanism／Team proposal／Team data／Story prototype | Science＋Design | 2026-08-16 | 使用 GDD/TDD 預設字串 | Proposed |
| DEC-SCI-008 | H | 玩家在故事中的權責邊界是否獲顧問核准？ | 玩家可蒐證／設計／解讀／提案；不可診斷、執法、確認污染、批准部署或清理 | Safety＋HP | 2026-09-14 | 收窄角色；由 NPC 權責人作最終決定 | Proposed |
| DEC-SCI-009 | H | 對 real-world contamination／monitoring 的 disclaimer？ | 遊戲不是檢測、診斷、監管或環境處置工具 | Science＋Safety＋Comms | 2026-09-14 | 啟動畫面與圖表顯示預設 disclaimer | Proposed |
| DEC-SCI-010 | H | 是否提供 wet-lab steps、序列或可操作 protocol？ | P0 不提供；只作概念與資料判讀 | Science＋Safety | 2026-08-09 | 全部移除／改為抽象 UI | Proposed |
| DEC-SCI-011 | H | 真實 stakeholder 角色是否基於可識別個人？ | 優先 composite fictional characters；任何真實故事需同意與 review | Education／HP | 2026-08-30 | 使用虛構合成人物，不稱代表整個社群 | Proposed |
| DEC-SCI-012 | B | 中學生／Junior playtest 的同意、錄影、資料保留與地區要求？ | 書面 protocol；最少資料；預設不錄影；匿名／代碼化 | Education／Safeguarding | 2026-08-30 | 只做成人內部 heuristic；不宣稱目標玩家驗證 | Open |
| DEC-SCI-013 | M | 是否收集 free-text、語音、裝置識別或遙測？ | 公開 build 預設不收集；QA 本機匯出由測試者主動操作 | Privacy＋Tech | 2026-09-01 | 完全關閉 | Proposed |
| DEC-SCI-014 | M | 對外是否使用「sensor detects mercury」？ | 只在機制教育語境使用；團隊實作寫「proposed mercury-responsive reporter」直到有數據 | Science＋Comms | 2026-09-14 | 使用保守候選文案 | Proposed |

## 4. 技術架構決策

| ID | Sev | 決策問題 | 選項 | 建議基線 | Accountable | Due | 逾期預設／縮減 | Status |
|---|---|---|---|---|---|---:|---|---|
| DEC-TECH-001 | B | Package manager？ | npm／pnpm／bun | npm；commit `package-lock.json`；整個 repo 只用一個 | Tech Lead | 2026-07-30 | npm＋lockfile | Baseline v2.0 |
| DEC-TECH-002 | B | UI framework？ | Preact／React／原生 DOM | Preact＋semantic DOM；UI reactive state 用 `@preact/signals`；G1 只驗證維護性，失敗則保留 contracts 改原生 DOM | Tech Lead | 2026-08-02 | 原生 DOM custom elements，保持 contracts | Baseline v2.0 |
| DEC-TECH-003 | B | 3D engine／版本？ | Three.js 直接使用／其他 | TypeScript strict＋Vite＋Three.js，鎖版本 | Tech Lead | 2026-07-30 | Three.js；不轉引擎 | Baseline v2.0 |
| DEC-TECH-004 | H | 角色碰撞是否使用 Rapier？ | Rapier／simple capsule-AABB | 只在 2 日 spike 通過 WASM、樓梯／斜坡、bundle、reset 後使用 | Tech Lead | 2026-08-09 | simple kinematic controller；無動態物理 | Proposed |
| DEC-TECH-005 | H | Content data 格式與 validator？ | JSON＋schema／TS literals／CMS | versioned JSON／TS data＋Zod；build-time validation，runtime 只讀已驗證資料 | Tech Lead＋Design | 2026-08-09 | TS typed fixture，仍需 validator before content scale | Baseline v2.0 |
| DEC-TECH-006 | H | State machine 實作？ | 自製 typed reducer／library | 小型 typed reducer＋explicit transition table；不加大型狀態機依賴 | Tech Lead | 2026-08-16 | 自製 reducer＋unit tests | Baseline v2.0 |
| DEC-TECH-007 | H | Save 儲存位置？ | localStorage／IndexedDB／file export | versioned localStorage summary＋JSON 匯入／匯出；不存大型 world snapshot | Tech Lead | 2026-08-16 | localStorage versioned save；無大型快照 | Baseline v2.0 |
| DEC-TECH-008 | H | Save schema、migration、corrupt recovery owner？ | 版本化＋fixtures | TDD 基線；任何 schema change 獨立 ticket | Tech＋QA | 2026-08-16 | 只存 chapter/checkpoint/settings，刪除細節狀態 | Proposed |
| DEC-TECH-009 | H | Backend／帳號？ | 有／無 | 無 backend、無 account、無雲端存檔 | Product＋Tech | 2026-08-02 | 無 | Baseline v2.0 |
| DEC-TECH-010 | H | PWA 是否進 P0？ | P0／P1／不做 | 不進 P0；Beta gate 後才可作 P1；先可靠 static build＋offline zip | Tech＋QA | 2026-09-28 | 2026 build 不啟用 service worker | Baseline v2.0 |
| DEC-TECH-011 | H | Hosting provider／domain／HTTPS？ | 待選 | 靜態 hosting＋staging／prod＋cache control＋rollback | Tech＋Product | 2026-09-01 | 使用 iGEM／學校核准靜態 hosting；同時交 offline zip | Open |
| DEC-TECH-012 | M | Browser support matrix？ | Chrome／Edge P0；Firefox best effort；Safari／tablet P1 | 按 GDD 基線 | Tech＋QA | 2026-08-09 | 只列 Chrome／Edge desktop 為支援 | Proposed |
| DEC-TECH-013 | H | Touch／tablet 是否公開支援？ | P0／P1／不宣稱 | P1；必須有 touch UX 與實機 playtest | Product＋QA | 2026-09-14 | 不列支援 | Proposed |
| DEC-TECH-014 | H | Performance budgets 是否接受？ | shell ≤3 MB；PRE +≤5 MB；C1 +≤25 MB；cached ≤35 MB；30 FPS baseline | 接受 TDD 基線，G1 用裝置校正 | Tech＋Art＋QA | 2026-08-09 | 按基線；超出即砍材質／場景／音訊 | Proposed |
| DEC-TECH-015 | M | 3D quality tiers？ | auto low／medium／high | Low／Medium；自動偵測只作建議，使用者可改 | Tech＋Art | 2026-08-30 | 預設 Low；不做 High | Proposed |
| DEC-TECH-016 | M | Error／crash reporting？ | 遙測／本機 log／無 | 本機 structured QA log，可手動匯出 | Tech＋Privacy＋QA | 2026-08-30 | console＋本機下載；不傳網路 | Proposed |
| DEC-TECH-017 | M | CI provider 與 required checks？ | GitHub Actions／其他 | format、lint、typecheck、unit、content validation、build、link check | Tech＋QA | 2026-08-02 | 無 CI 不允許 agent merge | Proposed |
| DEC-TECH-018 | M | Dependency license allowlist？ | permissive only／case-by-case | production 優先 MIT／BSD／Apache-2.0；copyleft／未知個別審核 | Tech＋License | 2026-08-16 | 不加入未知或衝突 dependency | Proposed |
| DEC-TECH-019 | M | 是否使用 runtime remote CDN／第三方字型？ | 有／無 | P0 自帶必要檔案；無 runtime third-party dependency | Tech＋Art | 2026-08-16 | 全部 self-host | Proposed |
| DEC-TECH-020 | M | Analytics／feature flag？ | 有／無 | 無 public analytics；只用 build-time flags；production fail closed | Product＋Privacy＋Tech | 2026-09-01 | 關閉 | Baseline v2.0 |

## 5. UX、可及性與本地化決策

| ID | Sev | 決策問題 | 建議基線 | Accountable | Due | 逾期預設／縮減 | Status |
|---|---|---|---|---|---:|---|---|
| DEC-UX-001 | H | Canonical language？ | 繁體中文 `zh-Hant` | Product＋Comms | 2026-08-02 | zh-Hant only，保留 locale keys | Proposed |
| DEC-UX-002 | H | 英文範圍？ | 核心 UI＋3–5 分鐘 Expo；完整 C1 由 Alpha capacity gate 決定 | Product＋Comms | 2026-09-14 | 只做 Expo＋啟動／設定／disclaimer | Proposed |
| DEC-UX-003 | H | 科學術語表由誰核准？ | Science＋Localization 建立 bilingual glossary | Science＋Comms | 2026-08-30 | 不擴充完整英文；使用已核 glossary | Open |
| DEC-UX-004 | H | 3D 關鍵任務的非精準導航 fallback？ | objective list、interaction list、guided path、safe-node teleport | Design＋Accessibility | 2026-08-30 | 全部使用 interaction list／Guided target lock；不要求搜尋或操作鏡頭 | Proposed |
| DEC-UX-005 | H | 鍵盤／焦點規格？ | 完整鍵盤、可見焦點、modal trap／return、canvas escape | QA／Accessibility＋Tech | 2026-08-16 | 未通過不得 Alpha | Proposed |
| DEC-UX-006 | M | Motion／camera settings？ | fixed perspective isometric-like；隨位置平移、不跟隨面向；reduced motion；look-ahead on/off；focus cut/fade；無 sensitivity／invert／player zoom | Design＋QA | 2026-08-30 | 保持固定鏡頭；只調 level／cutaway／offset profile | Baseline v2.0 |
| DEC-UX-007 | M | 字級／閱讀量／延伸資訊？ | critical path 短句；延伸內容收合；可調 UI scale | Design＋Education | 2026-09-14 | 刪除非必要長文，保留來源頁 | Proposed |
| DEC-UX-008 | M | Screen reader 宣稱？ | DOM UI 可讀；不宣稱可完整操作 3D canvas；提供 guided alternative | Accessibility＋Comms | 2026-10-11 | 使用準確限制聲明 | Proposed |
| DEC-UX-009 | M | 色覺與非色彩編碼？ | 紅光同時有圖示、文字、pattern／數值類別 | Art＋QA | 2026-09-14 | 不以顏色作唯一訊號 | Proposed |
| DEC-UX-010 | M | Session reset／展覽模式？ | 一鍵清空 session、固定 checkpoint、無個資 | Tech＋QA＋Expo Owner | 2026-09-14 | 每輪重新載入受控 build＋清除 save | Proposed |

## 6. 資產、品牌與授權決策

| ID | Sev | 決策問題 | 建議基線 | Accountable | Due | 逾期預設／縮減 | Status |
|---|---|---|---|---|---:|---|---|
| DEC-ASSET-001 | H | 視覺風格與可製作 benchmark？ | 低多邊形／stylized、清楚 silhouette、有限材質、非寫實 | Art Lead | 2026-08-09 | 使用灰盒＋簡單自製材質 | Open |
| DEC-ASSET-002 | H | P0 NPC／角色數？ | 1 avatar＋5–6 NPC，共用 skeleton | Art＋Design | 2026-08-09 | 1 avatar＋3 NPC；以 portrait／DOM 取代其餘 | Proposed |
| DEC-ASSET-003 | H | Blender→GLB exporter、scale、axis、compression？ | 固定版本與 preset；自動檢查 | Art＋Tech | 2026-08-09 | 靜態 GLB、少材質、無複雜動畫 | Open |
| DEC-ASSET-004 | M | 字型？ | 支援繁中／英文、可 self-host、授權清楚、可讀 | Art＋License | 2026-08-16 | 系統字型 stack | Open |
| DEC-ASSET-005 | M | 音樂／SFX 來源？ | 原創或清楚可再散布授權；保留 attribution | Audio／Art | 2026-09-01 | 無音樂；只用自製／核准 SFX | Open |
| DEC-ASSET-006 | H | AI 生成資產是否允許公開？ | 允許 concept／placeholder；公開需 provenance、權利、相似性 review | Product＋Art＋License | 2026-08-16 | 公開 build 只用自製或明確授權資產 | Proposed |
| DEC-ASSET-007 | H | iGEM／學校／隊伍／合作方 logo 使用權？ | 依正式品牌規範與書面批准 | Comms＋License | 2026-09-14 | 移除未核 logo／商標 | Open |
| DEC-ASSET-008 | M | 真實河港／社區外觀是否可辨識？ | 使用 fictional composite；不暗示實際污染地點 | HP＋Art | 2026-08-30 | 去識別、改名、改地標 | Proposed |
| DEC-ASSET-009 | M | Credits／license manifest 格式？ | Asset ID、creator、source、license、changes、AI provenance | Art＋QA | 2026-08-30 | 未有記錄的 asset 不進 build | Proposed |
| DEC-ASSET-010 | M | 完整配音／人聲同意與補償？ | P0 無完整 VO；任何錄音先書面同意與使用範圍 | Product＋Art | 2026-09-01 | 無人聲 | Proposed |

## 7. QA、研究、Release 與公開交付決策

| ID | Sev | 決策問題 | 建議基線 | Accountable | Due | 逾期預設／縮減 | Status |
|---|---|---|---|---|---:|---|---|
| DEC-QA-001 | B | Alpha／Beta／RC gate 的實際 approver？ | Product 決定、QA recommendation、Science／Safety 專項 veto | Product＋QA | 2026-08-16 | 未指派不進 gate | Open |
| DEC-QA-002 | B | P0 支援裝置／瀏覽器的 pass criteria？ | 三台 baseline；Chrome／Edge；30 FPS；無 blocker crash | Tech＋QA | 2026-08-09 | 只在已通過裝置公開展示 | Open |
| DEC-QA-003 | H | 中學生 Alpha playtest 招募量？ | 5–8 名目標年齡＋2–3 名 facilitator／teacher review | Education＋QA | 2026-08-30 | 小範圍成人 usability only；降低驗證 claim | Open |
| DEC-QA-004 | H | Junior gate 的獨立樣本？ | 5–8 名 P4–P6＋教師；不能用中學生代替 | Education | 2026-08-30 | Junior 保持 Future／R&D | Proposed |
| DEC-QA-005 | H | Bug severity 與 release threshold 是否採 QA plan？ | RC：0 Blocker、0 High；Medium 需接受紀錄 | QA＋Product | 2026-09-14 | 不發公開 RC | Proposed |
| DEC-QA-006 | H | Science misconception test 的通過標準？ | 不把模擬當實驗、不把 reporter 當即時濃度、不把 proposal 當 result | Science＋Education＋QA | 2026-09-14 | 改寫／刪除誤導節點 | Proposed |
| DEC-QA-007 | H | Accessibility release claim？ | 描述已測功能與已知限制；不自稱完整 WCAG conformant 除非正式 audit | QA／Accessibility＋Comms | 2026-10-11 | 使用 feature-based statement | Proposed |
| DEC-QA-008 | H | Offline package 與 rollback owner？ | versioned zip、checksum、fresh install、previous RC | Tech＋QA | 2026-10-11 | 不依賴網路 live demo；保留影片 | Open |
| DEC-QA-009 | H | Public source／software license？ | 依 iGEM deliverable 與資產相容性選；code／content／assets 分開 | Product＋License＋Tech | 2026-09-14 | 不公開未知權利資產；code 只在核准後 release | Open |
| DEC-QA-010 | M | Repository 是否公開？何時？ | Beta 後 cleanup＋secret／license scan | Product＋Tech | 2026-10-11 | 私有 repo＋提交必要 deliverable／source archive | Open |
| DEC-QA-011 | M | Jamboree demo 的 fallback 層級？ | live static／offline zip／錄影／screenshots 四層 | Expo Owner＋Tech＋QA | 2026-10-21 | 使用已驗證 offline RC＋影片 | Proposed |
| DEC-QA-012 | M | Post-release support 到何時？ | 至 2026-11-16；只修 blocker／high | Product＋Tech＋QA | 2026-10-21 | 凍結 RC，不加功能 | Proposed |
| DEC-QA-013 | M | 教師／facilitator guide 是否 P0？ | 1–2 頁 quick guide P0；完整 curriculum P1 | Education＋Comms | 2026-09-28 | 只做 demo 操作卡＋learning limits | Proposed |
| DEC-QA-014 | M | Public feedback channel？ | 不收未成年人 free text；使用受監督 contact／event notes | Product＋Privacy | 2026-10-11 | 不在遊戲內收集 | Proposed |

## 8. AI 工具、資料與成本決策

| ID | Sev | 決策問題 | 建議基線 | Accountable | Due | 逾期預設／縮減 | Status |
|---|---|---|---|---|---:|---|---|
| DEC-AI-001 | B | 誰是 AI Steward，誰可批准模型／tool？ | 指派一位主責與 Tech backup | Product＋Tech | 2026-08-02 | 只允許人類手動編輯；不開自動 write agent | Open |
| DEC-AI-002 | H | 月度／總 AI budget？ | 設 provider 分項、單 ticket cap、警報 | Product＋AI Steward | 2026-08-02 | 只保留既有訂閱；每次 agent work 先批准 | Open |
| DEC-AI-003 | H | 主要日常工具？ | 一個主要互動工具＋一個獨立 review 路徑 | Tech＋AI Steward | 2026-08-02 | Cursor／IDE 手動＋單一核准 agent；禁止多工具同時寫同模組 | Open |
| DEC-AI-004 | B | 各 provider 可處理哪些資料等級？ | 依 Playbook D0–D3；逐一記 retention／training／region | Safety／Privacy＋AI Steward | 2026-08-02 | 只送 D0 公開資料；D1–D3 不送 | Open |
| DEC-AI-005 | H | Claude Fable 5 的 30 日保留是否可接受？ | 只有 D0／核准 D1；不送未公開序列、個資、研究資料 | Privacy＋Science | 2026-08-02 | 不用 Fable 處理限制資料 | Open |
| DEC-AI-006 | H | Kimi K3 是否進日常 workflow？ | 先驗證權重／API／license／retention／cost，再跑 AI-E01–E06 | Tech＋AI Steward＋Security | 2026-08-16 | R&D only；不成為 P0 相依 | Proposed |
| DEC-AI-007 | H | 是否嘗試本地 K3／大型模型部署？ | 不列 P0；先做硬體／運維／能源／license feasibility | Tech Lead | 2026-08-16 | 不做；使用核准 API／較小模型 | Proposed |
| DEC-AI-008 | H | Agent 可否安裝 dependency／上網／部署？ | 預設否；按 task 明確批准；production dependency／deploy 需人類 | Tech＋Security | 2026-08-02 | 只讀＋repo 內寫入＋既有 command | Proposed |
| DEC-AI-009 | H | `AGENTS.md` 是否作唯一規則源？ | 是；CLAUDE／Cursor adapters 不分叉 | Tech＋AI Steward | 2026-07-30 | agent 暫停 write mode直到規則提交 | Proposed |
| DEC-AI-010 | M | AI-assisted PR 如何記錄？ | 使用 Playbook notice：tool／model／date／data class／human reviewer | AI Steward＋QA | 2026-08-02 | 未記錄不 merge | Proposed |
| DEC-AI-011 | M | 多 agent 最大並行？ | 依 human review capacity；預設最多 2 個 write agent，且不同 module | Tech＋Delivery | 2026-08-09 | 1 個 write agent | Proposed |
| DEC-AI-012 | M | 獨立 review 是否需不同 provider？ | High-risk 優先不同 provider＋human；一般至少不同 session | Tech＋QA | 2026-08-09 | 人類 review＋CI；作者 agent 不自批 | Proposed |
| DEC-AI-013 | H | AI 資產／文字 provenance 欄位？ | 採 Asset Guidelines／Playbook minimum record | Art＋AI Steward | 2026-08-16 | 未記錄不公開 | Proposed |
| DEC-AI-014 | H | Prompt／session log 保存多久、放哪裡？ | 只保存必要摘要／decision／run metadata；不保存 secrets／D3 | Privacy＋AI Steward | 2026-08-16 | 不集中保存 raw prompts；PR notice only | Open |
| DEC-AI-015 | M | Model mini-eval 的 winner／fallback？ | 用 AI-E01–E06 比較 correctness、review time、cost；每月重看 | Tech＋QA＋AI Steward | 2026-08-16 | 不鎖定單一 frontier model；逐 ticket 人工選擇 | Open |
| DEC-AI-016 | H | Agent incident response owner？ | Security／AI Steward；credential revoke、provider deletion、rollback | Safety／Security | 2026-08-09 | 發生事件即關閉 agent access | Open |

## 9. 已建議但尚未正式簽核的設計基線

這些決定已寫入 GDD／TDD／PM／QA 作可執行 baseline。標成 `Baseline v2.0` 的項目不可由 agent／個別開發者自行更換，但在實際 Owner 簽署前仍不等於團隊正式核准；Rapier、PWA 啟用、hosting、裝置效能等仍按表中狀態處理：

| Baseline ID | 內容 | 對應 Decisions |
|---|---|---|
| BASE-01 | P0 = PRE＋C1＋Expo | DEC-GOV-001、DEC-SCOPE-001～004 |
| BASE-02 | zh-Hant canonical；英文先做 Expo | DEC-UX-001～003 |
| BASE-03 | npm＋TypeScript strict＋Vite＋Three.js＋Preact／Signals＋Zod；Rapier 僅是可替換 spike | DEC-TECH-001～006 |
| BASE-04 | 無跳躍、無 backend、無 public telemetry | DEC-SCOPE-007、DEC-TECH-009、016、020 |
| BASE-05 | PWA Beta-only；static＋offline zip first | DEC-TECH-010～011、DEC-QA-008 |
| BASE-06 | aptamer 暫不公開；MerR 主線需 source／claim sign-off | DEC-SCI-001～007 |
| BASE-07 | Agent 採 task packet、protected paths、independent review | DEC-AI-001～016 |

## 10. 決策紀錄範本

```markdown
### <DEC-ID> — <Decision title>

- Status: Decided / Deferred / Rejected
- Decision date:
- Accountable owner:
- Approver(s):
- Context:
- Options considered:
- Decision:
- Rationale:
- Evidence / spike / source:
- Consequences and trade-offs:
- Affected docs / tickets / assets:
- Effective version / build:
- Review date / trigger:
```

## 11. 每週決策清理

Delivery Owner 每週檢查：

- 7 日內到期項；
- 已逾期但未執行 fallback 的項；
- 已在 code／宣傳中被默認、但 register 仍 Open 的項；
- AI／供應商／iGEM 外部資訊是否變更；
- 決定是否已同步到 GDD、TDD、PM、QA、AGENTS、Claim Register；
- `Decided` 是否有真實姓名、證據與日期。

**禁止做法：** 把 `Proposed` 當作「已批准」、把會議口頭意見當作 close、把 agent 的選擇當作團隊決定，或在 deadline 過後仍保留較大範圍而不執行縮減。
