#!/usr/bin/env python3
"""Cross-document logic checks for the v2 fixed-isometric / C2-C8 baseline."""
from __future__ import annotations
import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class Finding:
    severity: str
    check: str
    file: str
    detail: str


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('root', nargs='?', default=str(Path(__file__).resolve().parents[1]))
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()
    root = Path(args.root).resolve()
    findings: list[Finding] = []

    def text(rel: str) -> str:
        p = root / rel
        if not p.is_file():
            findings.append(Finding('ERROR','required-file',rel,'missing'))
            return ''
        return p.read_text(encoding='utf-8')

    docs = {p.relative_to(root).as_posix(): p.read_text(encoding='utf-8') for p in root.rglob('*.md')}
    gdd = text('02_GAME_DESIGN_DOCUMENT.md')
    tdd = text('03_TECHNICAL_DESIGN_DOCUMENT.md')
    dec = text('20_OPEN_DECISIONS_REGISTER.md')
    readme = text('README_START_HERE.md')
    c6 = text('12_CHAPTER_06_FULL_SCRIPT.md')

    for rel in ['24_LOGIC_CAMERA_AND_CHAPTER_2_8_AUDIT.md','16_FULL_SCRIPT_REVIEW_AUDIT.md','tools/validate_v2_logic.py']:
        if not (root/rel).is_file():
            findings.append(Finding('ERROR','required-file',rel,'missing'))

    camera_tokens = [
        'IsometricPerspectiveRig','yawDeg: 45','downwardAngleDeg: 50',
        'vertical FOV','targetScreenY','0=top, 1=bottom','panHalfLifeS',
        'moveLookAheadM','CameraOccluder','DebugFreeCam','click-to-move',
        'screen-space proximity','production tree-shaken'
    ]
    for token in camera_tokens:
        if token not in tdd:
            findings.append(Finding('ERROR','camera-contract','03_TECHNICAL_DESIGN_DOCUMENT.md',f'missing {token}'))
    for token in ['固定方向的斜俯視透視鏡頭','隨玩家位置作平滑平移','不跟隨角色面向','FOV `40°`','≥1.8 m']:
        if token not in gdd:
            findings.append(Finding('ERROR','camera-gdd','02_GAME_DESIGN_DOCUMENT.md',f'missing {token}'))

    forbidden_global = [
        'ThirdPersonRig','CameraBlocker','cameraSensitivity:','cameraAssist:',
        '192–202','至少 40%','新 reporter 表達先停止','| FIN |',
        'GDD 1.0／TDD 1.0','https://platform.kimi.ai/docs/guide/kimi-k3-quickstart',
        'point-and-click fallback','TEAM-GCP-1.3','TEAM-CONTINUITY-1.2',
        '已上線，並描述為已發布／開源'
    ]
    # Historical audit documents may quote the exact stale wording they supersede.
    active_docs = {k:v for k,v in docs.items() if k not in {'01_GCP_REVIEW_AUDIT.md','23_DELIVERY_VALIDATION_REPORT.md','24_LOGIC_CAMERA_AND_CHAPTER_2_8_AUDIT.md'} and not k.startswith('_original_templates/')}
    joined = '\n'.join(f'@@{k}\n{v}' for k,v in active_docs.items())
    for token in forbidden_global:
        if token in joined:
            findings.append(Finding('ERROR','forbidden-stale','*.md',token))

    # Old GCP references are allowed only in the explicitly historical audit.
    for rel, body in docs.items():
        if rel in {'01_GCP_REVIEW_AUDIT.md'} or rel.startswith('_original_templates/'):
            continue
        if re.search(r'(對應 GCP \|.*(?:1\.3)|對應 GCP 1\.3|GCP 1\.3)', body):
            findings.append(Finding('ERROR','stale-gcp-ref',rel,'current document still references GCP 1.3'))

    invented = [
        'c2_batch_isolated','c2_product_layers_valid','c2_process_chain_valid','c2_access_needs_valid','c2_new_batch_valid',
        'c3_incident_seen','c3_expected_states_valid','c3_components_mapped','c3_faults_identified','c3_validation_complete',
        'c4_conflict_seen','c4_raw_data_reviewed','c4_outlier_handling_valid','c4_package_valid',
        'c5_overclaim_flagged','c5_exposure_map_valid',
        'c6_stakeholders_restored','c6_supply_chains_valid','c6_shocks_reviewed','c6_metrics_valid',
        'c7_cases_loaded','f_problem_context_seen'
    ]
    for token in invented:
        if token in gdd or token in tdd:
            findings.append(Finding('ERROR','invented-flag','GDD/TDD',token))

    canonical = {
        'c2':['c2_cells_product_separated','c2_process_order_valid','c2_quality_identity','c2_quality_purity','c2_quality_function','c2_quality_consistency','c2_batch_decision','c2_root_cause_valid','c2_statement_valid','c2_access_plan','p_c2_batch','p_c2_access'],
        'c3':['c3_expected_behavior','c3_fault_repressor','c3_fault_reporter_leak','c3_repair_strategy','c3_truth_table_valid','c3_failure_reported','p_c3_repair'],
        'c4':['c4_prior_repair_loaded','c4_question','c4_controls_valid','c4_replication_valid','c4_followup_plan_locked','c4_followup_complete','c4_outlier_handled','c4_conclusion_valid','c4_data_package_complete','p_c4_question'],
        'c5':['c5_release_rejected','c5_claim_scope_valid','c5_pathways_mapped','c5_contained_strategy','c5_evidence_ladder_valid','c5_lifecycle_choice','c5_public_statement_valid','p_c5_containment','p_c5_pilot'],
        'c6':['c6_missing_people_found','c6_chain_valid','c6_shock_response_valid','c6_access_metrics','c6_strategy','c6_transition_plan','c6_statement_valid','p_c6_supply','p_c6_transition'],
        'c7':['c7_risk_dimensions_valid','c7_case_education','c7_case_environment','c7_access_controls_valid','c7_case_unverified','c7_incident_response_valid','c7_public_summary_valid','p_c7_access'],
        'c8':['f_problem_statement_valid','f_stakeholder_conditions_confirmed','f_comparison_plan_valid','f_latched_state_valid','f_controls_valid','f_edge_cases_valid','f_quality_release_valid','f_access_choice','f_open_package_valid','f_solution_architecture','f_pilot_plan_valid','f_final_statement_valid','p_final_architecture','p_final_access']
    }
    for ch, tokens in canonical.items():
        for tok in tokens:
            for rel, body in [('02_GAME_DESIGN_DOCUMENT.md',gdd),('03_TECHNICAL_DESIGN_DOCUMENT.md',tdd)]:
                if tok not in body:
                    findings.append(Finding('ERROR','canonical-flag',rel,f'{ch}: missing {tok}'))

    source_map = [
        '08_CHAPTER_02_FULL_SCRIPT.md','09_CHAPTER_03_FULL_SCRIPT.md','10_CHAPTER_04_FULL_SCRIPT.md',
        '11_CHAPTER_05_FULL_SCRIPT.md','12_CHAPTER_06_FULL_SCRIPT.md','13_CHAPTER_07_FULL_SCRIPT.md','14_FINAL_CHAPTER_FULL_SCRIPT.md'
    ]
    for rel in source_map:
        if rel not in gdd or rel not in tdd:
            findings.append(Finding('ERROR','source-map','GDD/TDD',rel))

    for token in ['production manifest','P0 QA surface','future-preview','fail closed']:
        if token not in gdd and token not in tdd:
            findings.append(Finding('ERROR','future-exclusion','GDD/TDD',f'missing {token}'))

    profile_contracts = {
        '08_CHAPTER_02_FULL_SCRIPT.md':['p_c2_batch = c2_batch_decision','p_c2_access = c2_access_plan'],
        '09_CHAPTER_03_FULL_SCRIPT.md':['p_c3_repair = c3_repair_strategy'],
        '10_CHAPTER_04_FULL_SCRIPT.md':['p_c4_question = c4_question'],
        '11_CHAPTER_05_FULL_SCRIPT.md':['p_c5_containment = c5_contained_strategy','p_c5_pilot = c5_lifecycle_choice'],
        '12_CHAPTER_06_FULL_SCRIPT.md':['p_c6_supply = c6_strategy','p_c6_transition = c6_transition_plan'],
    }
    for rel, tokens in profile_contracts.items():
        body = text(rel)
        for token in tokens:
            if token not in body:
                findings.append(Finding('ERROR','profile-transaction',rel,f'missing {token}'))

    if '`c6_chain_valid = true`' not in c6 or 'S02 保持鎖定' not in c6:
        findings.append(Finding('ERROR','c6-gate','12_CHAPTER_06_FULL_SCRIPT.md','c6_chain_valid set/lock rule missing'))
    if 'artemisinic_acid_precursor' not in c6 or 'ACT_product' not in c6:
        findings.append(Finding('ERROR','c6-schema','12_CHAPTER_06_FULL_SCRIPT.md','canonical entity enums missing'))

    if 'Baseline v2.0' not in dec:
        findings.append(Finding('ERROR','decision-status','20_OPEN_DECISIONS_REGISTER.md','Baseline v2.0 definition missing'))
    for did in ['DEC-TECH-001','DEC-TECH-002','DEC-TECH-003','DEC-TECH-005','DEC-TECH-006','DEC-TECH-007','DEC-TECH-009','DEC-TECH-010','DEC-TECH-020','DEC-UX-006']:
        line = next((x for x in dec.splitlines() if x.startswith(f'| {did} |')), '')
        if 'Baseline v2.0' not in line:
            findings.append(Finding('ERROR','decision-baseline','20_OPEN_DECISIONS_REGISTER.md',did))

    if '2D／video fallback decision' in tdd or 'unsupported page／2D fallback decision' in tdd:
        findings.append(Finding('ERROR','unsupported-fallback','03_TECHNICAL_DESIGN_DOCUMENT.md','ambiguous automatic 2D fallback remains'))

    if 'NOT_APPROVED_FOR_PUBLIC_USE' not in text('22_SOURCE_AND_CLAIM_REGISTER.md'):
        findings.append(Finding('ERROR','aptamer-boundary','22_SOURCE_AND_CLAIM_REGISTER.md','aptamer public-use block missing'))


    # Network/load claims must be reproducible rather than a vague "school network" promise.
    for token in ['10 Mbps down／2 Mbps up／100 ms RTT','C1 first cold route','≤30 s acceptable','DEV-BASELINE-01..03']:
        if token not in tdd:
            findings.append(Finding('ERROR','network-load-contract','03_TECHNICAL_DESIGN_DOCUMENT.md',f'missing {token}'))

    qa = text('06_QA_TEST_PLAN.md')
    for token in ['QA-PERF-006','QA-NET-001','10 Mbps down／2 Mbps up／100 ms RTT','C1 cold≤30 s']:
        if token not in qa:
            findings.append(Finding('ERROR','qa-network-contract','06_QA_TEST_PLAN.md',f'missing {token}'))

    # Kimi status must separate hosted availability from independently verified weight artifacts.
    ai = text('19_AI_ASSISTED_DEVELOPMENT_PLAYBOOK.md')
    for token in ['服務、Kimi Code 與 API 已可使用','完整權重預定於 2026-07-27','未獨立確認確切 weight package']:
        if token not in ai:
            findings.append(Finding('ERROR','ai-status-boundary','19_AI_ASSISTED_DEVELOPMENT_PLAYBOOK.md',f'missing {token}'))
    if ai.count('所有圖表永久顯示 `教學模擬 / Teaching simulation` 與 maturity tag') != 1:
        findings.append(Finding('ERROR','duplicate-science-rule','19_AI_ASSISTED_DEVELOPMENT_PLAYBOOK.md','simulation watermark rule must appear exactly once'))

    # Duplicate ATX headings in the two main documents are usually copy/paste defects.
    for rel, body in [('02_GAME_DESIGN_DOCUMENT.md',gdd),('03_TECHNICAL_DESIGN_DOCUMENT.md',tdd)]:
        headings = [m.group(0).strip() for m in re.finditer(r'^#{1,6}\s+.+$', body, re.M)]
        for h in sorted(set(headings)):
            if headings.count(h) > 1:
                findings.append(Finding('ERROR','duplicate-heading',rel,h))

    # Control characters except newline, tab and carriage return.
    for rel, body in docs.items():
        bad = [ord(ch) for ch in body if ord(ch) < 32 and ch not in '\n\r\t']
        if bad:
            findings.append(Finding('ERROR','control-char',rel,str(sorted(set(bad)))))

    errors = sum(f.severity == 'ERROR' for f in findings)
    warnings = sum(f.severity == 'WARNING' for f in findings)
    result = {'root':str(root),'errors':errors,'warnings':warnings,'findings':[asdict(f) for f in findings]}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f'Logic validator: {errors} errors, {warnings} warnings')
        for f in findings:
            print(f'[{f.severity}] {f.check} {f.file}: {f.detail}')
    return 1 if errors else 0

if __name__ == '__main__':
    raise SystemExit(main())
