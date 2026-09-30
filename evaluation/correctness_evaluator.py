import re
def evaluate_vacation_correctness(response):

    acceptable_terms = {

        "has_vacation_context": [
            "vacation",
            "leave"
        ],

        "has_unsupported_rule": [
            "20 vacation days",
            "twenty vacation days",
            "some employees receive only 20",
            "some employees receive only twenty",
            "do not receive"
        ]
    }

    response_lower = response.lower()

    has_quantity = (
            re.search(r"\b25\b", response_lower) is not None
            or "twenty-five" in response_lower
    )

    has_vacation_context = any(
            term in response_lower
            for term in acceptable_terms["has_vacation_context"]
        )

    has_unsupported_rule = any(
            term in response_lower
            for term in acceptable_terms["has_unsupported_rule"]
        )

    has_wrong_quantity = (
            "20 vacation days" in response_lower
            or "twenty vacation days" in response_lower
    )

    if has_quantity and has_vacation_context and not has_wrong_quantity and not has_unsupported_rule:
     return {
        "passed": True,
        "reason": "Response contains the expected carry-over rule"
    }

    return {
    "passed": False,
    "reason": "Response does not satisfy the expected carry-over rule"
}


def build_evaluator_judge_prompt(answer, expected_behavior):


    prompt = f"""
 You are evaluating whether the AI response semantically satisfies  the expected behavior.

 Actual AI response:
{answer}

 Expected behavior:
{expected_behavior}

 Evaluation criteria:
- PASS if the AI response semantically satisfies  with the expected behaviour.
- FAIL if the AI response semantically does not satisfies  with the expected behaviour.
- Do not require exact wording.
- Judge based on meaning, not string similarity.


 Return:
 Result: PASS or FAIL
 Reason: short explanation
 """

    return prompt

class FakeCorrectnessJudge:

    def generate(self, context,prompt):


        print("\n----- JUDGE PROMPT -----")
        print(prompt)
        print("------------------------")

        if "Expected behavior:" not in prompt:
            return (
                "Result: FAIL\n"
                "Reason: Expected behavior is missing."
            )

        return (
            "Result: PASS\n"
            "Reason: Simulated semantic evaluation passed."
        )

def evaluate_correctness(judge_client, expected_behavior, answer):
    prompt = build_evaluator_judge_prompt(answer, expected_behavior)

    result = judge_client.generate(
        context="You are a correctness evaluator.",
        prompt=prompt
    )

    return result