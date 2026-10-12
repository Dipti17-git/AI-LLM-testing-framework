import re

question = "How many vacation days can I carry over?"
response = "You can transfer five unused vacation days."

def evaluate_carryover_relevance(question,response):
    concept_groups = {
        "carry-over": ["carry over", "transfer", "roll over", "carry forward","carry-over"],
        "vacation": ["vacation", "leave"],
        "quantity": ["day", "days", "maximum", "up to"]
    }
    response_lower = response.lower()
    question_lower = question.lower()

    question_has_carryover = any(
        term in question_lower
        for term in concept_groups["carry-over"]
    )

    response_has_carryover = any(
        term in response_lower
        for term in concept_groups["carry-over"]
    )

    question_has_vacation = any(
        term in question_lower
        for term in concept_groups["vacation"]
    )

    response_has_vacation = any(
        term in response_lower
        for term in concept_groups["vacation"]
    )
    question_has_quantity = any(
        term in question_lower
        for term in concept_groups["quantity"]
    )

    response_has_quantity = any(
        term in response_lower
        for term in concept_groups["quantity"]
    )


    if question_has_carryover and response_has_carryover and question_has_vacation and response_has_vacation and question_has_quantity and response_has_quantity:
        return {
            "passed": True,
            "reason": "Response contains the expected carry-over rule"
        }

    return {
        "passed": False,
        "reason": "Response does not satisfy the expected carry-over rule"
    }

def build_relevance_judge_prompt(question, response):

    prompt = f"""
 You are evaluating whether an AI response is relevant to a user's question.

 Question:
{question}

 Response:
{response}

 Evaluation criteria:
- PASS if the response directly addresses what the user asked.
- FAIL if the response discusses the same topic but does not answer the requested information.
- Do not judge factual correctness here.
- Judge relevance only.

 Return:
 Result: PASS or FAIL
 Reason: short explanation
 """

    return prompt

class FakeRelevanceJudge:

 def generate(self, context, prompt):

        if "25 vacation days annually and carry-over is allowed" in prompt:
            return "Result: FAIL\nReason: The response does not provide the requested carry-over amount."

        return "Result: PASS\nReason: The response directly addresses the requested information."

def evaluate_relevance_with_judge(judge_client, question, response):
        prompt = build_relevance_judge_prompt(question, response)

        result = judge_client.generate(
            context="You are a relevance evaluator.",
            prompt=prompt
        )

        return result