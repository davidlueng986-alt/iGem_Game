# 《微界工程師：生命迴路》Quality Assurance & Test Plan

> 版本 1.0｜狀態：P0 測試基線候選｜日期：2026-07-26

| 文件欄位 | 內容 |
|---|---|
| 專案代號 | `MCE-LC-2026` |
| QA Owner | QA／Accessibility Lead（待指派姓名） |
| 目標 Build | Pre-Chapter＋Chapter 1＋Exhibition Mode |
| 測試原則 | 風險優先、需求可追溯、真實裝置、科學誤解、可恢復、人工＋自動 |
| Release 權責 | QA 提出建議；Product 作發行決定；Science／Safety 可阻擋未核准內容 |

## 修訂與核准

| 版本 | 日期 | 變更摘要 | QA | Tech | Design | Science／Safety | Education／A11y |
|---|---|---|---|---|---|---|---|
| 1.0 | 2026-07-26 | 完成功能、非功能、科學、可及性、研究、automation、release plan | 待簽 | 待簽 | 待簽 | 待簽 | 待簽 |

---

## 1. 目的與範圍

### 1.1 品質目標

品質不只指「沒有程式 bug」。本產品的主要失敗模式包括：玩家完成不了、低階電腦跑不動、存檔丟失、鍵盤／視覺／動態障礙、對照失敗仍能下結論、把螢光當汞或把感測當清理、居民意見不改變設計、模擬被宣傳成實驗數據、AI／第三方資產來源不清。因此 QA 同時驗證功能、科學、教育、責任、可及性、私隱、授權、效能和展覽可靠性。

### 1.2 In Scope

- P0 支援瀏覽器／裝置、boot、settings、3D navigation、all DOM screens；
- PRE S00–S05、C1 S00–S08、standalone、replay、Expo；
- quest／dialogue／evidence／circuit／test／safety／claim／report；
- save／migration／recovery／import／export／reset；
- localization、keyboard、zoom、motion、subtitles、screen-reader smoke；
- deterministic simulation、claims、misconception、safety boundaries；
- performance、bundle、memory、loading、offline、optional PWA；
- content／asset／license／dependency validation；
- target-player usability／learning evidence and research ethics；
- release、deployment、rollback、demo rehearsal。

### 1.3 Out of Scope

- 第二至終章 production QA；
- Junior public-release QA unless separate gate approves；
- 真實生物 assay／clinical／environmental validation；
- penetration test of nonexistent backend；
- full certification against a named accessibility standard before qualified audit；
- unsupported phone／old browser；
- proving long-term educational retention from small formative samples。

### 1.4 假設與限制

| ID | Limitation | QA Response |
|---|---|---|
| QL-01 | Team／device／participant details尚未提供 | G0前填入；否則不建議公開支援／效果claim |
| QL-02 | Small high-school test capacity | risk-based P0 suite；automation focus on deterministic domains |
| QL-03 | WebGL visual automation不完全穩定 | semantic hooks＋selected screenshots＋physical device manual |
| QL-04 | A11y automation只抓部分問題 | keyboard、zoom、screen reader、motion manual required |
| QL-05 | Science efficacy尚未實測 | 只驗證正確成熟度與禁止claim，不驗證產品性能 |
| QL-06 | AI工具輸出可變 | tests與acceptance固定；AI不能自報完成 |

### 1.5 相關文件

GDD、TDD、Asset Guidelines、PM、AI Playbook、[Source & Claim Register](22_SOURCE_AND_CLAIM_REGISTER.md)、PRE／C1 scripts、continuity、Independent Audit。Test cases引用 requirement／claim／scene IDs；若文件衝突，先凍結相關測試並按README權威順序決定。

## 2. 品質模型

| Dimension | Quality Question | Primary Evidence | Release Threshold |
|---|---|---|---|
| Functional correctness | 所有合法路徑、近似錯誤、修訂、save是否正確？ | automated／manual cases | no Blocker／High |
| Scientific integrity | 表述、動畫、數據和結局有否越過來源？ | claim audit＋Science sign | 100% P0 claims approved／removed |
| Learning／misconception | 玩家是否形成核心因果而非新誤解？ | transfer、interview、behavior | blocker misconceptions below threshold／resolved |
| Usability | 玩家能否不靠工作人員代操作完成？ | task completion、time、assist | PRE 95%≤8；C1≥80%≤30 formative targets |
| Accessibility | keyboard／zoom／motion／audio／cognitive barriers？ | manual＋automation＋user input | all Critical Path P0 checks pass |
| Performance | target school device穩定？ | frame／memory／load capture | ≥30 FPS baseline；no crash/leak |
| Reliability／recovery | refresh、offline、corrupt save、context loss可恢復？ | integration／soak | no data-loss High |
| Privacy／security | 是否只保存最小本機資料並抵抗輸入？ | schema／CSP／dependency audit | no unapproved collection／critical issue |
| Localization | zh-Hant與English Expo完整、術語一致？ | validator／LQA／pseudoloc | no missing key／critical overflow |
| Asset／license | 每項runtime資產可追溯？ | manifest／license／provenance | 100% release assets registered |
| Operability | deploy、offline、rollback、Expo reset可靠？ | runbook rehearsal | 2 successful rehearsals |

## 3. 測試策略

### 3.1 Test Level

| Level | Owner | When | Goal |
|---|---|---|---|
| Static／validation | Dev／Content／Art | every PR | types、IDs、schema、locale、assets、license |
| Unit | Dev | every PR | pure rules、claims、simulation、migration |
| Component | UI Dev／QA | every PR | focus、keyboard、states、workbenches |
| Integration | Dev／QA | main／nightly | quest→simulation→evidence→save；scene services |
| E2E | QA／Dev | main／gate | production-like Critical Path、browser、offline |
| Manual functional | QA | sprint／gate | 3D、camera、audio、visual、error |
| Specialist review | Science／Safety／A11y／HP | scheduled gates | claims、risk、misconception、stakeholders |
| Playtest | Education／QA | greybox／Alpha／Beta | real completion、comprehension、friction |
| Release verification | QA／Ops | RC／deploy | exact artifact、rollback、demo |

### 3.2 Test Type

Functional、regression、exploratory、compatibility、performance、memory、loading、reliability、offline、security/privacy、accessibility、localization、content/science、learning、usability、license／provenance、installation／deployment、recovery。

### 3.3 Risk-based Priority

