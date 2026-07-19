from pytest import fixture
from fastapi.testclient import TestClient
from app.websocket_app import app
from typing import Any, Mapping
from models import (
    Operation,
)


@fixture
def client():
    return TestClient(app)


@fixture
def bad_input_format_data() -> Mapping[str, Any]:
    return {"not-operation": "hello", "not-data": "data"}


@fixture
def good_input_format_data() -> Mapping[str, Any]:
    return {
        "message_id": "message-id-123",
        "operation": Operation.GUESS_INPUT_FROM_USER,
        "data": {},
    }
