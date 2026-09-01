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