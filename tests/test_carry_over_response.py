import pytest
from evaluation.relevance_evaluator import (
 evaluate_carryover_relevance,
 build_relevance_judge_prompt,
 FakeRelevanceJudge,
 evaluate_relevance_with_judge


)

@pytest.mark.parametrize("response,expected", [
    ("1. You can transfer five unused vacation days.", True),
    ("2. Employees receive 25 vacation days annually.", False),
    ("3. You can transfer 10 vacation days.", True),
    ("4. Employees have 25 vacation days annually and carry-over is allowed.", False)
 ])

def test_vacation_correctness(response, expected):
    # result = evaluate_vacation_correctness(response)
    question = "How many vacation days can I carry over?"
    result = evaluate_carryover_relevance(question, response)
    assert result["passed"] == expected

def test_build_relevance_judge_prompt():
    question = "How many vacation days can I carry over?"
    response = "You can transfer five unused vacation days."

    prompt = build_relevance_judge_prompt(question, response)
    assert question in prompt
    assert response in prompt
    print(prompt)

def test_relevance_judge_relevant_response():
    judge = FakeRelevanceJudge()

    question = "How many vacation days can I carry over?"
    response = "You can transfer five unused vacation days."

    result = evaluate_relevance_with_judge(
        judge,
        question,
        response
    )

    assert "Result: PASS" in result

def test_relevance_judge_irrelevant_response():
    judge = FakeRelevanceJudge()

    question = "How many vacation days can I carry over?"
    response = "Employees have 25 vacation days annually and carry-over is allowed."

    result = evaluate_relevance_with_judge(
        judge,
        question,
        response
    )

    assert "Result: FAIL" in result
