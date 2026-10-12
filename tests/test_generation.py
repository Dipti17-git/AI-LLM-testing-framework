import pytest


scenario = [{
        "id": "RET-003",
        "retrieved_chunks": [
             "Employees may carry over a maximum of 5 unused vacation days.",
    "Carry-over requires manager approval."
        ],

         "generated_answer": [
    "Employees may carry over a maximum of 10 unused vacation days with manager approval."
],
        "required_information": [
            "5 unused vacation days",
            "manager approval"
        ],
        "expected_required": False
    }]


def contains_all_required_information_in_answer(
    generated_answer,
    required_information
):
    return all(
        phrase in generated_answer
        for phrase in required_information
    )

@pytest.mark.parametrize("scenario", scenario)
def test_generation_required_information(scenario):
    assert scenario["expected_required"] == contains_all_required_information_in_answer(
        scenario["generated_answer"],
        scenario["required_information"]
    )