- **P0 Critical：** data loss、cannot complete、science/safety misconception、unsupported claim、child/privacy leak、low-device crash、keyboard blocker。
- **P1 High：** significant delay、wrong consequence、major UI overflow、Firefox blocker、offline failure。
- **P2 Medium：** optional dialogue、minor visual/audio、non-critical animation。
- **P3 Low：** polish、rare unsupported path。

Test execution order：smoke → Critical Path → changed area → save/recovery → science/a11y → performance/device → full regression → polish。

### 3.4 Entry Criteria

A build enters formal test when：build ID and commit fixed；content／asset validation green；known blocker list provided；test data and migration fixtures available；release notes list changes；environment deploy stable；Science／A11y reviewers know affected claims；no developer-only manual setup required。

### 3.5 Exit Criteria

| Stage | Exit |
|---|---|
| Prototype | targeted spike cases pass／decision recorded |
| G2 Greybox | PRE complete、C1 S00–S04、save/reset、smoke green；no blocker architecture issue |
| Alpha | full C1 complete；all P0 cases attempted；target-player findings triaged；science issue list |
| Beta | content freeze；no Blocker、≤agreed High with owners；performance/a11y/localization/offline pass |
| RC | no Blocker／High；P0 regression pass；100% claims/assets/licenses；release/rollback rehearsed；QA report |

Pass rate alone cannot override a single science、privacy、data-loss or completion blocker。

### 3.6 Suspension／Resumption

Suspend affected suite／build for：wrong build／content version；repeated crash；save corruption；test environment unavailable；science claim withdrawn；more than 20% cases blocked by same defect；deploy mismatch。Resume after fix build、environment proof、data reset and smoke pass。

## 4. 測試環境

### 4.1 Environment

| Env | Build | Data | Purpose |
|---|---|---|---|
| Local Dev | dev | fixtures／debug | fast development |
| CI | production-like | deterministic fixtures | automated gates |
| Preview | optimized／no PWA | seeded QA profiles | sprint review／specialist review |
| Staging | exact RC candidate | clean＋migration | full regression／deploy rehearsal |
| Production | exact approved artifact | clean public | post-deploy smoke |
| Offline | archived package | clean／import fixtures | demo／network failure |

### 4.2 Device／Browser Matrix

| Device ID | Hardware | OS | Browser | Input | Tier | Owner／Location |
|---|---|---|---|---|---|---|
| DEV-BASELINE-01 | 待填 school low | 待填 | Chrome actual version | keyboard／trackpad | T1 | 待填 |
| DEV-BASELINE-02 | 待填 school low/mid | 待填 | Edge actual version | keyboard／mouse | T1 | 待填 |
| DEV-BASELINE-03 | 待填 Chromebook／equivalent | 待填 | Chrome actual version | keyboard／trackpad | T1 | 待填 |
| DEV-REF-01 | team dev machine | 待填 | pinned Chromium | keyboard／mouse | T0 | Tech |
| DEV-FX-01 | available desktop | 待填 | Firefox current | keyboard／mouse | T2 | QA |
| DEV-TAB-01 | optional iPad | iPadOS actual | Safari | touch | T3/P1 | optional |

Actual versions、GPU、RAM、resolution and browser policy must be recorded；“school computer” is not a test environment description。

### 4.3 Network Matrix

可重現 Lab baseline 使用 `10 Mbps down／2 Mbps up／100 ms RTT`＋cold cache；另測 `1 Mbps／200 ms RTT`、offline after load、offline first load、proxy／stale cache、asset 404、WASM MIME failure及 interrupted download。每個 RC 必須以 browser／OS shaping 重跑 Lab profile，並在 `DEV-BASELINE-01..03` 至少做一次不 shaping 的真實學校網路 rehearsal，記錄 throughput、RTT、proxy／MIME 與 cache state。

### 4.4 Account／Save State

No account。Profiles：clean、PRE mid、PRE complete、C1 S02、S04 valid、S04 failed control、S06 safety draft、C1 complete、legacy v1、corrupt current/valid backup、future schema、quota failure、Expo session。Each fixture versioned and immutable。

### 4.5 Test Data

All biological and river results are deterministic teaching simulations。Test data includes valid controls、failed positive、inconsistent C、near-miss claims、delay consequences、all hint levels、Guided／Standard。No real participant or experiment data in automated fixtures。

## 5. 需求追蹤

### 5.1 Requirement Traceability Matrix

| Requirement | Source | Acceptance／Tests |
|---|---|---|
| REQ-PRE-COMPLETE | GDD 9.3／PRE script | QA-PRE-001..014 |
| REQ-C1-FLOW | GDD 9.3／C1 script | QA-C1-001..028 |
| REQ-CONTROLS | GDD DG-003／SYS-TEST | QA-PRE-006/007、QA-C1-011..015 |
| REQ-SCIENCE-SCOPE | GDD 11／Claim Register | QA-SCI suite、QA-C1-006..010/020..022 |
| REQ-SAFETY | GDD DG-005／SYS-SAFETY | QA-C1-016..020 |
| REQ-REPORT | GDD 13／14 | QA-C1-024/025 |
| REQ-ACCESSIBILITY | GDD 17／TDD 14 | QA-A11Y-001..010、QA-SET-003/004 |
| REQ-SAVE | GDD 18／TDD 13 | QA-SAVE-001..009 |
| REQ-PERFORMANCE | TDD 18 | QA-PERF-001..006、QA-NET-001、QA-REL-001 |
| REQ-OFFLINE | TDD 15/20 | QA-OFF-001/002、QA-PWA-001 |
| REQ-PRIVACY | GDD 18／TDD 16 | QA-SEC-001..004、QA-SAVE-006 |
| REQ-EXPO | GDD／PM | QA-EXPO-001..004、QA-SAVE-008 |

### 5.2 Learning Outcome Traceability

| LO | In-game Evidence | Transfer／Test | Misconception Watch |
|---|---|---|---|
| LO-01 gene vs protein | PRE S01、C1 S03 | new reporter symbol categorization | DNA card “becomes” protein directly |
| LO-02 input/regulator/output | PRE S02、C1 states | novel input absent/present prediction | input placed on DNA |
| LO-03 controls | PRE S03、C1 S04 | failed known-high scenario | Low unknown = no target |
| LO-04 signal scope | PRE S04、C1 public claim | Use＋Limit＋Next | fluorescence = identity/concentration/safety |
| LO-05 detect/confirm/clean | C1 S04/S07/S08 | sequencing responsibility cards | sensor cleaned mercury |
| LO-06 multi-layer safety | C1 S05/S06 | explain two different categories | one box/kill switch = zero risk |
| LO-07 uncertainty／responsibility | C1 statement/report | choose next actor／unknown | admitting unknown = failure |
| LO-08 stakeholder impact | consultation→safety diff | ask what resident changed | public only needs persuasion |

