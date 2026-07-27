# 《微界工程師：生命迴路》AI 任務包模板

> AI Task Packet Template｜版本 1.0｜日期：2026-07-27｜每個 agent 任務先複製本文件，再刪除不適用說明

## 0. 使用方式

一個任務包對應一個 ticket、一個 branch／worktree 與一個主要 outcome。先由人類 Owner 填寫，再交給 agent 做 Explore／Plan／Build／Test／Review。不要只貼一句「幫我完成第一章」；那會把範圍、科學、可及性和架構決定交給模型猜測。

- 小型低風險任務可以合併 Explore＋Plan；
- 跨檔、state、save、3D、science、a11y、privacy、dependency、release 任務必須先 Plan；
- Reviewer 使用同一任務包，但不要只讀 implementer summary；
- 所有欄位若不知道，寫 `UNKNOWN — needs <ROLE> decision`，不要讓 agent補完；
- 任務完成後把本文件連結放入 PR／issue。

---

# TASK `<TICKET-ID>` — `<一句話 outcome>`

## 1. Metadata

```yaml
ticket_id: <TICKET-ID>
title: <SHORT TITLE>
status: Draft | Ready | In Progress | Review | Done | Blocked
priority: P0 | P1 | R&D | Future
risk: Low | Medium | High | Blocker
task_type: Explore | Plan | Build | Test | Review | Asset | Content | Science-support
owner_name: <HUMAN NAME>
accountable_role: Product | Design | Tech | Art | Science | Safety | Education/HP | QA | AI Steward
human_reviewer_name: <HUMAN NAME>
independent_ai_review: Required | Optional | Prohibited
target_branch: <feat/TICKET-slug>
base_commit: <SHA>
due_date: YYYY-MM-DD
data_classification: D0 | D1-approved | D2-approved | D3-prohibited
ai_tools_allowed: [<TOOL/MODEL OR CAPABILITY TIER>]
ai_tools_prohibited: [<TOOLS/PROVIDERS>]
max_agent_runs: <NUMBER>
max_elapsed_time: <MINUTES>
max_cost: <CURRENCY/AMOUNT OR TEAM POLICY REF>
```

## 2. 玩家／系統 Outcome

用可觀察結果描述，不先指定實作：

> 當 `<玩家／系統前置狀態>`，玩家做 `<行動>` 時，系統應 `<可觀察結果>`；在 `<失敗／邊界狀態>` 時，系統應 `<安全回復／限制>`。

**不應寫：**「新增一個 manager class。」

**較好：**「玩家在 failed positive control 後不能提交 contamination claim；UI 顯示 Limit＋Next，並可回到 test bench 重新選 control。」

## 3. Why Now

- 對應 milestone／gate：`<G1/G2/Alpha/Beta/RC>`
- 阻擋的工作：`<TICKETS／PLAYTEST／ASSET>`
- 不做的後果：`<PLAYER／SCIENCE／RELEASE IMPACT>`
- 這是 bug／feature／debt／spike：`<TYPE>`

## 4. 權威來源與衝突順序

只提供完成任務必要的來源；不要把整個 repo 塞入 context。

| 優先 | Source | Section／ID | 本任務需要的規則 |
|---:|---|---|---|
| 1 | Human decision／signed ADR | `<LINK>` | `<RULE>` |
| 2 | `AGENTS.md` | `<SECTION>` | `<RULE>` |
| 3 | GDD | `<REQ-ID／SECTION>` | `<OUTCOME>` |
| 4 | TDD | `<CONTRACT／SECTION>` | `<ARCHITECTURE>` |
| 5 | QA Plan | `<TEST-ID>` | `<PASS CONDITION>` |
| 6 | Script／content | `<SCENE／LINE ID>` | `<CANONICAL COPY／EVENT>` |
| 7 | Claim Register | `<CLAIM-ID>` | `<APPROVED／PROHIBITED WORDING>` |

**衝突規則：** 發現來源衝突時停止；列出衝突與影響，交由 `<ROLE>` 決定。禁止自行選擇最新檔名、最長文件或最像答案的內容。

## 5. Current Behaviour

由人類或 Explore agent 填寫：

- Entry point：`<ROUTE／SCENE／COMMAND>`
- Current observed result：`<RESULT>`
- Expected result：`<RESULT>`
- Reproduction steps：
  1. `<STEP>`
  2. `<STEP>`
  3. `<STEP>`
- Evidence：`<SCREENSHOT／LOG／TEST／VIDEO LINK>`
- Frequency：Always／Intermittent／Device-specific
- First known good／bad build：`<VERSION>`

## 6. Scope

### 6.1 Allowed paths

```text
<path/a>
<path/b>
<tests/path>
```

