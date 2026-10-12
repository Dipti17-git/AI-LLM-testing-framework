import pytest

scenario = [{
    "id": "NEG-RAG-001",
    "question": "How many paid parental-leave weeks do employees receive?",
    "retrieved_chunks": [
        "Employees receive 25 vacation days annually."
    ],
    "generated_answer": "Employees receive 25 weeks of paid parental leave.",
    "unsupported_text": [
        "25 weeks"
    ],
    "expected_unsupported": True

} ]
scenario1 = [{
    "id": "NEG-RAG-002",
    "question": "How many paid parental-leave weeks do employees receive?",
    "retrieved_chunks": [
        "Employees may carry over a maximum of 5 unused vacation days.",
        "Contractors may carry over a maximum of 2 unused leave days."
    ],
    "generated_answer": "Employees may carry over a maximum of 2 unused vacation days.",
    "required_information": [
         "5 unused vacation days"
    ],
    "expected_required": False

}]

scenario2 = [{
    "id": "NEG-RAG-003",
    "question": "How many unused vacation days can employees carry over?",
    "retrieved_chunks": [
        "Vacation Policy 2024: Employees may carry over 10 unused vacation days.",
        "Vacation Policy 2026 CURRENT: Employees may carry over 5 unused vacation days."
    ],
    "generated_answer":
        "Employees may carry over 10 unused vacation days.",
    "current_information": [
        "5 unused vacation days"
    ],
    "expected_current": False
}]

scenario3 = [{
    "id": "NEG-RAG-004",
    "question": "How many unused vacation days can employees carry over?",
    "retrieved_chunks": [
        "Policy A: Employees may carry over a maximum of 5 unused vacation days.",
        "Policy B: Employees may carry over a maximum of 10 unused vacation days."
    ],
    "generated_answer":
        "Employees may carry over a maximum of 5 unused vacation days.",
    "required_conflict_response": [
        "conflicting"
    ],
    "expected_conflict_handled": False
}]

def contains_unsupported_information(
    generated_answer,
    unsupported_text
):
    return any(phrase in generated_answer for phrase in unsupported_text)

@pytest.mark.parametrize("scenario", scenario)
def test_rag_negative(scenario):
    assert scenario["expected_unsupported"] == contains_unsupported_information(scenario["generated_answer"], scenario["unsupported_text"])


def contains_required_information(
    generated_answer,
    required_information
):
    return all(phrase in generated_answer for phrase in required_information)

@pytest.mark.parametrize("scenario", scenario1)
def test_rag_required(scenario):
    assert scenario["expected_required"] == contains_required_information(scenario["generated_answer"], scenario["required_information"])

def contains_current_information(
            generated_answer,
            current_information
    ):
        return all(phrase in generated_answer for phrase in current_information)

@pytest.mark.parametrize("scenario", scenario2)
def test_rag_currentInfo(scenario):
        assert scenario["expected_current"] == contains_current_information(scenario["generated_answer"],
                                                                              scenario["current_information"])


def contains_conflict_information(
        generated_answer,
        required_conflict_response
):
    return all(phrase in generated_answer for phrase in required_conflict_response)


@pytest.mark.parametrize("scenario", scenario3)
def test_rag_conflict(scenario):
    assert scenario["expected_conflict_handled"] == contains_conflict_information(scenario["generated_answer"],
                                                                        scenario["required_conflict_response"])

scenario4 = [{
    "id": "NEG-RAG-005",
    "question": "How many unused vacation days can employees carry over?",
    "retrieved_chunks": [
            {
        "policy": "vacation",
        "audience": "employee",
        "version": 2,
        "status": "superseded",
        "carry_over": 10
    },
    {
        "policy": "vacation",
        "audience": "employee",
        "version": 3,
        "status": "current",
        "carry_over": 5
    }],
    "generated_answer":
        "Employees may carry over a maximum of 5 unused vacation days.",

    "expected_authoritative": True
}]


def validate_authoritative_answer(
    retrieved_chunks,
    generated_answer
):
    for chunk in retrieved_chunks:
        if chunk.get("status") == "current":
         carry_over = chunk.get("carry_over")
         print(f"Current carry_over: {carry_over}")
         expected_policy = f"{carry_over} unused vacation days"
         if expected_policy in generated_answer:
                return True
    return False

@pytest.mark.parametrize("scenario", scenario4)
def test_rag_authoritative(scenario):
    assert scenario["expected_authoritative"] == validate_authoritative_answer(scenario["retrieved_chunks"], scenario["generated_answer"])

scenario5 = [{
    "id": "NEG-RAG-006",
    "question": "Can I work remotely?",
    "retrieved_chunks": [
        {
            "audience": "employee",
            "policy": "remote_work",
            "rule": "Employees may work remotely up to 2 days per week with manager approval."
        },
        {
            "audience": "contractor",
            "policy": "remote_work",
            "rule": "Contractors are not eligible for remote work."
        }
    ],
    "generated_answer":
        "Yes, you can work remotely up to 2 days per week.",
    "expected_ambiguity_handled": False
}]


def validate_ambiguity_answer(
    retrieved_chunks,
    generated_answer
):
    audiences=[]
    for chunk in retrieved_chunks:
        audience = chunk.get("audience")
        if audience not in audiences:
         audiences.append(audience)
         print (audiences)
    is_ambigious = len(audiences)>1
    all_audiences_mentioned =  all(role in generated_answer for role in audiences)
    print(all_audiences_mentioned)
    if is_ambigious:
     return all_audiences_mentioned
    return True

@pytest.mark.parametrize("scenario", scenario5)
def test_rag_ambiguity(scenario):
    assert scenario["expected_ambiguity_handled"] == validate_ambiguity_answer(scenario["retrieved_chunks"], scenario["generated_answer"])

