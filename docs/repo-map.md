# Repo Map

This map explains how the standalone AnarchI repositories should be understood after the Lyra Voss port repair work.

| Repository | Intended Responsibility | Current Direction |
| --- | --- | --- |
| `hive` | Coordination engine | Clean Go service with health/status and deterministic gates |
| `Autonomous-Agent-Hive` | Agent authority | Tested deterministic gatekeeper for agent actions |
| `core-dashboard` | Executive dashboard | Static presentation-safe dashboard shell with authored validator and proof strip |
| `Nexusv2` | Integration hub | Canonical Nexus path with a tested deterministic pipeline |
| `Nexus` | Earlier design kits | Legacy research, preserved as reference and pointed at `Nexusv2` |
| `Core-DEK` | Execution kit | Tested deterministic event kernel with AI/risk gates; historical cluster code retained as research |
| `Core-Engine` | Core resource engine | Rust runtime with dry-run/stress/debug launch gate and source-controlled Cargo lockfile |
| `Automation-Engines` | Action machinery | Tested deterministic event bridge with dry-run-first routing |
| `AI-systems-module` | AI boundary | Tested escalation policy: deterministic route first, model only for approved ambiguity |
| `Analytics-core` | Measurement | Tested deterministic scorecards plus operating reports with grade, bottleneck, and recommendation |
| `Compliance-Strategy-Matrix` | Governance | Tested public-safe audit records and control planning |
| `CRM-Software-Layer` | CRM workflow layer | Canonical tested consent-aware cadence and deterministic account planning core |
| `smart-CRM` | CRM prototype | Legacy research pointing to `CRM-Software-Layer` |
| `marketing-systems-matrix` | Growth operations | Tested campaign router plus deterministic launch plans with proof assets and blocked claims |
| `Enjoyment-Scroler` | UX research | Tested public-safe scroll-session scoring prototype |
| `Visual_Systems` | Brand systems | Tested deterministic visual identity package with clean build, package dry-run, and zero moderate audit findings |
| `anarchi-offer-engine` | Offer productization | Standalone standard-library package for deterministic starter/pro/studio offer ladders |
| `anarchi-proof-ledger-kit` | Evidence tooling | Standalone standard-library package for proof ledger entries and SHA-256 manifests |
| `Stress-Test-Agent` | Resilience | Tested readiness scoring plus existing stress harness fixtures |
| `scriptsv1` | Script staging | Governed script registry with dry-run/risk validation |
| `anarchi-core` | Core policy | Dry-run-first deterministic PowerShell policy surface |

## Consolidation Rule

If two repos solve the same problem, keep the one with the clearest production path and convert the other into docs, fixtures, or archived research.

