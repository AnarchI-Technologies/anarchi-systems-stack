# Repo Map

This map explains how the standalone AnarchI repositories should be understood after the Lyra Voss port repair work.

| Repository | Intended Responsibility | Current Direction |
| --- | --- | --- |
| `hive` | Coordination engine | Clean Go service with health/status and deterministic gates |
| `core-dashboard` | Executive dashboard | Static presentation-safe dashboard shell |
| `Nexusv2` | Integration hub | Canonical Nexus path with a tested deterministic pipeline |
| `Nexus` | Earlier design kits | Legacy research, preserved as reference and pointed at `Nexusv2` |
| `Core-DEK` | Execution kit | Simulation and distributed control-plane experiments |
| `Automation-Engines` | Action machinery | Event bridge and operator automation primitives |
| `AI-systems-module` | AI boundary | Tested escalation policy: deterministic route first, model only for approved ambiguity |
| `Analytics-core` | Measurement | Metrics, reports, and sourced decision support |
| `Compliance-Strategy-Matrix` | Governance | Policy, control, and treasury audit ideas |
| `CRM-Software-Layer` | CRM workflow layer | Relationship cadence and workflow state |
| `smart-CRM` | CRM prototype | Consolidate into CRM layer after tests |
| `marketing-systems-matrix` | Growth operations | Campaign routing and measurement hooks |
| `Visual_Systems` | Brand systems | Deterministic visual identity and asset generation |
| `Stress-Test-Agent` | Resilience | Break/fix/test harnesses and scenario evidence |

## Consolidation Rule

If two repos solve the same problem, keep the one with the clearest production path and convert the other into docs, fixtures, or archived research.

