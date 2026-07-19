from fastapi.testclient import TestClient
from app.websocket_app import app
import pytest


class TestWebsocket:
    def test_if_no_errors_during_initialization(self):
        try:
            TestClient(app)
        except Exception as e:
            pytest.fail(f"Initialization resulted in errors: {e}")

    def test_if_incorrect_input_format_returns_error_message(
        self, client: TestClient, bad_input_format_data: dict[str, str]
    ):

        with client.websocket_connect("/ws") as ws:
            ws.send_json(bad_input_format_data)
            response = ws.receive_json()
            assert response == {"message": "Unexpected Data Format"}

    def test_if_correct_data_sent_responds_correctly(
        self, client: TestClient, good_input_format_data: dict[str, str]
    ):

        with client.websocket_connect("/ws") as ws:
            ws.send_json(good_input_format_data)
            response = ws.receive_json()
            assert response == {
                "message": "data was recieved",
                "data": good_input_format_data,
            }
