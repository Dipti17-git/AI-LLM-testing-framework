import pytest
from llm.client import LLMClient

@pytest.fixture
def base_url():
    return "http://127.0.0.1:8000"

@pytest.fixture
def valid_payload():
    return {
        "context": "Employees receive 25 vacation days annually.",
        "prompt": "How many vacation days do employees receive?"
    }

@pytest.fixture
def llm_client():
    return LLMClient()


@pytest.fixture
def vacation_scenario():
    return {
        "context": "Employees receive 25 vacation days annually.",
        "prompt": "How many vacation days can I take in a year?"
    }