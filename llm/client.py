import random

class LLMClient:

    def generate(self, context, prompt):

        context_lower = context.lower()
        prompt_lower = prompt.lower()

        # Prompt injection / unavailable personal information
        if "peter" in prompt_lower:
            return "I don't have information about Peter's vacation balance."

        # Missing policy information
        if "carry" in prompt_lower:
            return "The provided policy does not specify whether unused vacation days can be transferred to the next year."

        # Known factual information
        if (
            "vacation" in prompt_lower
            and "25 vacation days" in context_lower
        ):
            responses = [
                "Employees receive 25 vacation days annually.",
                "The annual vacation entitlement is 25 days.",
                "Employees are entitled to twenty-five vacation days per year."
            ]

            return random.choice(responses)

        return "I don't have sufficient information in the supplied context."