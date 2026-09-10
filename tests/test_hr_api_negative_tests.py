import requests
import pytest

def test_empty_prompt(base_url,valid_payload):

    payload = valid_payload.copy()
    payload["prompt"] = ""

    response = requests.post(
        f"{base_url}/api/chat",
        json=payload
    )

    assert response.status_code == 400
    body = response.json()
    assert "detail" in body

def test_whitespace_prompt(base_url,valid_payload):

    payload = valid_payload.copy()
    payload["prompt"] = "  "

    response = requests.post(
        f"{base_url}/api/chat",
        json=payload
    )

    assert response.status_code == 400
    body = response.json()
    assert "detail" in body

def test_missing_prompt(base_url,valid_payload):
        payload = valid_payload.copy()
        del payload["prompt"]

        response = requests.post(
            f"{base_url}/api/chat",
            json=payload
        )

        body = response.json()

        assert response.status_code == 422
        assert "detail" in body
        assert body["detail"][0]["type"]=="missing"
        assert "prompt" in body["detail"][0]["loc"]

def test_missing_context(base_url,valid_payload):
            payload = valid_payload.copy()
            del payload["context"]

            response = requests.post(
                f"{base_url}/api/chat",
                json=payload
            )

            body = response.json()

            assert response.status_code == 422
            assert "detail" in body
            assert body["detail"][0]["type"]=="missing"
            assert "context" in body["detail"][0]["loc"]


@pytest.mark.parametrize("context", [
    "", " ", "     "

])
def test_invalid_context(base_url, context,valid_payload):

    payload = valid_payload.copy()
    payload["context"] = context

    response = requests.post(
        f"{base_url}/api/chat",
        json=payload
    )
    body = response.json()

    assert response.status_code == 400
    assert "detail" in body
    assert body["detail"] == "Context must not be empty"