### 5.3 Content Claim Traceability

| Claim ID | Build Location | Source Maturity | Tests／Reviewer |
|---|---|---|---|
| CLM-MER-001 | PRE bridge、C1 circuit animation／text | literature mechanism | QA-C1-006..008＋Science sign |
| CLM-DES-001 | source page／C1 intro | team proposal | QA-SCI-002＋Team sign |
| CLM-PERF-001 | must remain unknown | untested | search/static forbidden phrase test |
| CLM-SIM-001 | all test graphs／reports | teaching simulation | watermark／source／QA-SCI-005 |
| CLM-SAFE-001 | S05/S06/report | risk principle＋fiction | QA-C1-018..020＋Safety |
| CLM-CLEAN-001 | S07/S08 | story | QA-C1-021/022＋misconception interview |
| CLM-APT-001 | nowhere in P0 | blocked | build search／content validator |

## 6. 測試案例

### 6.1 Test Case Template

```markdown
- Test ID／Title：
- Requirement／Risk／Claim：
- Priority／Type／Automation：
- Build／Device／Browser：
- Preconditions／Fixture：
- Steps：
- Expected per step：
- Evidence（screenshot、video、log、hash）：
- Result／Defect ID：
- Tester／Date：
```

### 6.2 P0 Detailed Test Catalogue

