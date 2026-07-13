def websocket_input(data: dict) -> bool:
    return "operation" not in data or "data" not in data
