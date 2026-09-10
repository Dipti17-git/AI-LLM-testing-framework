# AI/LLM API Test Strategy – HR Assistant

## Objective

Validate the API and AI behaviour of an HR policy assistant that accepts
policy context and a user prompt and returns an AI-generated response.

The testing approach combines traditional API validation with AI-specific
response evaluation.

## Scope

Testing covers:

- API functionality
- Input validation
- Response contract validation
- LLM/provider failure handling
- Response time and timeout behaviour
- Missing-information handling
- Prompt injection and privacy-sensitive scenarios
- AI response evaluation

## API Validation

For POST `/api/chat`, automated tests validate:

- HTTP status codes
- JSON responses
- Required `answer` and `model` fields
- Expected datatypes
- Non-empty responses
- Missing context or prompt
- Empty and whitespace-only inputs
- Error response structure

## AI Behaviour Validation

AI responses are evaluated for:

- Correctness
- Groundedness against supplied context
- Missing information
- Unsupported inference
- Response consistency
- Prompt-injection behaviour
- Sensitive-information disclosure

AI responses are evaluated against expected behaviour rather than relying
only on exact-string matching.

## Provider and Failure Testing

Provider failures are simulated using a failing LLM client.

Tests verify that:

- Provider exceptions are handled
- Failures do not unexpectedly crash the application
- Error information is logged
- Provider failures are distinguished from AI-quality failures

## Performance Validation

API response time is measured against a configurable threshold.

The tests distinguish between:

- Response-time requirement
- Technical request timeout

An HTTP 200 response can therefore still fail the performance requirement.

## Automation Approach

The framework uses:

- Python
- pytest
- requests
- FastAPI
- pytest fixtures
- pytest parameterization

Reusable fixtures are used for common test setup and test data.

## Failure Classification

Failures are investigated across:

1. Test code/setup
2. Test data
3. API/environment
4. Request validation
5. Response contract
6. LLM/provider
7. AI response behaviour
8. Evaluation logic
9. Performance

A successful API response does not automatically mean that the AI response
is correct.

## Current Status

The automated regression suite currently contains 43 passing tests covering
API, integration, performance and AI-specific behaviour.

Future iterations will extend the framework with more advanced LLM
evaluation, RAG testing and AI security testing.