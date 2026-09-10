import requests
import pytest
import time

MAX_RESPONSE_TIME = 2.0  # Set the expected response time in seconds
REQUEST_TIMEOUT = 5.0  # Set the request timeout in seconds

def test_api_response_time(base_url, valid_payload):

    payload = valid_payload.copy()
    start_time = time.time()

    response = requests.post(
        f"{base_url}/api/chat",
        json=payload
    )

    end_time = time.time()
    response_time = end_time - start_time

    print(f"\nResponse time: {response_time:.2f} seconds")
    assert response.status_code == 200
    assert response_time < MAX_RESPONSE_TIME, f"Response time exceeded {MAX_RESPONSE_TIME} seconds"

def test_api_request_with_timeout(base_url, valid_payload):

    payload = valid_payload.copy()

    try:
        response = requests.post(
            f"{base_url}/api/chat",
            json=payload,
            timeout=REQUEST_TIMEOUT
        )
        assert response.status_code == 200
        body = response.json()
        assert "answer" in body
    except requests.exceptions.Timeout:
        pytest.fail(f"Request timed out after {REQUEST_TIMEOUT} seconds")

