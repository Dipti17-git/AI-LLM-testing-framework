# LLM Evaluation Criteria

## Objective

LLM responses should not be evaluated using exact text matching alone.
A response may vary in wording while still being acceptable, or appear
reasonable while containing unsupported or incomplete information.

This project evaluates AI responses across multiple quality dimensions.

## Evaluation Dimensions

### 1. Correctness
Determines whether the claims made by the AI are factually correct
according to the expected or authoritative information.

Example:
Context: Employees receive 25 vacation days annually.

AI:
"Employees receive 30 vacation days annually."

Result: FAIL

---

### 2. Groundedness
Determines whether important claims in the AI response are supported
by the supplied context.

A statement may be factually true but still be ungrounded if it is not
supported by the required source.

Example:
Context:
Employees receive 25 vacation days annually.

AI:
"Employees receive 25 vacation days annually.
Copenhagen is the capital of Denmark."

The Copenhagen statement may be factually correct but is not supported
by the supplied context.

Result: Groundedness FAIL

---

### 3. Relevance
Determines whether the response addresses the user's actual question.

Example:

User:
"How many vacation days do employees receive?"

AI:
"Employees may work remotely two days per week."

Result: FAIL

---

### 4. Completeness
Determines whether the response contains the critical information
required to answer the question correctly.

Example:

Context:
Employees may work remotely up to two days per week with manager approval.

AI:
"Employees may work remotely up to two days per week."

The response omits the manager approval requirement.

Result: FAIL

---

### 5. Faithfulness
Determines whether the generated response accurately represents the
context supplied to the model.

Example:

Retrieved context:
"Refund requests must be submitted within 14 days."

AI:
"Refund requests can be submitted within 30 days."

Result: FAIL

---

### 6. Unsupported Inference
Determines whether the model reaches a conclusion that does not logically
follow from the available information.

Example:

Policy:
Employees receive 25 vacation days annually.

User:
"Can I take seven days of vacation?"

The annual entitlement alone does not establish that the employee
currently has seven vacation days remaining.

The model should not approve the request without sufficient information.

---

## Claim-Level Evaluation

AI responses should be broken into individual claims where appropriate.

Example:

AI response:
"Employees receive 25 vacation days and can carry five unused days
into next year."

Claim 1:
Employees receive 25 vacation days.
Result: Supported

Claim 2:
Five unused days can be carried forward.
Result: Unsupported

Overall result: FAIL

## Key Testing Principles

- A factually true statement is not automatically grounded.
- A grounded response can still be incomplete.
- A relevant response can still contain incorrect information.
- Structural validity does not guarantee semantic correctness.
- Correct individual facts can still produce an unsupported conclusion.
- A wrong end-user answer does not automatically mean generation failed.
  Source, retrieval, context and generation should be investigated separately.
