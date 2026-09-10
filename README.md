# AI/LLM Testing Framework

A hands-on portfolio project demonstrating how traditional QA practices can be extended to test AI/LLM-powered applications.

The project uses a simulated HR policy assistant to demonstrate API automation, LLM response evaluation, negative testing, provider failure handling, performance validation and AI-specific behaviour testing.

## Current Capabilities

- REST API automation with Python, pytest and requests
- Positive and negative API testing
- Response contract and datatype validation
- Pytest fixtures and parameterization
- LLM response validation
- Missing-information and unsupported-answer testing
- Prompt-injection and privacy-sensitive testing
- LLM provider failure simulation
- Response-time and timeout validation
- Repeated-response consistency testing

## Tech Stack

Python | pytest | requests | FastAPI | Git | GitHub

## Project Structure

```text
app/          - HR assistant API
datasets/     - Test datasets
docs/         - Test strategy and evaluation documentation
evaluation/   - AI response evaluators
llm/          - LLM client
reports/      - Test reports
tests/        - Automated test suite
```

## Run the Project

Start the API:

```bash
uvicorn app.hr_api:app --reload
```

Run the tests:

```bash
python -m pytest -v
```

## Current Status

43 automated tests covering API validation, LLM integration, provider failures, performance checks and AI-specific behaviour.

## Next Steps

- Advanced LLM evaluation
- RAG testing and evaluation
- AI security testing
- Automated reporting
- CI/CD integration