### 6.2 Read-only context paths

```text
<docs/path>
<contract/path>
```

### 6.3 Forbidden／protected paths

```text
content/scripts/canonical/**
content/science/approved/**
src/save/migrations/**       # 除非本 ticket 明確批准
.github/workflows/release/**
licenses/**
.env*
<ADDITIONAL PATHS>
```

### 6.4 Explicit non-goals

- 不實作 `<FUTURE FEATURE>`；
- 不重寫 `<NEIGHBOUR MODULE>`；
- 不加入新 production dependency；
- 不改 canonical script／science copy；
- 不改善與 acceptance 無關的 styling；
- 不處理 `<KNOWN SEPARATE BUG>`。

## 7. Interfaces／Contracts

| Contract | Current | Allowed change | Compatibility requirement |
|---|---|---|---|
| Event／Command | `<TYPE>` | None／Additive／Breaking-approved | `<RULE>` |
| Content schema | `<VERSION>` | `<CHANGE>` | old fixture must still validate／migration required |
| Save schema | `<VERSION>` | `<CHANGE>` | no silent data loss；fixture required |
| DOM／A11y | `<ROLE/FOCUS>` | `<CHANGE>` | keyboard／focus return preserved |
| Scene／Asset | `<ID/BUDGET>` | `<CHANGE>` | draw call／poly／memory budget |
| Localization | `<KEYS>` | `<CHANGE>` | no hard-coded player text |

未列出的 public contract 預設不可改。

## 8. Acceptance Criteria

每項要可獨立 pass／fail，並連結 QA ID。

| AC ID | Given | When | Then | QA／Evidence |
|---|---|---|---|---|
| AC-01 | `<STATE>` | `<ACTION>` | `<OBSERVABLE RESULT>` | `<TEST-ID／SCREEN>` |
| AC-02 | `<NEGATIVE STATE>` | `<ACTION>` | `<SAFE FAILURE>` | `<TEST-ID>` |
| AC-03 | `<BOUNDARY>` | `<ACTION>` | `<RECOVERY／NO DATA LOSS>` | `<TEST-ID>` |
| AC-04 | keyboard／reduced motion／locale | `<ACTION>` | `<A11Y／L10N RESULT>` | `<TEST-ID>` |

### 8.1 Science／Learning acceptance（適用時）

- [ ] `Claim ID <...>` 的 approved wording 沒有被擴大；
- [ ] Team proposal 沒有被改成 team result；
- [ ] 教學模擬有永久標示；
- [ ] 無 Hg²⁺ 狀態沒有被寫成絕對 zero；
- [ ] dTomato 沒有被當成即時／定量濃度計；
- [ ] aptamer content 沒有進 public path，除非 `DEC-SCI-002` 已關閉；
- [ ] 玩家沒有取得診斷、執法、確認污染或部署批准權。

### 8.2 Accessibility acceptance（適用時）

- [ ] 全程鍵盤可達；
- [ ] 焦點可見；modal 開啟後 trap，關閉後回到觸發元件；
- [ ] canvas 可用 Escape／明確按鈕離開；
- [ ] 色彩不是唯一訊號；
- [ ] reduced motion／camera setting 生效；
- [ ] 關鍵任務有 guided／non-precision fallback。

### 8.3 Performance acceptance（適用時）

- Device ID：`<DEVICE>`
- Scenario：`<SCENE／DURATION>`
- FPS target：`>= 30 FPS baseline`
- Memory target：`<= 512 MB target`
- Draw calls：`typical <= 200；warning 250`
- Visible triangles：`typical <= 450k；warning 500k`
- Bundle delta：`<BUDGET>`

## 9. Test Plan

### 9.1 Required commands

先按 repo lockfile／scripts 確認，不自行改 package manager。

```bash
<package-manager> run format:check
<package-manager> run lint
<package-manager> run typecheck
<package-manager> run test -- <FOCUSED TEST>
<package-manager> run test
<package-manager> run content:validate
<package-manager> run build
```

### 9.2 Required fixtures／cases

| Case | Purpose | Expected failure if bug exists |
|---|---|---|
| Positive | 正常完成 | `<FAIL>` |
| Negative | 禁止／不完整狀態 | `<FAIL>` |
| Boundary | first／last／empty／max | `<FAIL>` |
| Recovery | reload／reset／corrupt／cancel | `<FAIL>` |
| Regression | 原 bug | `<FAIL>` |
| Accessibility | keyboard／focus／motion | `<FAIL>` |
| Localization | zh-Hant／English Expo | `<FAIL>` |

### 9.3 Manual evidence

