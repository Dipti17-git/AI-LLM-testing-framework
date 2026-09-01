import json
import pytest


def load_dataset(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


required_fields = [
    "id",
    "category",
    "context",
    "prompt",
    "critical_facts",
    "prohibited_claims",
    "expected_behavior"
]


test_cases = load_dataset("datasets/golden_dataset.json")


@pytest.mark.parametrize("test_case", test_cases)
def test_golden_dataset_structure(test_case):

    test_id = test_case.get("id", "UNKNOWN")

    for field in required_fields:

        assert field in test_case, (
            f"{test_id}: Missing required field: {field}"
        )

        if isinstance(test_case[field], str):
            assert len(test_case[field].strip()) >= 3, (
                f"{test_id}: Field '{field}' is empty or invalid"
            )