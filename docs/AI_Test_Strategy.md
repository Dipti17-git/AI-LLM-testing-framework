# AI/LLM Test Strategy

## Objective

The objective of this testing approach is to evaluate whether an LLM-based application produces responses that are accurate, relevant, grounded in the provided context, and compliant with system instructions.

## Testing Approach

Unlike traditional deterministic applications, LLM applications may produce different valid responses for the same input.

Therefore, testing should evaluate both deterministic properties and semantic quality.

## Key Validation Areas

### Functional Validation

Validate whether the model follows the application's defined requirements and instructions.

### Groundedness

Validate whether factual claims made by the model are supported by the provided context or source information.

### Missing Information

Validate whether the model appropriately identifies when sufficient information is unavailable rather than generating unsupported answers.

### Unsupported Inference

Validate whether the model makes conclusions that are not explicitly supported by the available information.

### Privacy

Validate whether the model protects restricted or personal information according to its instructions.

### Boundary and Negative Testing

Validate model behaviour when receiving ambiguous, incomplete, conflicting or unsupported questions.

## Test Design Principle

Each AI response should be evaluated at claim level rather than treating the complete response as correct simply because most of the answer is accurate.

Important factual claims should be traceable to the supplied source or context when the model is instructed to answer only from that information.
# AI Assistant API Test Strategy

## Objective

Validate the API and AI behaviour of an HR policy assistant that accepts
policy context and a user prompt and returns an AI-generated answer.

The testing approach separates traditional API validation from AI-specific
response evaluation.

---

## System Under Test

Endpoint:

POST /api/chat

Example request:

{
  "context": "Employees receive 25 vacation days annually.",
  "prompt": "How many vacation days do employees receive?"
}

Example response:

{
  "answer": "Employees receive 25 vacation days annually.",
  "model": "mock-hr-assistant"
}

---

## Test Layers

### 1. HTTP Validation

Validate:

- HTTP status codes
- Request processing
- Error handling
- Response availability
- Request timeout

### 2. Schema Validation

Validate:

- answer field exists
- model field exists
- expected datatypes
- mandatory fields
- malformed or incomplete requests

### 3. Input Validation

Test:

- valid context and prompt
- missing prompt
- empty prompt
- whitespace-only prompt
- missing context
- empty context

### 4. AI Content Validation

Validate that:

- response is non-empty
- answer reflects supplied context
- unsupported information is not invented
- missing information is handled appropriately

### 5. AI Security and Behaviour

Validate scenarios including:

- prompt injection
- instruction override
- privacy-sensitive requests
- unsupported assumptions

---

## Automation Approach

Python, requests and pytest are used for API automation.

Pytest parameterization is used to execute the same validation logic
against multiple input datasets.

Fixtures are used for reusable test configuration such as the API base URL.

Example:

@pytest.fixture
def base_url():
    return "http://127.0.0.1:8000"

---

## Failure Classification

An automated test failure should not automatically be classified as an
LLM defect.

Failures are investigated across the following layers:

1. Test code/setup
2. Test data
3. HTTP/API layer
4. Response schema
5. Application/integration layer
6. AI/model behaviour
7. Evaluation logic

For example, HTTP 200 with an empty answer indicates that transport
succeeded but content validation failed. Further investigation is required
before attributing the issue to the LLM.

---

## Key Quality Principle

API success does not imply AI success.

A response can have:

- HTTP PASS
- Schema PASS
- Content presence PASS
- AI semantic FAIL

Therefore AI applications require both traditional API validation and
AI-specific semantic evaluation.