- [ ] Screenshot／screen recording；
- [ ] Browser／device/version；
- [ ] FPS／memory／draw call capture；
- [ ] Keyboard-only walkthrough；
- [ ] Save／reload／reset；
- [ ] Offline／fresh install（release-related）；
- [ ] Science／copy sign-off link。

## 10. Dependencies and Decisions

| Item | Status | Owner | Required before build? | Fallback |
|---|---|---|---|---|
| `<DEC-ID>` | Open／Decided | `<ROLE>` | Yes／No | `<SAFE DEFAULT>` |
| `<ASSET-ID>` | Ready／Blocked | `<ROLE>` | Yes／No | placeholder／DOM alternative |
| `<API／LIB>` | Existing／New | Tech | Yes | do not add／use existing |

如果 required decision 仍 Open，agent 只能做 Explore／Plan／fixture，不可把推薦基線當成正式決定。

## 11. Data／Security／Privacy

- Data class：`<D0/D1/D2/D3>`
- Permitted providers：`<LIST>`
- Redactions performed：`<DETAIL>`
- Network access：None／Allowlisted domains `<LIST>`
- Secrets needed：None（預設）；若需要，改由人類執行，不貼入 prompt
- Personal／minor data：None（必須）
- Telemetry change：None／`<APPROVED DECISION>`
- Dependency／supply-chain change：None／`<APPROVED DECISION>`

## 12. Asset／License（適用時）

| Asset ID | Source／creator | License／terms | AI tool／model | Inputs rights | Public-use reviewer |
|---|---|---|---|---|---|
| `<ID>` | `<SOURCE>` | `<LICENSE>` | `<TOOL OR N/A>` | `<RIGHTS>` | `<NAME>` |

- 不得使用來源不明 asset；
- 生成內容不等同自動可商用／可再散布；
- 不建立看似真實的實驗／污染影像而不標示；
- 尺寸、poly、texture、material、audio budget 依 Asset Guidelines。

## 13. Agent Operating Instructions

### 13.1 Explore output

```markdown
## Relevant files
## Current flow
## Existing patterns/tests
## Risks and unknowns
## Minimal change surface
## Questions requiring human decision
## Recommended next step
```

### 13.2 Plan output

```markdown
## Assumptions
## Step-by-step changes
## Files to edit
## Contract/schema effects
## Tests and evidence
## Rollback
## Stop/ask conditions
## Estimated diff/dependencies
```

### 13.3 Build constraints

- 只改 allowed paths；
- 不新增 production dependency，除非有 signed decision；
- 不改 package manager／lockfile，除非任務明確要求；
- 不使用 `any`、`@ts-ignore`、關閉 strict 或刪測試來取得綠燈；
- 不在 content 中執行 raw HTML／JavaScript；
- 不把 UI 和 Three.js 直接互相查找；使用 typed event／command contracts；
- 不把 debug／cheat／telemetry 開關預設打開；
- 遇到 protected path、science conflict、save migration、secret、data、license 問題立即停止。

### 13.4 Final output

```markdown
## Summary
## Changed files
## Acceptance mapping
## Commands run and results
## Manual evidence
## Not run / not verified
## Risks and known limitations
## Science/a11y/privacy/license/save/release impact
## Rollback
## Suggested reviewer focus
```

## 14. Stop／Ask Conditions

Agent 在以下情況不應「自行合理推斷」：

- 需求與 GDD／TDD／script／Claim Register 衝突；
- 需要修改 forbidden／protected path；
- 需要新增 production dependency、網路服務或 telemetry；
- 需要改 save schema／migration；
- 需要新增科學 claim、數字、真實資料或 aptamer public content；
- 看見 secret、個資、未成年人資料；
- 發現 asset license 不明；
- 預計 diff 超出 task 上限或跨另一 subsystem；
- 兩輪嘗試仍無法通過同一測試；
- command 可能 destructive、部署或改遠端狀態；
- reviewer／owner／decision 不明。

回報格式：`BLOCKED — <REASON>｜Needs <ROLE> decision on <QUESTION>｜Safe fallback: <OPTION>`。

## 15. Human Plan Approval

| 欄位 | 填寫 |
|---|---|
| Plan version／link |  |
| Approved scope |  |
| Approved paths |  |
| Additional constraints |  |
| Human approver／date |  |
| Approval expires／trigger |  |

## 16. Review Checklist

### Requirements

- [ ] Diff 只完成一個主要 outcome；
- [ ] AC 可觀察且有證據；
- [ ] 沒有偷偷實作 Future／P1；
- [ ] 來源衝突已升級而非自行解決。

### Code／Architecture

