from fastapi import FastAPI, WebSocket
import util.parse as parse

app = FastAPI()

if __name__ == "__main__":
    app = FastAPI()


@app.get("/")
async def get():
    return {"message": "hello, world!"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        print(type(data))
        # parse and validate data
        if not parse.websocket_input(data):
            await websocket.send_json({"message": "Unexpected Data Format"})
        await websocket.send_json({"message": "data was recieved", "data": data})
