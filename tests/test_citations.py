import pytest

scenario1 = [{
    "id": "CIT-001",
    "question": "How many unused vacation days can I carry over",
    "generated_answer": "Employees may carry over a maximum of 5 unused vacation days.",
    "citation": ["Employees may carry over a maximum of 5 unused vacation days."],

    "critical_claim_elements": ["carry over", "5", "unused vacation days"],
    "expected_result": True,
}]
scenario2 = [{
    "id": "CIT-002",
    "question": "How many unused vacation days can I work remotely",
    "generated_answer": "Employees can work remotely up to 2 days per week with manager approval.",
    "citation": ["Employees can work remotely up to 2 days per week."],

    "critical_claim_elements": ["remotely", "2", "days per week","manager approval"],
    "expected_result": False,
}
]
scenario3 = [{
    "id": "CIT-003",
    "question": "How many unused vacation days can I carry over",
    "generated_answer": "Employees may carry over a maximum of 5 unused vacation days.",
    "citation": ["Employees may carry over a maximum of 10 unused vacation days."],
    "critical_claim_elements": ["carry over", "5", "unused vacation days"],
    "expected_result": False,
}
]
scenario4 = [{
    "id": "CIT-004",
    "question": "How many unused vacation days can I have annually",
    "generated_answer": "Employees receive 25 vacation days annually and may carry over 5 unused vacation days with manager approval.",
    "citation": ["Employees receive 25 vacation days annually.", "Employees may carry over a maximum of 5 unused vacation days."],
    "critical_claim_elements": ["carry over", "5","unused vacation days", "25 vacation days annually", "manager approval"],
    "expected_result": False,
}
]

scenario5 = [{
    "id": "CIT-005",
    "question": "Can I work remotely",
    "generated_answer": "Contractors are not eligible for remote work.",
    "citation": [],
    "critical_claim_elements": ["contractors", "remote work"],
    "expected_result": False,
}
]


def validate_multiple_citation_support(
        generated_answer, citations, critical_claim_elements
):
    return all(
        any(claim_element in generated_answer and claim_element in citation for citation in citations) for claim_element in critical_claim_elements)

@pytest.mark.parametrize("scenario1", scenario1, ids=["CIT-001"])
def test_rag_citation(scenario1):
    assert scenario1["expected_result"] == validate_multiple_citation_support(scenario1["generated_answer"], scenario1["citation"],
                                                                    scenario1["critical_claim_elements"])

@pytest.mark.parametrize("scenario2", scenario2, ids=["CIT-002"])
def test_rag_citation_partial(scenario2):
    assert scenario2["expected_result"] == validate_multiple_citation_support(scenario2["generated_answer"], scenario2["citation"],
                                                                    scenario2["critical_claim_elements"])

@pytest.mark.parametrize("scenario3", scenario3, ids=["CIT-003"])
def test_rag_citation_conflict(scenario3):
    assert scenario3["expected_result"] == validate_multiple_citation_support(scenario3["generated_answer"], scenario3["citation"],
                                                                    scenario3["critical_claim_elements"])

@pytest.mark.parametrize("scenario4", scenario4, ids=["CIT-004"])
def test_rag_citation_unsupported(scenario4):
    assert scenario4["expected_result"] == validate_multiple_citation_support(scenario4["generated_answer"], scenario4["citation"],
                                                                    scenario4["critical_claim_elements"])
@pytest.mark.parametrize("scenario5", scenario5, ids=["CIT-005"])
def test_rag_citation_missing(scenario5):
    assert scenario5["expected_result"] == validate_multiple_citation_support(scenario5["generated_answer"], scenario5["citation"],
                                                                    scenario5["critical_claim_elements"])
