# 《微界工程師：生命迴路》交付前驗證報告

> Delivery Validation Report｜版本 2.0｜驗證日期：2026-07-27｜狀態：**固定斜俯視鏡頭、C2–C8 設計契約與文件結構驗證通過；產品、科學與公開發行仍須依 Gate 簽核**

## 1. 驗證目的

本報告記錄使用者要求的第二輪完整審核：檢查文件是否仍有無效、不合邏輯、違反常識或互相矛盾的內容；把 3D 鏡頭統一為 Hades／Diablo 類固定斜俯視透視構圖；把第二至第八章的 Scene script、canonical flags、route／schema／fixture／transaction 與 Future build exclusion 納入 GDD／TDD；最後重跑結構與邏輯 validator。

本驗證不等同 Science Lead、Safety、Privacy、Education／HP、Product、Tech 或 QA 的正式批准，也不表示遊戲已實作或通過真人 playtest。正式 Go／No-Go 仍以 [本輪邏輯／鏡頭／C2–C8 審核](24_LOGIC_CAMERA_AND_CHAPTER_2_8_AUDIT.md)、[獨立製作就緒審核](18_INDEPENDENT_PRODUCTION_READINESS_AUDIT.md)、[開放決策登記](20_OPEN_DECISIONS_REGISTER.md) 與各階段 Gate 為準。

## 2. 最終自動驗證結果

| 指標 | 結果 |
|---|---:|
| Markdown 文件 | `35` |
| 已檢查相對連結 | `73` |
| 已檢查 Markdown 表格 | `947` |
| 詳細 QA 案例 | `94` |
| Decision 定義 | `103` |
| Claim 定義 | `31` |
| 來源 PDF 頁數 | `5` |
| Structural validator | `0 errors／0 warnings` |
| Logic validator | `0 errors／0 warnings` |
| Manifest 收錄檔案 | `38` |

來源 PDF `sources/TEAM-PDF-2026-INTRO.pdf` 的 SHA-256：

```text
090f2d44f62d95c1edd9449c582236c0798217940e1529f185afb3fff3a2f64a
```

此 hash 與使用者提供的 `iGEM 2026 intro(4).pdf` 相同，表示打包副本沒有內容變動。

## 3. 本輪重要修正

| Finding | 原問題 | 修正 |
|---|---|---|
| Camera contract | 固定斜俯視、肩後跟隨、自由 yaw／pitch／zoom 概念曾混在同一文件包 | 全部統一 `IsometricPerspectiveRig`：透視投影、固定 yaw／down angle／FOV；鏡頭只隨玩家**位置**平移，不隨角色**面向**旋轉；production 無自由相機 |
| Movement fallback | GDD 風險表曾寫 `point-and-click fallback`，與 TDD 不做 click-to-move／pathfinding 矛盾 | 改為 interaction list、keyboard target cycle、safe-anchor reset 及點擊已高亮互動物；不建立第二套導航 |
| Camera numerics | offset、FOV 與畫面 Y 定義可能被不同工程師各自解讀 | 明定 horizontal offset 是地面平面距離、FOV 是 Three.js vertical FOV、`targetScreenY` 以 0=top／1=bottom；12 m 高／10 m offset 與約 50° down angle 幾何一致 |
| C2–C8 authority | GDD／TDD 曾只有摘要，且若干 flag 名稱與完整腳本不一致 | GDD 9.4 加入逐 Scene 製作腳本；TDD 9.8 加入 route、schema、fixture、transaction 與 canonical flags；逐章 source mapping 固定到 `08_...` 至 `14_...` |
| Chapter state | C6 `c6_chain_valid` 沒有明確 set event；C2–C6 單章腳本未明寫 profile transaction | 補上正常 set／lock 規則；各章新增原子寫入、來源 flag→profile key mapping及未完成重玩不得覆寫 |
| Time-dependent biology | C3 舊句可能暗示移除 inducer 後 reporter 立即停止／消失 | 改為新產生／轉錄輸出開始下降，既有 reporter 依已表徵反應窗回到低背景 |
| Final timer | C8 的 duration flag 看似可由玩家獨立設定，browser suspension 可能造成跳時 | duration 只由 condition 的連續 fixed-step elapsed time 派生；illegal combinations 只供 QA fixture |
| Junior 3D metric | 以固定移動時間比例判定 3D 價值會鼓勵無意義走路 | 改為每個 learning gate 有有意義空間／因果操作，是否保留 3D 由目標玩家 transfer／usability 測試決定 |
| Unsupported WebGL2 | 舊 wording 容易被理解為已有完整自動 2D 遊戲 | 只承諾來源、逐字稿、靜態摘要、預錄 walkthrough 或受控展示，不稱為等價 2D build |
| Network/load | 「學校網路」沒有可重現 profile；25 MB C1 first load 沒有時間界線 | 新增 `10 Mbps down／2 Mbps up／100 ms RTT` cold-cache Lab profile、三台真實學校設備 run、C1 cold route ≤30 s、1 s 內 loading stage、cancel／retry及 QA cases |
| Source versions | GDD／Source Register 殘留舊 `TEAM-GCP-1.3`／`TEAM-CONTINUITY-1.2` | 更新為 `TEAM-GCP-1.4`／`TEAM-CONTINUITY-1.3`；logic validator 禁止 active docs 使用舊 ID |
| AI status | hosted API 可用、官方 open-model 描述與可下載權重 artifact 曾被混為同一狀態 | Kimi K3 改為：服務／Kimi Code／API 已可用；完整權重 artifact、commit、license及可部署 package 未經本審核獨立確認；不作 P0 相依 |
| Biology claims | MerR OFF、dTomato 與 aptamer 圖可能被寫成絕對零、即時定量或完整開關 | MerR/Pmer 僅作低背景、Hg²⁺ 依賴增加、延遲定性訊號；aptamer 路線保持 `NOT_APPROVED_FOR_PUBLIC_USE` |