| Test ID | Area | Pri | Precondition | Action／Steps | Expected Result | Automation |
|---|---|---|---|---|---|---|
| QA-BOOT-001 | Boot | P0 | 全新支援瀏覽器、清空儲存 | 開啟 production build | 5 秒內出現可互動 shell／設定；無白屏；build ID 可查 | E2E |
| QA-BOOT-002 | Boot | P0 | WebGL2 被停用 | 開啟遊戲 | 顯示不支援原因、資料狀態與替代方案；不無限 loading | E2E＋Manual |
| QA-BOOT-003 | Loading | P0 | 1 Mbps／200 ms network | 進入 C1 河港 | 顯示真實階段／進度；可取消／重試；save 保留 | E2E throttled |
| QA-BOOT-004 | Loading | P0 | 載入中 | refresh／back／再次進入 | 沒有 corrupt save／重複事件；回到合法 checkpoint | E2E |
| QA-BOOT-005 | WebGL | P0 | C1 scene active | 觸發 context loss／restore test hook | 世界暫停、提示恢復；從 checkpoint 重建或安全 reload | Integration＋Manual |
| QA-SET-001 | Setup | P0 | 全新 profile | 只用鍵盤完成語言／模式／可及性 | focus order正確；所有選項可選；進入首頁 | E2E |
| QA-SET-002 | Settings | P0 | 修改 text scale／subtitle／reduced motion／movement look-ahead／audio | refresh browser | 設定持久化，固定鏡頭 yaw／pitch 不可被改動，未重設章節進度 | E2E |
| QA-SET-003 | Settings | P0 | reduced motion on | 觸發轉場、focus、VFX | 無強制平移／shake／高動態；使用 cut/fade/static variant | Manual＋Visual |
| QA-SET-004 | Zoom | P0 | browser 200% zoom、1024×768 | 走完 setup、PRE 工作台、report | 無功能丟失；必要表格可讀／替代 layout；無水平頁面迷失 | Manual |
| QA-SET-005 | Input | P0 | rebind interact to existing key | 保存 | 衝突被指出；玩家可交換／取消；HUD顯示實際鍵位 | Component＋E2E |
| QA-PRE-001 | PRE | P0 | 新 profile | 開始前導 | 30 秒內首次有意義操作；沒有長知識牆 | Manual timing |
| QA-PRE-002 | PRE | P0 | S01 | 把 protein card 放 DNA rail | 播放層級因果／解釋，卡回手牌；不只紅叉 | Component |
| QA-PRE-003 | PRE | P0 | S01 | 正確放 promoter→reporter gene→terminator | protein只在 Cell Output出現；DNA與protein標籤不同 | E2E |
| QA-PRE-004 | PRE | P0 | S02 | 嘗試把 input放 DNA rail | 拒絕並指向 Cell Environment；說明input不是DNA零件 | Component |
| QA-PRE-005 | PRE | P0 | S02完整模型 | 切換 input absent／present | absent顯示低背景／低於判讀線；present顯示較高輸出 | Unit＋E2E |
| QA-PRE-006 | PRE | P0 | S03 known-high失敗、unknown Low | 形成「input不存在」強主張 | 強主張不可提交／被具體追問；顯示本輪不能回答 | Unit＋E2E |
| QA-PRE-007 | PRE | P0 | S03 controls pass | 比較 known-low／known-high／unknown | 玩家可形成限定篩查主張；來源與control status可見 | E2E |
| QA-PRE-008 | PRE | P0 | S04 | 組合 Use＋Limit＋Responsibility／Next | 缺少Limit的near-miss顯示後果並允許局部修訂 | E2E |
| QA-PRE-009 | PRE | P0 | 任一輪無進展 | 等待／按Hint到H3 | 三層按模式時序出現；H3可完成；不降低報告評價 | E2E timed |
| QA-PRE-010 | PRE | P0 | 完成S04 | 進入MerR bridge | generic roles翻成Pconst／merR／Pmer／dTomato，無序列／濃度／已驗證claim | Science＋E2E |
| QA-PRE-011 | PRE Save | P0 | S02 checkpoint | refresh／關閉重開 | 回到合法輪次，已完成因果保存，沒有重複unlock | E2E |
| QA-PRE-012 | PRE→C1 | P0 | 使用H3完成PRE | 進入C1 S03 | 可顯示role輪廓但不自動完成C1 circuit；canonical難度不改 | E2E |
| QA-PRE-013 | PRE A11y | P0 | 不使用滑鼠 | 以選卡→選槽完成全部 | 所有drag action有等價操作；live region不過度播報 | E2E＋Screen reader smoke |
| QA-PRE-014 | PRE Time | P0 | 首次玩家session | 完整Critical Path | 95% formative target ≤8分鐘；記錄提示不視為失敗 | Playtest |
| QA-C1-001 | C1 Loader | P0 | 未完成PRE，從Chapter Select進入 | 完成90秒核心三題 | 不寫p_prechapter_complete；仍可開始C1；內容不偽造過往 | E2E |
| QA-C1-002 | C1 S01 | P0 | 河港封鎖線 | 向hazard區前進 | 安全系統阻止、解釋暴露；角色不受傷；可返回 | E2E |
| QA-C1-003 | C1 S01 | P0 | 與公共衛生人員互動 | 查看健康資訊 | 提供替代用水／專業轉介；玩家不診斷或處理汞 | Content review |
| QA-C1-004 | C1 S02 | P0 | 四個位置未收集 | 掃描A–D與水流 | 每項有來源／類別；外觀與傳聞不自動標成結論 | E2E |
| QA-C1-005 | C1 S02 | P0 | 證據簿 | 把人物不適分類為污染源證明 | near-miss被指出因果缺口；可改為觀察／待確認 | Component＋Content |
| QA-C1-006 | C1 S03 | P0 | 迴路台空白 | 完成兩轉錄單元 | 精確為Pconst→merR→terminator及Pmer→dTomato→terminator | E2E＋Science |
| QA-C1-007 | C1 S03 | P0 | 正確迴路 | run No Hg²⁺ | MerR維持低背景／低於教學閾值；不顯示絕對零 | Unit＋Visual＋Science |
| QA-C1-008 | C1 S03 | P0 | 正確迴路 | run With Hg²⁺ | 顯示調控狀態／DNA幾何抽象變化、較高dTomato output | Unit＋Visual＋Science |
| QA-C1-009 | C1 S03 | P0 | 查看元件／動畫 | 檢查dTomato | reporter coding sequence與protein在空間／label分開 | Science＋A11y |
| QA-C1-010 | C1 Visual | P0 | 所有河港scene／高訊號結果 | 檢查河水與UI | 河水不變紅／不螢光；signal只在封閉測試介面 | Visual＋Science |
| QA-C1-011 | C1 S04 | P0 | 測試台 | 未放known-high便run | run可被阻止或結果不可形成強claim；disabled原因清楚 | E2E |
| QA-C1-012 | C1 S04 | P0 | positive control故障fixture | 查看unknown | 顯示本輪不能回答；保留原始模擬觀察，不錯誤解讀 | Unit＋E2E |
| QA-C1-013 | C1 S04 | P0 | valid fixture | 比較A–D重複 | B與D一致高於教學線；C不一致；文字摘要與圖一致 | Unit＋E2E |
| QA-C1-014 | C1 S04 | P0 | valid結果＋水流 | 選擇先隔離B並專業確認 | claim被允許；明示可逆行動／非最終定案 | E2E |
| QA-C1-015 | C1 S04 | P0 | valid結果 | 直接宣告B為源頭／全河污染 | 觸發具體延誤／更正／額外監測；可回證據修窄 | E2E |
| QA-C1-016 | C1 S05 | P0 | 公眾諮詢 | 只說相信科學／完全安全 | 不能完成；NPC提出外洩、誤報、廢物、通知權缺口 | Content＋E2E |
| QA-C1-017 | C1 S05 | P0 | 居民需求 | 完成需求→設計requirement配對 | 至少一項生活／權力需求實際改變S06選項或監督 | E2E |
| QA-C1-018 | C1 S06 | P0 | 安全台 | 只選單一kill switch／只選物理盒 | 顯示單層失效與殘餘風險；不能標零風險 | Unit＋E2E |
| QA-C1-019 | C1 S06 | P0 | 安全台 | 選不同層控制並run組合failure | 至少三層；owner／monitoring／failure response可見 | E2E |
| QA-C1-020 | C1 S06 | P0 | 工程細胞方案 | 檢查部署位置 | 所有canonical方案留在封閉匣／受控設施；無河流釋放選項 | Science／Safety |
| QA-C1-021 | C1 S07 | P0 | 篩查完成 | 進入source confirmation | 由專業採樣、水流、設施紀錄、外洩通路共同確認；不是sensor單獨 | Content＋E2E |
| QA-C1-022 | C1 S07 | P0 | public statement | 組合Use＋Limit＋Next | 明示感測協助、未清除、專業隊伍負責、監測持續 | E2E＋Science |
| QA-C1-023 | C1 S07 | P0 | 先前過度claim | 選擇公開更正 | 世界保留延誤後果；更正不抹去歷史；report引用修訂 | E2E |
| QA-C1-024 | C1 S08 | P0 | 完成章節 | 查看四維報告 | Evidence／Design／Responsibility／Communication分開；無總分／排行榜 | E2E |
| QA-C1-025 | C1 S08 | P0 | 使用提示／H3 | 查看報告 | 不降grade；只記support種類，不推論能力 | E2E |
| QA-C1-026 | C1 Time | P0 | 目標玩家首次完整 | 計時 | ≥80% ≤30分鐘；median／卡點記錄；optional內容分開 | Playtest |
| QA-C1-027 | C1 Replay | P0 | 完成章節 | 從S04重玩並選不同claim | 使用draft；結束前確認是否覆寫summary；舊report可追蹤 | E2E |
| QA-C1-028 | C1 Standalone | P0 | 無profile summary | 載入C1 | 使用中性fallback，不提玩家曾完成前章／作某決策 | E2E＋Content |
| QA-SAVE-001 | Save | P0 | 完成checkpoint | refresh | 返回正確checkpoint；evidence／claim／settings完整 | E2E |
| QA-SAVE-002 | Save | P0 | save current存在 | 模擬寫入中斷 | current不被破壞；next未promote；提示可重試 | Integration |
| QA-SAVE-003 | Save | P0 | current checksum錯 | 啟動 | 保留corrupt blob、使用backup、通知恢復內容 | Unit＋E2E |
| QA-SAVE-004 | Migration | P0 | v1 fixture | 以v2 app載入 | 逐步migration通過；ID與chapter summary不丟失 | Unit |
| QA-SAVE-005 | Migration | P0 | future-version save | 匯入舊app | 拒絕覆寫；允許保留／export；訊息清楚 | Unit＋E2E |
| QA-SAVE-006 | Import | P0 | 惡意／過大／含HTML JSON | 匯入 | size/schema/allowlist拒絕；無XSS／freeze | Security E2E |
| QA-SAVE-007 | Storage | P0 | local storage quota failure | checkpoint | session繼續；顯示保存失敗／export；不假裝成功 | Integration |
| QA-SAVE-008 | Expo | P0 | 家用profile存在 | 啟動Expo、完成、reset | 不修改家用profile；10秒內回初始session | E2E |
| QA-SAVE-009 | Delete | P0 | profile存在 | 清除資料／undo | 二次確認、10秒undo；完成後不存在；無遠端資料聲稱 | E2E |
| QA-REL-001 | Soak | P0 | production build | PRE/C1 route切換5次 | memory回近基線；無listener／audio／physics leak | Performance manual |
| QA-A11Y-001 | Keyboard | P0 | production build | 全流程不碰滑鼠 | 所有Critical Path可完成；無focus trap | Manual＋E2E |
| QA-A11Y-002 | Focus | P0 | 每個modal／workbench | 開啟／關閉 | initial focus合理；關閉回trigger／HUD fallback | Component＋E2E |
| QA-A11Y-003 | Screen Reader | P0 | Windows screen reader combination | 走setup、PRE一輪、test result | heading／label／selected card／result summary可理解；限制記錄 | Manual |
| QA-A11Y-004 | Color | P0 | 色覺差異／grayscale | 檢查signal、pass/fail、hazard、samples | 每個狀態有shape/icon/text；A–D不只顏色 | Visual manual |
| QA-A11Y-005 | Motion | P0 | reduced motion | 完成轉場、camera focus、VFX | 無不可關閉shake／auto-pan；無閃爍；功能相同 | Manual |
| QA-A11Y-006 | Audio | P0 | Master mute | 完成章節 | 所有語義有字幕／視覺；無音訊依賴 | Manual |
| QA-A11Y-007 | Subtitles | P0 | subtitle XL | 所有對話 | 不遮選項／重要世界提示；speaker清楚 | Visual manual |
| QA-A11Y-008 | Cognitive | P0 | Guided mode | 觀察HUD／提示 | 一次一個主目標；可回看；詞彙可展開；無限時 | Playtest |
| QA-A11Y-009 | 3D Navigation | P0 | fixed isometric＋Guided target lock | 從每 anchor 到目標 | interaction list／direction／target cycle 可用；無需操作鏡頭；reset 不丟 state | Manual |
| QA-A11Y-010 | High Contrast | P0 | high contrast on | 工作台／對話／HUD | focus／text／state達團隊標準；圖片文字有替代 | Manual＋axe |
| QA-LOC-001 | Localization | P0 | zh-Hant | 全P0 | 無missing key／placeholder／簡體混入；術語一致 | Automated＋LQA |
| QA-LOC-002 | Pseudoloc | P0 | pseudolocale | 所有screen | 50% expansion無功能截斷；button／dialog可用 | E2E visual |
| QA-LOC-003 | English Expo | P0 | en locale | Expo 3–5 min | 核心術語、superscript、line wrap、speaker、sim label正確 | LQA |
| QA-LOC-004 | Glyph | P0 | 各browser/font fallback | 顯示Hg²⁺、MerR/Pmer、dTomato | superscript／symbols不缺字或亂碼 | Visual |
| QA-SEC-001 | Security | P0 | production HTML | 檢查CSP／permissions／network | 無第三方analytics；無camera/mic/location；connect-src符合設計 | Automated＋Manual |
| QA-SEC-002 | Security | P0 | content rich text | 注入script/HTML token | validator拒絕；runtime以text/allowlist render | Unit＋Security |
| QA-SEC-003 | Privacy | P0 | 新profile／QA export | 檢查schema/log | 無姓名、email、school、health、location、free text | Schema test |
| QA-SEC-004 | Dependency | P0 | RC lockfile | audit/license/SBOM | 沒有未核准critical issue／unknown license；例外有簽核 | CI＋Review |
| QA-PERF-001 | Performance | P0 | Low baseline harbor | 5分鐘Critical Path | p95 frame ≤33.3ms；無持續stutter／thermal crash | Device capture |
| QA-PERF-002 | Performance | P0 | Mid baseline | 完整章 | 60 FPS target；p95記錄；不以High機替代Low | Device capture |
| QA-PERF-003 | Bundle | P0 | production build | 執行bundle report | shell≤3MB、PRE增量≤5MB、C1增量≤25MB、cached≤35MB或有核准cut | CI |
| QA-PERF-004 | Scene Budget | P0 | 每場景 | capture triangles/drawcalls/textures | typical≤450k／200；warning有owner或修正 | QA build |
| QA-PERF-005 | Memory | P0 | Low baseline | route cycle／workbench open/close | target≤512MB且無增長；scene dispose有效 | Manual |
| QA-PERF-006 | Loading | P0 | `10 Mbps down／2 Mbps up／100 ms RTT`、cold cache | boot、PRE start、C1 first cold route、cached zone transition | shell≤5 s acceptable；PRE cold≤10 s；C1 cold≤30 s；1 s內顯示具名stage；可取消／重試；記錄bytes/cache/RTT/timestamps | E2E throttled＋Device |
| QA-NET-001 | Network recovery | P0 | `1 Mbps／200 ms RTT`＋中斷下載／asset retry | 啟動或C1下載中斷、取消、重試 | 1 s內有loading狀態；不顯示假百分比；不破壞既有save；retry成功或顯示可行offline／受控展示路徑 | E2E throttled＋Manual |
| QA-OFF-001 | Offline | P0 | 已載入C1後斷網 | 完成章節／save | 不呼叫server；可完成；錯誤不阻擋 | E2E |
| QA-OFF-002 | Offline Package | P0 | 乾淨demo laptop | 依README啟動 | 可在無網路完成；版本／checksum一致 | Manual |
| QA-PWA-001 | PWA | P1 | 若VITE_ENABLE_PWA=true | install／offline／update／rollback | 不混版本／不丟save；fail則2026關閉PWA | E2E manual |
| QA-EXPO-001 | Expo | P0 | 全新session | 開始快速路徑 | 在30秒內出現核心操作；總長3–5分鐘 | Timed playtest |
| QA-EXPO-002 | Expo | P0 | 完成／中途離開 | 按reset | 10秒內清理session；無cache／save殘留 | E2E |
| QA-EXPO-003 | Expo | P0 | 訪客不懂背景 | 完成路徑 | 能說出signal是線索、control失敗不能下結論、下一步由專業確認 | Playtest |
| QA-EXPO-004 | Expo | P0 | 網路故障 | 使用offline／video fallback | presenter可在1分鐘內切換；內容一致且標示演示 | Rehearsal |


