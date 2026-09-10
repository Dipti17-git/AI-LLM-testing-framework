import requests
import pytest

def test_response_is_json(base_url, valid_payload):

    payload = valid_payload.copy()

    response = requests.post(
        f"{base_url}/api/chat",
        json=payload
    )

    print("\nSTATUS:", response.status_code)
    print("BODY:", response.text)
    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict), "Response body is not a JSON object"
    assert  "application/json" in response.headers.get("Content-Type"), "Response content type is not application/json"

def test_answer_is_string(base_url, valid_payload):

    payload = valid_payload.copy()

    response = requests.post(
        f"{base_url}/api/chat",
        json=payload
    )

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body.get("answer"), str), "Answer is not a string"

def test_model_is_string(base_url, valid_payload):

    payload = valid_payload.copy()

    response = requests.post(
        f"{base_url}/api/chat",
        json=payload
    )

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body.get("model"), str), "Model is not a string"
