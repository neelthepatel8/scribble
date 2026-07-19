from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import util.parse as parse

app = FastAPI()

if __name__ == "__main__":
    app = FastAPI()  # pragma: no cover


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_json()

            # parse and validate data
            if not parse.websocket_input(data):
                await websocket.send_json({"message": "Unexpected Data Format"})

            else:
                await websocket.send_json(
                    {"message": "data was recieved", "data": data}
                )
    except WebSocketDisconnect:
        # this exception is called by fastapi when websocket closes, it is safe to pass since it happens anyways
        pass