### 6.3 Exploratory Charter

| Charter ID | Mission | Risks | Timebox | Evidence |
|---|---|---|---:|---|
| EX-3D-01 | 嘗試在每個zone卡住、穿牆、鏡頭入牆、失去互動 | controller／camera／anchor | 60 min | map notes／video |
| EX-CLAIM-01 | 刻意形成所有近似錯誤／過度主張 | consequence／revision／report | 60 min | state diff／screens |
| EX-A11Y-01 | 只用keyboard、200% zoom、mute、reduced motion | focus／layout／info equivalence | 90 min | barrier log |
| EX-RECOVERY-01 | 在load/save/transition各階段refresh、offline、quota | data loss／stuck state | 60 min | save hashes／error codes |
| EX-TEACHER-01 | 模擬25–30分鐘工作坊／多人輪候／快速reset | facilitation／timing／privacy | 60 min | facilitator notes |
| EX-AI-REG-01 | 查看近期AI PR是否有未要求重構、claim／dependency drift | maintainability／source | 45 min | diff audit |

### 6.4 Checklist Test

Use checklists for：every scene anchor／collider；every screen state；every locale key；every asset license；every claim；every audio cue visual equivalent；every interaction disabled reason；every build variant；every release URL／offline copy。

## 7. 功能測試套件

