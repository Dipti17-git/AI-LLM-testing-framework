# Retrieval vs Generation Failure Analysis

## Objective

When an AI application produces an incorrect or incomplete answer, the final response alone may not identify the actual source of the failure.

For RAG-based applications, I use a layered investigation approach.

## Investigation Flow

Source
↓
Retrieval
↓
Retrieved Context
↓
LLM Generation
↓
Response

### Step 1 - Source Validation

Verify whether the required information exists in the authoritative source.

### Step 2 - Retrieval Validation

Verify whether the relevant information was retrieved for the user's question.

### Step 3 - Context Validation

Verify whether the retrieved information was actually supplied to the model.

### Step 4 - Generation Validation

If the correct context reached the model, verify whether the generated response accurately reflects that context.

### Step 5 - Reproducibility

Repeat the scenario where appropriate to determine whether the behaviour is consistent or intermittent.

## Example: Retrieval Failure

Source:
Employees receive 25 vacation days annually.

Retrieved context:
Only remote-working information is retrieved.

AI response:
The available information does not specify the vacation allowance.

Assessment:

LLM behaviour: PASS

End-to-end system: FAIL

Likely failure area: Retrieval

## Example: Generation Failure

Source:
Employees receive 25 vacation days annually.

Retrieved context:
Employees receive 25 vacation days annually.

AI response:
Employees receive 30 vacation days annually.

Assessment:

LLM behaviour: FAIL

End-to-end system: FAIL

Likely failure area: Generation / Groundedness

## Key Testing Principle

A wrong end-user answer should not automatically be classified as an LLM hallucination.

The failure should be investigated across the source, retrieval, context and generation layers before assigning the defect to a component.
