import pytest

from evaluation.groundedness_evaluator import (

 FakeGroundednessJudge,
 evaluate_groundedness_with_judge

)

def test_response_groundedness():
    judge = FakeGroundednessJudge()

    context = "Employees receive 25 vacation days annually. Unused vacation days may be carried over, up to a maximum of 5 days."
    response = "You can carry over 5 days"


    result = evaluate_groundedness_with_judge(
        judge,
        context,
        response
    )
    print (result)
    assert "GROUNDED" in result

def test_response_not_grounded():
    judge = FakeGroundednessJudge()

    context = "Employees receive 25 vacation days annually. Unused vacation days may be carried over, up to a maximum of 5 days."
    response = "You can carry over 5 days with manager approval."


    result = evaluate_groundedness_with_judge(
        judge,
        context,
        response
    )
    print (result)
    assert "NOT GROUNDED" in result