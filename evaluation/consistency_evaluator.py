
def build_consistency_judge_prompt(response_a, response_b):


    prompt = f"""
 You are evaluating whether two AI responses are consistent.

 Response A:
{response_a}

 Response B:
{response_b}

 Evaluation criteria:
- CONSISTENT if both responses communicate the same essential meaning, even with different wording.
- INCONSISTENT if they contradict each other or provide materially different rules/facts.
- Do not require exact wording.
- Judge consistency only, not relevance or writing style.


 Return:
 Result: CONSISTENT or INCONSISTENT
 Reason: short explanation
 """

    return prompt

class FakeConsistencyJudge:

    def generate(self, context,prompt):

        if (("5 unused vacation days" in prompt.lower() and "10 unused vacation days" in prompt.lower())
                or ("with manager approval" in prompt.lower() and "without manager approval" in prompt.lower()))\
                or ("25 vacation days" in prompt.lower() and "20 vacation days" in prompt.lower()):
            return (
                "Result: INCONSISTENT\n"
                "Reason: The responses contain conflicting information."
            )

        return (
            "Result: CONSISTENT\n"
            "Reason: The responses are consistent."
        )

def evaluate_consistency_with_judge(judge_client, response_a, response_b):
        prompt = build_consistency_judge_prompt(response_a, response_b)

        result = judge_client.generate(
            context="You are a consistency evaluator.",
            prompt=prompt
        )

        return result