### 7.1 啟動與載入

Run QA-BOOT suite plus：base path hosting、direct deep link、404 chunk、corrupt manifest、cache update、first locale load、unsupported resolution。Verify error page never loses local save。

### 7.2 控制與鏡頭

必要 camera cases：yaw 固定 45°、向下角約 50°、FOV profile 範圍、W／↑ 朝 screen-up、角色轉向不帶動鏡頭、look-ahead 關閉、focus command 可取消、reduced-motion cut／fade、屋頂／高牆 cutaway、occluder fade 不改 player collision、所有 Critical Path 物件在 720p／200% UI 可見、production 無 DebugFreeCam。

Keyboard／arrows、screen-relative movement、rebind、trackpad、pointer target selection、modal input capture、fixed yaw／pitch／FOV、look-ahead on/off、authored focus cancellation、cutaway／occluder fade、tab blur、reset。P0 has no pointer lock、camera sensitivity／invert、free rotation、zoom or jump action in UI／bindings／animation／docs。

### 7.3 角色與物理

Slopes、steps、corners、rails、NPC overlap、spawn、teleport、floor fall、frame drop、scene unload、camera profile bounds、roof／wall cutaway、`CameraOccluder` fade。No dynamic prop must be required to solve a task。

### 7.4 互動

World distance／screen-space projection／visibility、multiple candidates、target cycle、disabled reason、interaction list、focus restore、double activation、rapid input、route transition、stale entity handle、optional object missing fallback。

### 7.5 任務與對話

All nodes reachable／required nodes not bypassable；near-miss consequences persist；revision returns correct evidence；back／history；Guided／Standard canonical equality；standalone neutral defaults；replay draft／overwrite；no dialogue auto-advance Critical Path。

### 7.6 模擬與數值

Fixture hash、seed determinism、control invariants、text-summary parity、threshold label、no fake units／significant figures、version persisted、old science version report behavior。

### 7.7 UI／設定

All states、error／empty／loading、focus、responsive、high contrast、localization、settings live apply／persist、button disabled reason、screen registry modality、escape/back behavior。

### 7.8 存檔／載入／遷移

Atomic transaction、backup、checksum、quota、legacy、future、import attack、export、delete／undo、multiple profiles if supported、Expo isolation、chapter replay、content version correction。

### 7.9 音訊

Autoplay blocked、first interaction resume、mute、bus、ducking、tab hidden、loop seam、compression、missing asset、caption/visual equivalent、no semantic-only cue。

### 7.10 離線／復原

Network cut、asset failure、retry、static/offline package、PWA optional、context loss、route failure、production rollback、demo fallback。

## 8. 非功能測試

### 8.1 Performance

Measure p50/p95 frame time、CPU／GPU rough bottleneck、draw calls、triangles、texture estimate、JS long tasks on each Critical Path scene。Capture same camera route and build。Fail if baseline p95 >33.3ms sustained or player interaction unresponsive, even if average FPS looks acceptable。

### 8.2 Memory／Leak

Five PRE/C1 route cycles、open/close each workbench 20 times、dialog history、audio transitions、save/replay。Record browser process memory／Three renderer info／physics handles／event listeners where possible。Investigate upward trend, not just hard threshold。

### 8.3 Loading／Bundle

CI checks compressed sizes and chunk membership。Confirm no Future chapter asset/content、source maps、debug tools、AI logs or large source files in production。Cold／warm／slow network timing and progress accuracy。

### 8.4 Reliability／Soak

60-minute mixed session、tab hide/resume、sleep/wake、network changes、repeated save、fullscreen/window resize、device thermal。No crash、stuck input、audio runaway、save loss or exponential log。

### 8.5 Compatibility

Actual Chrome／Edge versions on T1；Firefox flow；optional Safari/touch only if P1。Record browser-specific known issue and workaround。Do not mark entire platform supported because homepage loads。

### 8.6 Security／Privacy

Static dependency／license、CSP、no secret、import validation、URL allowlist、sanitized SVG／rich text、no unapproved network request、schema data minimization、QA log review、AI data boundary evidence。

## 9. Accessibility QA

### 9.1 Keyboard／Focus

- no mouse Critical Path；
- visible focus all controls；
- modal initial/restore/trap；
- cards and grids have documented key model；
- shortcut conflict／rebind；
- canvas interaction mirrored／guided；
- no keyboard trap in browser fullscreen／dialog；
- skip link and landmarks。

### 9.2 Visual／Color／Text

200% zoom、1280×720／1024×600、high contrast、grayscale/color-vision simulation、projector washout、font fallback、superscript、no text in texture、focus contrast、status redundancy、chart text summary。

### 9.3 Audio／Caption

All dialogue captions、speaker、history、subtitle sizes；mute completion；critical sounds visualized；voice optional；music does not mask cue；autoplay failure graceful。

### 9.4 Motion／Timing

Reduced motion、no shake、cancel auto camera、no flashing、animations pause／skip、no reaction-time gate、hints not tied to ability、dialog not auto-disappear。

### 9.5 Cognitive Load

One primary goal、short text、terms on demand、Guided support、consistent icons、error recovery、near-miss explanation、no penalty for hints、no long uninterrupted dialogue。Use think-aloud carefully without teaching answers。

## 10. 本地化 QA

### 10.1 Pseudolocalization

Run every CI main or nightly：expanded strings、bracket markers、missing glyph、button／table／dialog overflow。Do not rely only screenshots；exercise keyboard/focus because overflow changes DOM。

