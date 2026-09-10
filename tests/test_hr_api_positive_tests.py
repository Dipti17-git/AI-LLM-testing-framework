import requests
import pytest

def test_valid_hr_request(base_url,valid_payload):

    payload = valid_payload.copy()

    response = requests.post(
        f"{base_url}/api/chat",
        json=payload
    )

    print("\nSTATUS:", response.status_code)
    print("BODY:", response.text)
    assert response.status_code == 200

    body = response.json()

    assert "answer" in body
    assert body["answer"].strip() != ""
    assert "model" in body

def test_valid_different_prompt(base_url, valid_payload):
    payload = valid_payload.copy()
    payload["prompt"] = "How many vacation days an employee is entitled annually?"

    response = requests.post(
        f"{base_url}/api/chat",
        json=payload
    )

    print("\nSTATUS:", response.status_code)
    print("BODY:", response.text)
    assert response.status_code == 200

    body = response.json()

    assert "answer" in body
    assert body["answer"].strip() != ""
    assert "model" in body

def test_response_contains_model(base_url, valid_payload):
    payload = valid_payload.copy()
    response = requests.post(
        f"{base_url}/api/chat",
        json=payload
    )

    assert response.status_code == 200

    body = response.json()

    assert "model" in body
    assert body["model"].strip() != ""