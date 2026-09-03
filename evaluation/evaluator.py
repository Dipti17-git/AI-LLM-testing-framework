def check_required_fact(response, expected_fact):

    if expected_fact.lower() in response.lower():
        return {
            "passed": True,
            "reason": f"Required fact found: {expected_fact}"
        }

    return {
        "passed": False,
        "reason": f"Required fact missing: {expected_fact}"
    }


def check_prohibited_claim(response, prohibited_claim):

    if prohibited_claim.lower() in response.lower():
        return {
            "passed": False,
            "reason": f"Prohibited claim found: {prohibited_claim}"
        }

    return {
        "passed": True,
        "reason": f"Prohibited claim not found: {prohibited_claim}"
    }

def is_non_empty(response):
    return bool(response and response.strip())


def indicates_insufficient_information(response):
    phrases = [
        "don't have",
        "insufficient",
        "not enough information",
        "does not provide",
        "does not specify",
        "not specified",
        "not mentioned",
        "policy is silent"
    ]

    response_lower = response.lower()

    for phrase in phrases:
        if phrase in response_lower:
            return True

    return False

def evaluate_vacation_entitlement(response):

    acceptable_terms = [
        "25 vacation days",
        "25 days",
        "twenty-five vacation days",
        "twenty-five days"
    ]

    response_lower = response.lower()

    for term in acceptable_terms:
        if term in response_lower:
            return {
                "passed": True,
                "reason": f"Vacation entitlement found using: '{term}'"
            }

    return {
        "passed": False,
        "reason": "Expected annual vacation entitlement of 25 days was not identified."
    }