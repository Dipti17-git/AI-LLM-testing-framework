# AI-LLM-testing-framework
Hands-on AI/LLM testing portfolio covering functional testing, LLM evaluation, RAG testing, AI security and automated regression.
# AI/LLM Testing Framework

A hands-on portfolio project demonstrating my approach to testing AI and LLM-based applications.

## Project Objective

The objective of this project is to apply software quality engineering principles to AI/LLM applications and explore how testing changes when outputs are non-deterministic.

The project will progressively cover:

- LLM functional testing
- Prompt and instruction validation
- API automation using Python and pytest
- Groundedness and hallucination testing
- Golden dataset-based evaluation
- RAG testing and evaluation
- AI security and adversarial testing
- Automated AI regression testing

## Current Progress

### Day 1: LLM Testing Fundamentals

Topics covered:

- Traditional QA vs AI/LLM testing
- LLM, GenAI, prompt, model and inference
- Deterministic vs non-deterministic outputs
- Groundedness
- Unsupported assumptions
- Missing-information handling
- Claim-level response validation
- Converting AI instructions into testable requirements
- ### Day 2: LLM Configuration and Context Testing

Topics applied:

- Token and context-window fundamentals
- System vs user instruction testing
- Retrieval vs generation failure analysis
- Prompt injection testing
- Privacy instruction validation
- Repeated-output consistency concepts
- Boundary value analysis for LLM policy responses
- Ambiguous temporal input testing
- Golden dataset-based regression testing

Key testing principle:

A wrong AI response does not automatically indicate an LLM-generation defect. The source, retrieval, supplied context and generation layers should be investigated independently.
