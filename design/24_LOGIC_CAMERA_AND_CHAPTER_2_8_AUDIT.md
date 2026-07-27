# 《微界工程師：生命迴路》邏輯、固定斜俯視鏡頭與第二至第八章審核

> Independent Logic / Camera / Chapter 2–8 Audit｜版本 1.1｜日期：2026-07-27｜狀態：**已修正文件內部矛盾；仍待具名人類與實機驗證**

## 1. 審核問題

本輪回答四個問題：

1. 文件中是否仍有無效、不合邏輯、違反常識或互相矛盾的內容？
2. 玩家鏡頭是否真正是 Hades／Diablo 類固定斜俯視構圖，而不是肩後跟隨／自由相機？
3. 第二至第八章是否已在 GDD／TDD 留下足以拆 issue、建 schema、寫測試的腳本與技術契約？
4. 文件是否把「已寫設計」誤說成「已完成 production／科學核准」？

審核範圍為整個 production pack，包括 GCP、GDD、TDD、Asset、PM、QA、PRE、C1–C8、Junior、continuity、兩份舊 audit、AI Playbook、Decision Register、Claim Register、AGENTS 及團隊 PDF。

## 2. 整體裁決

**修正後可作開發基線，但不能作公開發行批准。** 最重要的設計決定已一致：

- 2026 P0 = PRE＋C1＋Expo；C2–C8 是 Future Design Bible，不進 production bundle／manifest／P0 QA。
- 3D 探索使用固定斜俯視**透視**鏡頭。它會隨玩家位置平移，否則玩家會走出畫面；但不跟隨角色面向、不繞到背後、不提供旋轉／俯仰／縮放，因而不是常見肩後 following camera。
- GDD scene script、canonical chapter script、TDD contract 三層已建立明確權威順序和 source mapping。
- 所有教學模擬、團隊 proposal、文獻機制與團隊實測資料仍分層；結構 validator 通過不等於科學正確、遊戲可玩或已可公開。

## 3. 主要發現與修正

| ID | 發現 | 為何不合理／風險 | 修正後規格 | 狀態 |
|---|---|---|---|---|
| AUD-001 | 舊文件同時含固定斜俯視、肩後與自由鏡頭概念 | 同一關卡無法同時為固定角度遮擋與任意角度資產製作；QA matrix 失控 | 全部統一 `IsometricPerspectiveRig` | Closed |
| AUD-002 | 「不跟隨相機」可能被誤解為鏡頭完全不移動 | 玩家會走出視野，不符合 Hades／Diablo 類常識 | 明定隨**位置**平移，不隨**面向**旋轉 | Closed |
| AUD-003 | GDD／TDD C2–C8 flags 與完整腳本不一致 | runtime gate、save、QA 和內容作者會各用一套名稱 | 逐章對齊 canonical flags；invented flags 移除 | Closed |
| AUD-004 | C6 有 flag 定義但無 set event | 正常流程可能永久鎖在 S01 | 完成兩條鏈後 set `c6_chain_valid`，否則 S02 locked | Closed |
| AUD-005 | C3 用「表達先停止」作絕對敘述 | 不符合一般時間動態與腳本自身的延遲前提 | 改為新產生／轉錄輸出開始下降，整體依反應窗回低 | Closed |
| AUD-006 | C8 的 D 看似可被當成獨立 input | 玩家可造出物理上矛盾狀態；timer 亦可能受 tab suspension 影響 | D 只由 T 的連續時間派生；fixed simulation step；非法組合只供 QA | Closed |
| AUD-007 | Junior 以 40% 時間配額判定 3D | 會誘導無意義走路，不能證明學習 | 每個 learning gate 必須有有意義操作；保留 3D 由 transfer／usability 實測決定 | Closed |
| AUD-008 | WebGL2 fallback 暗示有完整 2D 遊戲 | 沒有設計、資產、QA 或工期支持 | 只承諾來源／逐字稿／靜態摘要／預錄 walkthrough 或受控 demo | Closed |
| AUD-009 | 技術 stack 一處「鎖定」、一處仍 Proposed | agent 可能擅自換 framework；或文件假裝已有批准 | 新狀態 `Baseline v2.0`：禁止自行改，但仍待具名 Owner 簽核 | Closed |
| AUD-010 | 舊 script audit 宣稱 0 finding | 與實際發現矛盾，容易被誤作 release approval | `16_FULL_SCRIPT_REVIEW_AUDIT.md` v2.0 明確 supersede v1.2 | Closed |
| AUD-011 | 舊文案把 API／consumer service 可用、官方「open model」描述與完整權重 artifact 混成同一狀態 | 會把尚未核對的權重、license、commit 與部署可行性寫成既成事實 | 改為：服務／API 已可用；官方頁面仍列 2026-07-27 權重釋出時點；本審核未獨立確認確切 artifact／license／package | Closed |
| AUD-012 | 原總時長上限比逐章加總少 1 分鐘 | 常識性算術錯誤影響 scope | 統一 192–203 | Closed |
| AUD-013 | GDD 風險表曾寫 `point-and-click fallback` | 與 TDD「不做 click-to-move／pathfinding」衝突，agent 可能誤做第二套導航 | 改為 target cycle、interaction list、safe-anchor reset、點擊已高亮互動物；明確不做 click-to-move | Closed |
| AUD-014 | 「學校網路」load target 沒有可重現 profile | 不同測試者可用任意網路宣稱達標，C1 25 MB 首次下載亦無時間界線 | 新增 `10 Mbps down／2 Mbps up／100 ms RTT` cold-cache Lab profile、真實學校現場 run、C1 cold-route ≤30 s／progress／cancel／retry 契約，以及對應 QA-PERF-006／QA-NET-001 | Closed |
| AUD-015 | GDD／Source Register 仍有舊 `TEAM-GCP-1.3`／`TEAM-CONTINUITY-1.2` | 來源追溯會指向錯版本，與 canonical scripts 不一致 | 更新為 `TEAM-GCP-1.4`、`TEAM-CONTINUITY-1.3`，並加入 validator 禁止舊 ID | Closed |
| AUD-016 | C2–C6 完整腳本未明寫章末 profile transaction | GDD／TDD／continuity 有 profile writes，但內容作者只讀單章腳本時可能漏寫或在中途覆寫 | 各章新增原子寫入條件、source flag→profile key mapping，以及未完成重玩不得覆寫規則 | Closed |

