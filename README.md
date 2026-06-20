# AnarchI Systems Stack

Polished public architecture for the AnarchI Technologies operating system.

Hardcoding freedom into the systems of tomorrow.

## Thesis

AnarchI builds deterministic systems so deeply layered, compiled, and context-aware that they feel intelligent. Real AI is not the hardcoded goal. It is an escalation layer used only when rules, state, and evidence determine that ambiguity remains.

This repository is the clean umbrella for the repaired standalone repos.

## System Layers

```text
Signal Layer        -> captures product, market, user, treasury, and system events
State Layer         -> normalizes events into typed, replayable state
Rule Layer          -> applies deterministic policy, thresholds, and gates
Execution Layer     -> runs approved automations and adapters
Audit Layer         -> preserves evidence, decisions, and rollback context
AI Escalation Layer -> handles ambiguity only after deterministic checks fail
Presentation Layer  -> dashboards, investor views, and operator controls
```

## Repaired Repo Map

| Repo | Role |
| --- | --- |
| `hive` | Coordination service for deterministic gates and status |
| `Autonomous-Agent-Hive` | Tested deterministic gatekeeper for agent actions |
| `core-dashboard` | Executive presentation surface with proof/validation strip |
| `Nexusv2` | Canonical integration and event-routing platform |
| `Nexus` | Legacy design-kit research retained for reference |
| `Core-DEK` | Tested deterministic execution kernel and distributed-control research path |
| `Core-Engine` | Rust resource/core engine with runtime-gated side effects |
| `Analytics-core` | Tested deterministic scorecards for operating metrics |
| `Automation-Engines` | Tested event bridge and dry-run-first action routing |
| `AI-systems-module` | Tested AI escalation policy boundary |
| `Compliance-Strategy-Matrix` | Tested audit records and control planning |
| `CRM-Software-Layer` | Tested consent-aware cadence core |
| `smart-CRM` | Legacy CRM prototype retained for reference |
| `marketing-systems-matrix` | Tested campaign router for reviewable growth operations |
| `Enjoyment-Scroler` | Tested public-safe scroll-session scoring prototype |
| `Visual_Systems` | Tested deterministic brand and asset generation package |
| `Stress-Test-Agent` | Tested readiness scoring for resilience evidence |
| `scriptsv1` | Governed operator-script registry |
| `anarchi-core` | Dry-run-first deterministic core policy surface |

## What This Repo Contains

```text
.
|-- docs/
|   |-- architecture.md
|   |-- repo-map.md
|   `-- public-safety.md
|-- src/anarchi_system/
|   |-- __init__.py
|   `-- router.py
|-- tests/
|   `-- test_router.py
|-- system_manifest.json
`-- README.md
```

## Verify

```bash
python -m unittest discover -s tests -q
```

## Public Safety

This repo is intentionally presentation-safe. It does not include credentials, runtime memory, account state, unreleased CERBERUS decision chains, private wallet data, or exact deterministic scoring formulas.