- [ ] 使用既有 pattern；
- [ ] 沒有不必要 abstraction／manager／service；
- [ ] strict TypeScript；無未解 `any`／ignore；
- [ ] UI／3D／content／save 邊界符合 TDD；
- [ ] error／cancel／reload／reset path 存在；
- [ ] 沒有未批准 dependency／network／telemetry。

### Tests

- [ ] 測試會因錯誤實作而失敗；
- [ ] 包含 negative／boundary／recovery；
- [ ] 沒有只為 snapshot 或 coverage 而測；
- [ ] command 結果可重現；
- [ ] 實機／視覺／效能工作有非文字證據。

### Science／Safety／Learning

- [ ] Claim IDs 正確；
- [ ] proposal／simulation／result 分層；
- [ ] 限制與不確定性可見；
- [ ] 沒有 zero-risk、診斷、監測、部署或未驗證效能主張；
- [ ] near-miss 可修正，不用錯誤 science 作懲罰。

### Accessibility／Localization

- [ ] keyboard/focus；
- [ ] reduced motion／camera；
- [ ] non-color signal；
- [ ] locale keys；
- [ ] zh-Hant overflow；英文 Expo 不破版。

### Data／License／Release

- [ ] 無 secrets／PII／minor data；
- [ ] asset／dependency provenance；
- [ ] save migration 安全；
- [ ] release／service worker／hosting 無未批准變更；
- [ ] AI-Assisted Change Notice 完整。

## 17. Completion Record

| 欄位 | 填寫 |
|---|---|
| Implementer／agent session |  |
| Tool／model／date |  |
| Data class |  |
| PR／commit |  |
| CI run |  |
| Manual evidence |  |
| Independent review |  |
| Findings closed |  |
| Science／a11y／privacy／license approvals |  |
| Human merge approver／date |  |
| Release build first included |  |
| Follow-up debt／ticket |  |

---

# 已填寫示例：PRE-S03 Failed Positive Control

> 此示例只展示任務包粒度；實際 path／command 以 repo 建立後為準。

## A. Metadata

```yaml
ticket_id: PRE-042
title: Block claim confirmation after failed positive control
status: Ready
priority: P0
risk: High
task_type: Build
owner_name: "待由團隊填寫"
accountable_role: Design
human_reviewer_name: "待由團隊填寫"
independent_ai_review: Required
target_branch: feat/PRE-042-positive-control-gate
base_commit: <SHA>
due_date: 2026-08-23
data_classification: D0
ai_tools_allowed: [approved coding agent, independent review agent]
ai_tools_prohibited: [unapproved provider]
max_agent_runs: 3
max_elapsed_time: 120
max_cost: per DEC-AI-002
```

## B. Outcome

當玩家在 PRE S03 的 positive control 失敗時，`Confirm claim` 按鈕維持不可用，介面顯示「目前證據不足」及 `Limit／Next`，玩家可返回 control selection 修正；成功 control 後才可確認有限主張。Reload 不可把 failed state 變成 success。

## C. Sources

| Source | ID | Rule |
|---|---|---|
| GDD | PRE S03／Evidence→Claim | 證據不足不能形成確認主張 |
| TDD | typed state transition／save summary | UI 不直接改 scene；reload 保留 outcome |
| QA | PRE-FUNC／EX-CLAIM cases | negative、recovery、reload |
| Script | PRE S03 | canonical feedback；不可自行改對白 |

## D. Allowed／Forbidden

Allowed：

```text
src/prelude/state/**
src/ui/claim/**
tests/prelude/**
content/prelude/<scene-data-file>   # 只可改 state mapping，不改文字
```

Forbidden：

```text
content/scripts/canonical/**
content/science/approved/**
src/save/migrations/**
package.json
```

## E. Acceptance

| AC | Given | When | Then |
|---|---|---|---|
| AC-01 | positive control failed | open claim panel | confirm disabled；Limit＋Next visible |
| AC-02 | failed state | reload | still failed；no auto-unlock |
| AC-03 | failed state | choose valid control and rerun | state becomes sufficient；confirm enabled |
| AC-04 | keyboard only | repair flow | all controls reachable；focus returns to rerun button |
| AC-05 | any state | inspect public text | no contamination confirmation／diagnostic authority |

## F. Tests

- unit：transition rejects `CONFIRM_CLAIM` when `positiveControl !== pass`；
- integration：failed → reload → repair → confirm；
- negative：missing／unknown control；
- a11y：disabled reason is programmatically associated；focus return；
- manual：zh-Hant copy、Guided／Standard 共用成功條件。

## G. Stop conditions

若 canonical script 沒有對應 `Limit／Next` 文案，停止並要求 Design／Science 決定；不要由 agent 撰寫新的科學宣稱。若 save summary 無法表達 control state，提出最小 schema proposal，但不要修改 migration。
