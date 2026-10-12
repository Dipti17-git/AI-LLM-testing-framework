
from evaluation.consistency_evaluator import (
     FakeConsistencyJudge,
     evaluate_consistency_with_judge
)


def test_response_inconsistent():
    judge = FakeConsistencyJudge()

    response_a = "Employees receive 5 unused vacation days."
    response_b = "Employees receive 10 unused vacation days."

    result = evaluate_consistency_with_judge(
        judge,
        response_a,
        response_b
    )
    print(result)
    assert "Result: INCONSISTENT" in result

def test_response_consistent():
    judge = FakeConsistencyJudge()

    response_a = "Employees can carry over up to 5 unused vacation days."
    response_b =  "A maximum of five unused vacation days may be transferred to the next year."

    result = evaluate_consistency_with_judge(
        judge,
        response_a,
        response_b
    )
    print(result)
    assert "Result: CONSISTENT" in result

def test_response_inconsistent_1():
    judge = FakeConsistencyJudge()

    response_a = "Employees may work remotely up to 2 days per week with manager approval."
    response_b =  "Employees may work remotely up to 2 days per week without manager approval."

    result = evaluate_consistency_with_judge(
        judge,
        response_a,
        response_b
    )
    print(result)
    assert "Result: INCONSISTENT" in result



def evaluate_multiple_responses(judge, responses):
    responses = [
        "Employees receive 25 vacation days annually.",
        "The annual vacation entitlement is 25 days.",
        "Employees are entitled to twenty-five vacation days each year.",
        "Employees receive 20 vacation days annually.",
        "Staff receive 25 days of annual vacation."
    ]
    baseline = responses[0]
    results = []
    judge = FakeConsistencyJudge()
    for response in responses[1:]:
        result = evaluate_consistency_with_judge(
            judge,
            baseline,
            response
        )
        results.append(result)
    print(results)
    return results

def test_consistency_rate():
    judge = FakeConsistencyJudge()
    responses = [
        "Employees receive 25 vacation days annually.",
        "The annual vacation entitlement is 25 days.",
        "Employees are entitled to twenty-five vacation days each year.",
        "Employees receive 20 vacation days annually.",
        "Staff receive 25 days of annual vacation."
    ]
    consistency_count =0
    results = evaluate_multiple_responses(judge, responses)
    for result in results:
        if "Result: CONSISTENT" in result:
            consistency_count += 1
    consistency_rate = consistency_count / len(results)
    print(f"Consistency rate: {consistency_rate:.0%}")
    assert consistency_rate >= 0.6