## 4. 固定斜俯視鏡頭最終契約

### 4.1 視覺與行為

| 項目 | 基線 |
|---|---|
| 投影 | Three.js `PerspectiveCamera`；isometric-like，不是 true orthographic |
| 世界 yaw | `45°` fixed |
| 向下角 | 約 `50°` fixed |
| 高度／地面水平 offset | 約 `12 m`／`10 m`；可按 zone profile 微調，但不改控制框架 |
| Vertical FOV | baseline `40°`；authored tested range `38–44°` |
| 玩家畫面位置 | normalized viewport Y `0.58`，其中 0=top、1=bottom |
| 平移平滑 | half-life `0.20 s` |
| 移動預視 | `0–0.9 m`，玩家可關閉；只改 target translation |
| authored focus | `0.35–0.60 s`；可由移動／Back 取消；reduced motion 改 cut／fade |
| 角色與相機 | 角色朝移動方向轉；相機 yaw／pitch 不跟著轉 |
| 玩家相機輸入 | 無 rotate、pitch、zoom、sensitivity、invert、mouse-look、Q/E rotate |
| Debug | `DebugFreeCam` 只在 dev／QA，production tree-shaken／不可達 |

### 4.2 移動與互動

- `W／↑` 永遠朝螢幕上方；輸入由固定 camera basis 投影至 world XZ。
- Pointer 可選已註冊／高亮互動物，但 P0 不做 click-to-move 或 pathfinding。
- 候選互動依世界距離、投影畫面接近度、quest priority、可見／可達與 accessibility target lock 排序；不依角色面向或 view cone。
- Guided／keyboard-only 模式提供 interaction list 和 target cycle；關鍵任務不要求玩家精準點 3D 像素。
- 遮擋先靠 level layout；再用 roof／wall cutaway 與 `CameraOccluder` fade。禁止 camera boom push-in、突然貼近、旋轉到角色背後。
- 關鍵走廊淨寬目標 `≥1.8 m`；720p、200% UI、字幕與低階畫質都要實機驗證。

## 5. 第二至第八章腳本／技術對齊