### 10.2 Terminology

Approved glossary：繁體中文、MerR、Pmer、Pconst、dTomato、Hg²⁺、reporter gene／protein、known expected-low/high、教學模擬、篩查、確認、清理、殘餘風險。Search for `Hg++`、absolute zero／完全安全、已證明、清除汞等 forbidden or review-required phrases。English Expo gets Science／native/competent language review。

## 11. 內容、科學與教育 QA

### 11.1 Content Review

Review every player-visible claim、animation、icon、graph、loading tip、source page、marketing screenshot。Check mature case vs team proposal vs untested vs fictional vs simulation。Content validator links `ClaimId`; unlinked scientific statement is defect。

### 11.2 Misconception Audit

P0 blocker misconceptions：

1. red fluorescence is mercury／river glows red；
2. detection equals confirmation or cleanup；
3. one positive／low result proves identity／absence；
4. failed positive control still supports unknown conclusion；
5. OFF means zero expression；
6. sensor detects all mercury forms／concentration／health risk；
7. team has built／validated the construct；
8. engineering cells released into river；
9. one containment／kill switch guarantees zero risk；
10. public disagreement is ignorance and persuasion is success；
11. player diagnoses／cleans／approves deployment；
12. aptamer diagram is a complete working switch。

Audit via build search、visual inspection、scenario questions and free explanation。A single canonical screen that teaches blocker misconception can block release even if average learning score is high。

### 11.3 Learning Validation

Use equivalent pre/post／transfer prompts, not identical recall：new reporter color／symbol、new failed control、new Use-Limit-Next statement。Metrics：correct action、explanation category、confidence (optional), support used, completion time。Do not interpret hints as failure or small sample as causal proof。

### 11.4 Sensitive Content

Health statements reviewed；no diagnosis／graphic harm；pollution source fictional and not identifiable；stakeholder stories consented／de-identified；dual-use not operational；no wet-lab steps；child-friendly warning／support。Marketing and screenshots included in review scope。

## 12. Playtest 與可用性

### 12.1 Research Plan

Separate formative usability from learning research。Define age／background、sample、consent、data fields、recording、retention、compensation、withdrawal、analysis and publication before recruitment。Junior needs separate protocol and cannot inherit secondary-school evidence。

### 12.2 Session Script

1. Consent／purpose／not a test of participant；
2. device／accessibility preferences；
3. minimal neutral intro；
4. play without coaching, facilitator logs assistance；
5. transfer prompts；
6. open explanation：red signal、controls、next step、safety、resident change；
7. usability／emotion feedback；
8. debrief simulation／not medical advice；
9. data check／withdrawal info。

### 12.3 Observation Log

Record participant code (not name in game log)、route、mode、device、start/end、task success、hint／facilitator assistance、critical quote de-identified、misconception category、3D/a11y barrier、bug ID。Do not record health or school details unless approved and necessary。

### 12.4 Usability Metric

- PRE completion ≤8 min target；C1 ≤30 min target；Expo 3–5 min；
- first meaningful action ≤30 s；
- task success without facilitator代操作；
- hint level／reset count；
- top three delay points；
- System Usability-like short items may be used but not alone；
- comprehension and misconception rubric；
- player can name one decision with impact。

Targets are product hypotheses and may be revised after baseline，with reason记录；不得调阈值只为宣称成功。

### 12.5 Research Ethics

Age-appropriate consent/assent、guardian/school requirements、voluntary、no academic penalty、minimal data、secure separate storage、restricted access、retention/deletion、no upload to general AI、de-identification before quote、avoid photographing minors／screens unnecessarily、right to stop。Public Education／HP claims clearly state sample and method。

## 13. Automation

### 13.1 Automation Scope

Automate stable high-risk logic：content references、forbidden claims、simulation invariants、quest transition、save migration、keyboard DOM flow、Critical Path checkpoints、bundle／license、network requests。Do not over-automate subjective art、science nuance、3D comfort or stakeholder dignity。

### 13.2 Automated Flow

| Suite | Frequency | Max Time | Fail Policy |
|---|---|---:|---|
| Static／unit | PR | 5–8 min | blocks merge |
| Component／integration | PR/main | 10–15 min | blocks merge／main alert |
| E2E smoke | main | 10 min | blocks release branch |
| Full E2E／browsers | nightly／gate | 30–45 min | gate blocker until triaged |
| Bundle／license／SBOM | main／RC | 5–10 min | budget／license gate |
| Visual stable screens | nightly／gate | 10 min | review differences；not auto-approve |

### 13.3 Visual Regression

Capture setup、PRE key states、test result、safety、report、同一固定斜俯視 harbor route per graphics tier。Mask time/build dynamic text only where necessary。Tolerance tuned；review by human。No visual baseline updated in same PR without explicit screenshot review。

### 13.4 Flaky Test Register

A flaky test is a defect。Fields：ID、suite、first seen、rate、cause、owner、quarantine expiry。Quarantine max 7 days and never for Blocker flow；skipped test needs ticket。Agents cannot solve by adding arbitrary waits；prefer event／state wait。

## 14. Defect 管理

### 14.1 Severity

| Severity | Definition／Examples | Release |
|---|---|---|
| Blocker | cannot boot/complete；data loss；science/safety/privacy severe harm；all baseline devices crash | no release |
| High | major P0 path wrong；keyboard blocker；wrong claim/consequence；severe performance／offline | no RC unless fixed；exception extraordinary and signed |
| Medium | workaround exists；optional path／noticeable visual／Firefox issue | accepted only with owner/workaround |
| Low | cosmetic／minor wording not affecting meaning | may defer |

### 14.2 Priority

Priority considers severity、frequency、exposure、gate date、fix risk。Science／privacy blocker always immediate。A frequent cosmetic issue may be P2；rare data loss remains P0 priority。

### 14.3 Bug Report Template

```markdown
- Defect ID／Title：
- Build／Commit／Content Version：
- Device／OS／Browser／Locale／Mode：
- Severity／Priority：
- Requirement／Claim／Test ID：
- Preconditions／Save Fixture：
- Reproduction Steps：
- Actual／Expected：
- Frequency：
- Evidence（video、screenshot、log、save hash）：
- Science／A11y／Privacy／License Impact：
- Workaround：
- Owner／Target Build：
- Regression Test Added：
```

### 14.4 Defect Workflow

New → Triaged → Assigned → In Progress → Ready for Verify → Verified → Closed。Reopen if same build/version or regression。`Won't Fix`／`Deferred` requires reason、impact、workaround、owner、review date and Product/QA approval；science/safety reviewer for content defects。

