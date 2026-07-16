from base import Operation
from services.guess_generator import WordGeneratorService
from models.generated.scribble_types_pb2 import (
    WebSocketRecievedMessage,
    WebSocketSendMessage,
    WebSocketSendMessageData,
)


class NextWordOperation(Operation):
    def __init__(self):
        super().__init__()

    def run(
        self, input_message: WebSocketRecievedMessage, client: WordGeneratorService
    ) -> None:

        client.generate()
        # will update state here
