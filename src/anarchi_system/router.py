from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class Signal:
    source: str
    kind: str
    confidence: float
    risk: float
    payload: Mapping[str, object]


@dataclass(frozen=True)
class Decision:
    action: str
    reason: str
    requires_ai: bool = False


def route_signal(signal: Signal) -> Decision:
    """Route a signal through deterministic gates before allowing AI escalation."""
    if not 0 <= signal.confidence <= 1:
        return Decision("reject", "confidence must be between 0 and 1")

    if not 0 <= signal.risk <= 1:
        return Decision("reject", "risk must be between 0 and 1")

    if signal.risk >= 0.8:
        return Decision("hold", "risk gate blocked automatic execution")

    if signal.confidence >= 0.75 and signal.risk <= 0.35:
        return Decision("execute", "deterministic confidence cleared action gate")

    if signal.confidence < 0.45:
        return Decision("escalate", "ambiguity remains after deterministic checks", requires_ai=True)

    return Decision("review", "signal is valid but needs operator review")

