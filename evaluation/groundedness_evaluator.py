

def build_groundedness_judge_prompt(context, response):

 prompt = f"""
 You are evaluating whether an AI response is grounded in the provided context.

 Context:
{context}

 Response:
{response}

 Evaluation criteria:
- GROUNDED if every factual claim in the response is supported by the context.
- NOT GROUNDED if the response contains any factual claim that is not supported by the context.
- NOT GROUNDED if the response contradicts the context.
- Do not judge relevance.
- Do not use outside knowledge.
 
Return:
Result: GROUNDED or NOT GROUNDED
Reason: short explanation
 """
 return prompt

class FakeGroundednessJudge:

    def generate(self, context, prompt):

        if "manager approval" in prompt.lower():
            return (
                "Result: NOT GROUNDED\n"
                "Reason: Manager approval is not supported by the provided context."
            )

        return (
            "Result: GROUNDED\n"
            "Reason: The response is supported by the provided context."
        )

def evaluate_groundedness_with_judge(judge_client, question, response):
        prompt = build_groundedness_judge_prompt(question, response)

        result = judge_client.generate(
            context="You are a groundedness evaluator.",
            prompt=prompt
        )

        return result