## 4. 鏡頭與現行技術基線

| 領域 | 已鎖定基線 | 尚待真實證據 |
|---|---|---|
| Camera | `PerspectiveCamera`、yaw `45°`、down angle 約 `50°`、height `12 m`、ground offset `10 m`、vertical FOV `40°`（authoring 38–44°）、player Y `0.58`、pan half-life `0.20 s` | 三台學校機、720p、200% UI、遮擋、暈動與角色可讀性 |
| Camera behaviour | 隨位置平移；不隨面向旋轉；無 rotate／pitch／zoom／mouse-look／Q/E；authored focus 0.35–0.60 s，可取消；reduced motion 改 cut／fade | 目標玩家理解方向及 focus transition 舒適度 |
| Movement／interaction | screen-relative WASD／方向鍵；kinematic capsule；pointer 只選已註冊高亮目標；keyboard target cycle；無 jump／click-to-move／pathfinding | controller feel、碰撞、safe-anchor reset及 keyboard-only playthrough |
| Runtime | npm、TypeScript strict、Vite、Three.js | package versions、build reproducibility、browser matrix |
| UI／state | Preact＋`@preact/signals`、semantic DOM、typed reducer／explicit transition table、Zod | G1 maintainability／a11y spike |
| Physics | kinematic capsule；Rapier adapter 只作 spike；custom capsule／AABB 是明確 build fallback | WASM startup、memory、school proxy／MIME及碰撞品質 |
| Save | versioned localStorage summary＋JSON import/export；不存每幀或大型 world snapshot | migration、quota、corruption及 privacy walkthrough |
| Test | Vitest、Playwright、axe、content validators＋manual device／science／usability | 目標玩家、Science/Safety及實機證據 |
| Deployment | client-only static、無 backend／account／cloud save／public analytics；static＋offline local-server package P0；PWA P1 | hosting、base path、cache headers、rollback及 offline rehearsal |
| Future chapters | C2–C8 `future/**`，只可由 non-production build-time flag 開啟；production fail closed | 每章另立項、重新 source audit及容量批准 |

## 5. 第二至第八章完成範圍

| Chapter | GDD／TDD 已寫內容 | 2026 狀態 |
|---|---|---|
| C2 細胞工廠 | 生產層、四類品質教學、批次偏差、獨立放行、供應方案、profile transaction | Future design bible |
| C3 壞掉的開關 | LacI／Plac 故障、兩種修復、時間反應、失敗公開、profile transaction | Future design bible |
| C4 數據迷霧 | 問題預註冊、controls、replication、follow-up、outlier、bounded claim、data package | Future design bible |
| C5 離開實驗室之前 | PET scope、暴露路徑、封閉方案、成熟度、pilot governance、profile transaction | Future design bible |
| C6 誰能得到成果 | precursor／artemisinin／derivative／ACT 分層、雙來源鏈、衝擊、公平、合作社確認 | Future design bible |
| C7 雙面設計 | 風險維度、公開／受控／暫緩、事件 response、程序公平、profile object | Future design bible |
| C8 共同設計 | stakeholder requirements、baseline comparison、continuous-time latch、quality、access、pilot／no-pilot | Future design bible |

這些內容已足以建立 Future backlog、schema fixtures、content validators 與灰盒 issue，但**不是 2026 可玩章節承諾**，也不得進 P0 production manifest、bundle graph或 release QA enumeration。

## 6. 重驗命令

```bash
python tools/validate_v2_logic.py .
python tools/generate_manifest.py .
python tools/validate_production_pack.py .
sha256sum -c manifest.sha256
```

修改任何收錄檔案後，必須重新產生 manifest，再執行 structural validator 與 checksum。`0 errors／0 warnings` 只表示文件結構、已編碼規格及 checksum 一致，不代表科學、可玩性、效能、可及性、授權、未成年人研究或公開發行已批准。

## 7. 仍未關閉的 Gate

- 具名 Product、Tech、Science／Safety、Education／HP、Art、QA、Privacy Owner 與每週有效容量；
- MerR／Pmer 實際 construct、宿主、序列、background、response time、selectivity、matrix effect、LOD／LOQ 及安全資料；
- aptamer expression platform／actuator、序列架構、controls與證據；
- 三台學校設備與真實學校網路的 FPS、memory、loading、遮擋、keyboard-only及 200% UI 測試；
- 12–17 歲目標玩家理解度、完成率、誤解、暈動及 facilitator 依賴；Junior 另需 9–12 歲測試；
- 所有資產、字型、音訊、AI 生成內容、商標與 dependency license；
- hosting、offline launcher、rollback、研究同意、資料保存與 safeguarding。

## 8. 交付簽核

| 角色 | 姓名 | 日期 | 結論／例外 | 簽署 |
|---|---|---:|---|---|
| Product Owner |  |  |  |  |
| Delivery Owner |  |  |  |  |
| Technical Lead |  |  |  |  |
| Science Lead |  |  |  |  |
| Safety／HP／Education |  |  |  |  |
| Art／Asset Lead |  |  |  |  |
| QA Lead |  |  |  |  |
| Privacy／Safeguarding |  |  |  |  |
