import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"

@pytest.mark.parametrize(
    "payload, expected_status",
    [
        (
            {"context": "Employees receive 25 vacation days annually."},
            422
        ),
        (
            {
                "context": "Employees receive 25 vacation days annually.",
                "prompt": ""
            },
            400
        ),
        (
            {
                "context": "Employees receive 25 vacation days annually.",
                "prompt": "   "
            },
            400
        ),
        (
            {"prompt": "How many vacation days do employees receive?"},
            422
        ),
        (
            {
                "context": "",
                "prompt": "How many vacation days do employees receive?"
            },
            400
        ),
    ],
    ids=[
        "missing-prompt",
        "empty-prompt",
        "whitespace-prompt",
        "missing-context",
        "empty-context"
    ]
)
def test_invalid_requests(payload, expected_status):

    response = requests.post(
        f"{BASE_URL}/api/chat",
        json=payload
    )

    assert response.status_code == expected_status