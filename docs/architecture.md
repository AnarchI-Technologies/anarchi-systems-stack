# Architecture

AnarchI systems are built around a simple operating rule:

> Deterministic systems act first. Real AI enters only when deterministic state declares that ambiguity remains.

## Control Flow

1. Capture a signal.
2. Normalize it into typed state.
3. Apply rules and gates.
4. Select an action, defer, or escalate.
5. Record the reason.
6. Expose a presentation-safe summary.

## Layer Responsibilities

### Signal Layer

Collects events from products, dashboards, agents, treasury tools, compliance workflows, and operator inputs.

### State Layer

Turns raw events into structured facts. This layer should be replayable and testable.

### Rule Layer

Applies deterministic policies, thresholds, cooldowns, and safety gates. It should answer: can the system act, should it wait, or does ambiguity require human or AI review?

### Execution Layer

Runs approved actions through adapters. Write-capable actions must pass explicit gates.

### Audit Layer

Stores the reasoning trail: inputs, selected rule, action, outcome, and rollback context.

### AI Escalation Layer

Handles synthesis, ambiguity, language-heavy reasoning, or classification only after deterministic checks decide the model is needed.

### Presentation Layer

Shows the operating picture to builders, operators, investors, and auditors without leaking private machinery.