### 14.5 Defect Register

Track counts by severity、age、area、introduced build、escape。Gate reports list each open Blocker/High, not just count。AI-generated changes are tagged for process analysis, not blame。

### 14.6 Deferred Defect

A deferred defect cannot make acceptance statement false。Known issues page only for user-relevant limitations；it is not a place to hide science、data loss or core accessibility blockers。

## 15. Smoke、Regression 與 Acceptance

### 15.1 Smoke Suite

Boot supported／unsupported、setup、start PRE、one card interaction、save/refresh、C1 load、move/interact、open each workbench、run deterministic test、report、Expo reset、sources/privacy。Target ≤12 minutes automated＋5 minutes manual visual。

### 15.2 Regression Suite

Run all P0 catalogue by risk; full automated plus manual matrix at Beta/RC。Changed content triggers claim/misconception/LQA; changed asset triggers performance/license/visual; changed save triggers all migrations; changed input/UI triggers keyboard／zoom。

### 15.3 User Acceptance

Product Owner evaluates GDD acceptance；Science／Safety signs claims；Education／HP reviews learning／stakeholders；Tech signs exact artifact／rollback；QA recommends release based on evidence。UAT is not a substitute for testing and cannot waive specialist authority silently。

## 16. Test Execution

### 16.1 Run Summary

| Field | Value |
|---|---|
| Run ID／Build |  |
| Scope／Environment |  |
| Planned／Executed／Pass／Fail／Blocked |  |
| Open Blocker／High／Medium／Low |  |
| Requirement／Claim Coverage |  |
| Device／Browser Coverage |  |
| Key Risks／Recommendation |  |

### 16.2 Daily Result

During RC：new defects、verified fixes、regressions、build stability、device runs、science/a11y changes、next blocking evidence。Keep concise and link details。

### 16.3 Blocker

When Blocker found：stop affected release、notify Owner／QA／Product／specialist、preserve build/save/log、create defect、decide rollback／feature disable／fix、run focused＋full smoke。Do not let another agent “patch directly on production”。

## 17. Release Checklist

### 17.1 Build

- exact tag／commit／build ID；clean reproducible build；
- production config no debug/test routes/source maps/secrets；
- content/asset manifests／hashes；bundle budgets；
- dependency audit／SBOM／notices；
- staging artifact equals production artifact；
- offline archive／checksum；rollback artifact。

### 17.2 Functional

- all Critical Path and modes；standalone／replay／Expo；
- error/loading/retry；save/migration/recovery/import/export/delete；
- no dead-end／stuck/camera/input issue；
- report and consequences correct；
- no Future route visible／included。

### 17.3 Content

- scripts／build parity；all claim IDs；Science／Safety／HP sign；
- simulated labels permanent；source／maturity page；
- no aptamer blocked content；no performance numbers without source；
- health／authority／cleanup boundaries；
- public screenshots／copy reviewed。

### 17.4 Compatibility／Performance

- T1 Chrome/Edge actual versions；Firefox best effort；
- baseline ≥30 FPS、memory／soak、loading／bundle；
- school network／offline；
- optional PWA only if suite pass。

### 17.5 Accessibility／Localization

- keyboard、focus、zoom、contrast、symbols、motion、audio/subtitles、cognitive；
- screen reader smoke／limitations documented；
- zh-Hant LQA、English Expo、pseudoloc、glyph；
- no text-only-in-image／untranslated key。

### 17.6 Security／Privacy／Child Safety

- no remote telemetry／unapproved calls；CSP／permissions；
- local schema minimum；import validation；
- playtest data not in build/repo；
- AI logs contain no sensitive data；
- research／privacy／contact pages；
- dependency／license／AI provenance complete。

### 17.7 Operations／Rollback

- staging／production smoke；
- previous build backup；rollback rehearsed；
- Expo reset、facilitator guide、demo laptop、power/network plan；
- video/screenshots fallback；
- support／incident owners；
- known issues and public version note。

## 18. Release Recommendation

QA recommendation options：

- **GO：** all exit criteria met；
- **GO WITH CONDITIONS：** no Blocker／High，limited Medium with documented workaround／owner；
- **CONTROLLED RELEASE ONLY：** public risk unresolved but supervised demo safe；
- **HOLD：** fix／evidence needed；
- **NO-GO：** science、privacy、data loss、completion or device blocker。

### 18.1 Open Defects by Severity

| Severity | Count | IDs／Summary | Accepted By |
|---|---:|---|---|
| Blocker |  |  | — |
| High |  |  | — |
| Medium |  |  |  |
| Low |  |  |  |

### 18.2 Known Issues

Each issue includes affected browser/device/route、impact、workaround、public disclosure、fix owner/date。Do not list internal implementation detail or sensitive vulnerability publicly。

### 18.3 Sign-off

| Role | Name | Decision | Date | Conditions |
|---|---|---|---|---|
| QA Lead（recommendation） | 待指派 | — | — | — |
| Product Owner（release） | 待指派 | — | — | — |
| Technical／Operations | 待指派 | — | — | — |
| Science／Safety | 待指派 | — | — | — |
| Education／HP／Privacy | 待指派 | — | — | — |

## 19. Post-release Verification

Within 30 minutes：production boot、PRE start、C1 load、save、source/privacy、Expo reset on two networks。Within 24 hours：support／errors、hosting cache、offline download、license links。Within 7 days：escaped defects、misconception reports、performance、AI/process retrospective、whether rollback/hotfix needed。No remote player analytics assumed。

## 附錄 A：測試證據索引

Recommended path：`docs/qa/<gate>/<run-id>/` containing summary、device matrix、screens/video links、logs、save hashes、performance captures、playtest de-identified report、science/a11y sign-offs。Do not commit participant identifiable media to public repo。

## 附錄 B：測試帳號與資料清理

No accounts。QA profiles use random fixture IDs。After session：export required log、clear browser profile／Expo session、remove local participant code mapping from device、confirm no downloads／screens with personal data、return research data to approved custodian。

## 附錄 C：最終測試報告最低內容

1. build／scope／dates／testers；
2. requirement、claim、device、browser、locale、a11y coverage；
3. pass/fail/blocked and defect trends；
4. performance／bundle／memory／offline；
5. science/misconception／playtest outcomes with limits；
6. privacy／license／AI provenance；
7. open defects／known issues／workarounds；
8. release recommendation and sign-offs；
9. rollback／post-deploy plan。
