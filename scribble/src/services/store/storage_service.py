import redis
import uuid


class StorageService:
    def __init__(self) -> None:
        self.client = redis.Redis(host="localhost", port=6379, decode_responses=True)

    def new_session(self) -> uuid.UUID:
        session_id = uuid.uuid4()

        # creating an empty session for now, i think we can do launch or smth
        # where we populate with base values
        self.client.hset(f"game_state_session:{session_id}", mapping={})
        return session_id
