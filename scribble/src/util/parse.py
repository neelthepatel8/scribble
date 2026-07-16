from models import WebSocketRecievedMessage
from google.protobuf.json_format import ParseDict, ParseError


def websocket_input(input_data: WebSocketRecievedMessage) -> bool:
    try:
        message_model = WebSocketRecievedMessage()

        ParseDict(input_data, message_model, ignore_unknown_fields=False)

    except (ParseError, ValueError):
        return False

    return True
