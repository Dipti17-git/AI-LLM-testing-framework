

def build_hallucination_judge_prompt(context, response):

    prompt = f"""
 You are evaluating whether an AI response is not inventing facts when it doesnot have data.

 Context:
{context}

 Response:
{response}

 Evaluation criteria:
- HALLUCINATION if the response contains factual claims that are not supported by the context.
- NO HALLUCINATION if the factual claims in the response are supported by the context.
- NO HALLUCINATION if the response appropriately says that the requested information is not available in the context.
  is not available in the context
- Do not judge factual correctness and relevance here.
- Do not use outside knowledge.
- Judge hallucinations only.

 Return:
 Result: HALLUCINATION or NO HALLUCINATION
 Reason: short explanation
 """

    return prompt

class FakeHallucinationJudge:

    def generate(self, context,prompt):

        if "10 paid sick days" in prompt.lower() or "manager approval" in prompt.lower() or "registered home address" in prompt.lower():
            return (
                "Result: HALLUCINATION\n"
                "Reason: The response contains sick leave information that is not supported by the context."
            )

        return (
            "Result: NO HALLUCINATION\n"
            "Reason: The response does not contain unsupported information."
        )

def evaluate_hallucination_with_judge(judge_client, context, response):
        prompt = build_hallucination_judge_prompt(context, response)

        result = judge_client.generate(
            context="You are a hallucination evaluator.",
            prompt=prompt
        )

        return result