
from evaluation.Hallucination_evaluator import (
     FakeHallucinationJudge,
     evaluate_hallucination_with_judge
)

def test_response_hallucination():
    judge = FakeHallucinationJudge()

    context = "Employees receive 25 vacation days annually."

    response = (
        "Employees working remotely are expected to work from their registered home address."
    )


    result = evaluate_hallucination_with_judge(
        judge,
        context,
        response
    )
    print (result)
    assert "Result: HALLUCINATION" in result

def test_response_not_hallucination():
    judge = FakeHallucinationJudge()

    context = "Employees receive 25 vacation days annually."

    response = (
        "The provided information does not specify how many paid sick days employees receive."

    )
    result = evaluate_hallucination_with_judge(
        judge,
        context,
        response
    )
    print (result)
    assert "Result: NO HALLUCINATION" in result