from models import WebSocketRecievedMessage
from google.protobuf.json_format import ParseDict, ParseError
from collections.abc import Mapping
from typing import Any


def websocket_input(input_data: Mapping[str, Any]) -> bool:
    try:
        message_model = WebSocketRecievedMessage()

        ParseDict(input_data, message_model, ignore_unknown_fields=False)

    except (ParseError, ValueError):
        return False

    return True
