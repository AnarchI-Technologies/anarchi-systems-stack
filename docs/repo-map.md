# Repo Map

This map explains how the standalone AnarchI repositories should be understood after the Lyra Voss port repair work.

| Repository | Intended Responsibility | Current Direction |
| --- | --- | --- |
| `hive` | Coordination engine | Clean Go service with health/status and deterministic gates |
| `Autonomous-Agent-Hive` | Agent authority | Tested deterministic gatekeeper for agent actions |
| `core-dashboard` | Executive dashboard | Static presentation-safe dashboard shell |
| `Nexusv2` | Integration hub | Canonical Nexus path with a tested deterministic pipeline |
| `Nexus` | Earlier design kits | Legacy research, preserved as reference and pointed at `Nexusv2` |
| `Core-DEK` | Execution kit | Simulation and distributed control-plane experiments |
| `Automation-Engines` | Action machinery | Tested deterministic event bridge with dry-run-first routing |
| `AI-systems-module` | AI boundary | Tested escalation policy: deterministic route first, model only for approved ambiguity |
| `Analytics-core` | Measurement | Tested deterministic scorecards for public-safe operating metrics |
| `Compliance-Strategy-Matrix` | Governance | Tested public-safe audit records and control planning |
| `CRM-Software-Layer` | CRM workflow layer | Canonical tested consent-aware cadence core |
| `smart-CRM` | CRM prototype | Legacy research pointing to `CRM-Software-Layer` |
| `marketing-systems-matrix` | Growth operations | Tested campaign router with investor review and claim-safety routing |
| `Enjoyment-Scroler` | UX research | Tested public-safe scroll-session scoring prototype |
| `Visual_Systems` | Brand systems | Deterministic visual identity and asset generation |
| `Stress-Test-Agent` | Resilience | Tested readiness scoring plus existing stress harness fixtures |

## Consolidation Rule

If two repos solve the same problem, keep the one with the clearest production path and convert the other into docs, fixtures, or archived research.