| Chapter | Canonical flags 摘要 | 已修正的關鍵邏輯 | P0 狀態 |
|---|---|---|---|
| C2 | cells/product、process order、4 quality、batch/root cause、statement、access | Q-17 入場前已隔離；Q-18 不追溯放行；玩家不作正式放行 | Future only |
| C3 | expected behavior、2 faults、repair、truth table、failure reported | output 依反應窗下降，不是瞬時 OFF | Future only |
| C4 | prior repair、question、controls、replication、follow-up、outlier、conclusion、package | 全 raw points 可總覽；walking optional；controls 不取代 replication | Future only |
| C5 | release rejected、scope、pathways、contained strategy、ladder、lifecycle、statement | PET scope 具材料情境；HGT 可能但非必然 | Future only |
| C6 | missing people、chain、shock、metrics、strategy、transition、statement | precursor／artemisinin／derivative／ACT 分開；合作社確認才寫 package | Future only |
| C7 | risk dimensions、3 cases、access controls、incident、public summary | 身分不作 proxy；hold 不等於惡意指控 | Future only |
| C8 | problem、stakeholders、comparison、latched time、controls、edge、quality、access/open、architecture/pilot/statement | D derived from continuous T；no-pilot 合法；聲明須與架構一致 | Future only |

完整 scene scripts 位於 GDD 9.4；技術 route／schema／fixture／transaction 位於 TDD 9.8；逐句對白和 Choice ID 仍在 `08_...` 至 `14_...`。

## 6. 現行技術基線

| 領域 | 基線 | 邊界／尚待驗證 |
|---|---|---|
| Runtime | TypeScript strict、Vite、Three.js | 實際 package versions 由 repo lockfile 固定 |
| UI | Preact＋`@preact/signals`＋semantic DOM | G1 維護性 spike；失敗可改原生 DOM但保留 contracts |
| Validation | Zod＋build-time content checks | production 不解析 Markdown；claim family 未核准 fail closed |
| State | typed reducer／explicit transition table | 不加大型狀態機 dependency |
| Physics | kinematic capsule；Rapier adapter spike | Rapier 失敗改 simple custom capsule/AABB；無 jump／dynamic physics |
| Save | versioned localStorage summary＋JSON import/export | 不存每幀、camera transform 或大型 world snapshot |
| Test | Vitest、Playwright、axe＋manual device／science／usability | 仍需三台學校機與真人 playtest |
| Deployment | client-only static；無 backend、account、cloud save、public analytics | hosting／base path 未決；PWA 是 P1／Beta gate；offline zip P0 |
| Unsupported WebGL2 | notice＋sources/transcript/static summary/video／controlled demo | 不稱為等價 2D 遊戲 |

## 7. 生物迴路審核邊界

團隊 PDF 第 1–2 頁支持一個兩轉錄單元 proposal：`Pconst → merR → terminator` 與 `Pmer → dTomato → terminator`；遊戲因此只可把它稱為團隊提出的汞響應 reporter 設計，並以低背景、Hg²⁺ 依賴增加、延遲且定性的 dTomato 教學訊號呈現。PDF 第 4–5 頁所畫的「promoter 後放一個 aptamer hairpin 便阻擋／恢復轉錄」沒有提供完整 expression platform／actuator、宿主、序列架構、controls 或數據，所以仍是 `NOT_APPROVED_FOR_PUBLIC_USE`。文件沒有替團隊補寫這些空缺。

## 8. 仍開放的真實風險

這輪只能關閉文件內部邏輯，不能關閉下列現實問題：

- MerR／Pmer construct、宿主、序列、背景、反應時間、選擇性、matrix effect、LOD／LOQ 與安全資料；
- 目標玩家是否理解 signal≠concentration≠confirmation≠cleanup；
- 固定鏡頭在三台學校機、720p、200% UI、低階 GPU 下的遮擋、暈動、FPS、memory 與 input；
- Preact、Rapier、字型、GLB pipeline、offline package、hosting、PWA update／rollback 的實作 spike；
- 資產、AI 生成內容、字型、音訊、商標與第三方 dependency license；
- 未成年人招募、同意、錄影、資料保存及公開 feedback 的 safeguarding／privacy；
- iGEM 2026 當期要求、截止日與公開提交格式。

## 9. 驗證邊界

`tools/validate_production_pack.py` 檢查檔案、連結、表格、ID、budget、PDF 和 checksum；`tools/validate_v2_logic.py` 檢查固定鏡頭 token、C2–C8 canonical flags、禁止舊名稱、Future build exclusion、版本與決策狀態。兩者的 0 errors 只代表文件結構及已編碼邏輯一致，**不代表科學批准、可玩性、效能、可及性 conformant、產品完成或 release ready**。
