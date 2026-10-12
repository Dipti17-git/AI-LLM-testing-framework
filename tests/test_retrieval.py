import pytest

def test_correct_retrieval():
    retrieved_chunks =  ["Employees receive 25 vacation days annually.",
    "Employees may carry over a maximum of 5 unused vacation days."
    ]

    assert any(
        "5 unused vacation days" in chunk
        for chunk in retrieved_chunks
    )

def test_missing_retrieval():
    retrieved_chunks =  [ "Employees receive 25 vacation days annually.",
    "Employees can work remotely up to 2 days per week."
    ]

    assert any(
        "5 unused vacation days" in chunk
        for chunk in retrieved_chunks
    )

def test_irrelevant_retrieval():
    retrieved_chunks =  [ "Employees may carry over a maximum of 5 unused vacation days.",
    "Employees can work remotely up to 2 days per week.",
    "Expense claims must be submitted within 30 days."
    ]

    assert not any(
        "work remotely" in chunk or "Expense claims" in chunk
        for chunk in retrieved_chunks
    )

retrieval_scenarios = [
    {
        "id": "RET-001",
        "expected_text": "5 unused vacation days",
        "retrieved_chunks": [
            "Employees receive 25 vacation days annually.",
            "Employees may carry over a maximum of 5 unused vacation days."
        ],
        "expected_result": True
    },
    {
        "id": "RET-002",
        "expected_text": "5 unused vacation days",
        "retrieved_chunks": [
            "Employees receive 25 vacation days annually.",
            "Employees can work remotely up to 2 days per week."
        ],
        "expected_result": False
    }
]
def contains_expected_information(retrieved_chunks, expected_text):
    return any(expected_text in chunk for chunk in retrieved_chunks)

@pytest.mark.parametrize("scenario", retrieval_scenarios)
def test_retrieval(scenario):
    assert scenario["expected_result"] == contains_expected_information(scenario["retrieved_chunks"], scenario["expected_text"])

scenario = [{
        "id": "RET-003",
        "retrieved_chunks": [
            "Employees may carry over a maximum of 5 unused vacation days.",
            "Employees can work remotely up to 2 days per week.",
            "Expense claims must be submitted within 30 days."
        ],
        "irrelevant_text": [
            "work remotely",
            "Expense claims"
        ],
        "expected_irrelevant": True
    }]

def contains_irrelevant_information(retrieved_chunks, irrelevant_text):
    return any(
        any(phrase in chunk for phrase in irrelevant_text)
        for chunk in retrieved_chunks
    )


@pytest.mark.parametrize("scenario", scenario)
def test_retrieval1(scenario):
   # assert scenario["expected_result"] == contains_expected_information(scenario["retrieved_chunks"], scenario["expected_text"])
    assert scenario["expected_irrelevant"] == contains_irrelevant_information(scenario["retrieved_chunks"], scenario["irrelevant_text"])


missing_scenario = [{
        "id": "RET-004",
        "retrieved_chunks": [
            "Employees may work remotely up to 2 days per week.",
            "Employees receive 25 vacation days annually."
        ],
        "required_information": [
            "2 days per week",
            "manager approval"
        ],
        "expected_required": False
    }]

def contains_all_required_information(retrieved_chunks, required_information):
    return all(
        any(phrase in chunk for chunk in retrieved_chunks)
        for phrase in required_information
    )
@pytest.mark.parametrize("scenario", missing_scenario)
def test_retrieval_required(scenario):
    assert scenario["expected_required"] == contains_all_required_information(scenario["retrieved_chunks"], scenario["required_information"])