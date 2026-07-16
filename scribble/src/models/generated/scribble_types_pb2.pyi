from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SYSTEM_NEUTRAL: _ClassVar[ChatType]
    SYSTEM_POSITIVE: _ClassVar[ChatType]
    SYSTEM_NEGATIVE: _ClassVar[ChatType]
    PLAYER: _ClassVar[ChatType]

class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GUESS_INPUT_FROM_USER: _ClassVar[Operation]
    DRAW_INPUT_FROM_USER: _ClassVar[Operation]
SYSTEM_NEUTRAL: ChatType
SYSTEM_POSITIVE: ChatType
SYSTEM_NEGATIVE: ChatType
PLAYER: ChatType
GUESS_INPUT_FROM_USER: Operation
DRAW_INPUT_FROM_USER: Operation

class Player(_message.Message):
    __slots__ = ("uuid", "username", "currentGamePoints", "iconUrl")
    UUID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    CURRENTGAMEPOINTS_FIELD_NUMBER: _ClassVar[int]
    ICONURL_FIELD_NUMBER: _ClassVar[int]
    uuid: int
    username: str
    currentGamePoints: int
    iconUrl: str
    def __init__(self, uuid: _Optional[int] = ..., username: _Optional[str] = ..., currentGamePoints: _Optional[int] = ..., iconUrl: _Optional[str] = ...) -> None: ...

class GameStatus(_message.Message):
    __slots__ = ("maxRounds", "maxTime", "players", "roundStatus")
    MAXROUNDS_FIELD_NUMBER: _ClassVar[int]
    MAXTIME_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    ROUNDSTATUS_FIELD_NUMBER: _ClassVar[int]
    maxRounds: int
    maxTime: int
    players: _containers.RepeatedCompositeFieldContainer[Player]
    roundStatus: RoundStatus
    def __init__(self, maxRounds: _Optional[int] = ..., maxTime: _Optional[int] = ..., players: _Optional[_Iterable[_Union[Player, _Mapping]]] = ..., roundStatus: _Optional[_Union[RoundStatus, _Mapping]] = ...) -> None: ...

class RoundStatus(_message.Message):
    __slots__ = ("currentRound", "guessWord", "time", "wordProgress", "drawingPlayer", "correctGuessingPlayers", "chatHistory")
    CURRENTROUND_FIELD_NUMBER: _ClassVar[int]
    GUESSWORD_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    WORDPROGRESS_FIELD_NUMBER: _ClassVar[int]
    DRAWINGPLAYER_FIELD_NUMBER: _ClassVar[int]
    CORRECTGUESSINGPLAYERS_FIELD_NUMBER: _ClassVar[int]
    CHATHISTORY_FIELD_NUMBER: _ClassVar[int]
    currentRound: int
    guessWord: str
    time: int
    wordProgress: str
    drawingPlayer: Player
    correctGuessingPlayers: _containers.RepeatedCompositeFieldContainer[Player]
    chatHistory: ChatHistory
    def __init__(self, currentRound: _Optional[int] = ..., guessWord: _Optional[str] = ..., time: _Optional[int] = ..., wordProgress: _Optional[str] = ..., drawingPlayer: _Optional[_Union[Player, _Mapping]] = ..., correctGuessingPlayers: _Optional[_Iterable[_Union[Player, _Mapping]]] = ..., chatHistory: _Optional[_Union[ChatHistory, _Mapping]] = ...) -> None: ...

class Chat(_message.Message):
    __slots__ = ("playerUuid", "rawMessageStr", "type")
    PLAYERUUID_FIELD_NUMBER: _ClassVar[int]
    RAWMESSAGESTR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    playerUuid: str
    rawMessageStr: str
    type: ChatType
    def __init__(self, playerUuid: _Optional[str] = ..., rawMessageStr: _Optional[str] = ..., type: _Optional[_Union[ChatType, str]] = ...) -> None: ...

class ChatHistory(_message.Message):
    __slots__ = ("chats",)
    CHATS_FIELD_NUMBER: _ClassVar[int]
    chats: _containers.RepeatedCompositeFieldContainer[Chat]
    def __init__(self, chats: _Optional[_Iterable[_Union[Chat, _Mapping]]] = ...) -> None: ...

class WebSocketRecievedMessageData(_message.Message):
    __slots__ = ("player",)
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    player: Player
    def __init__(self, player: _Optional[_Union[Player, _Mapping]] = ...) -> None: ...

class WebSocketRecievedMessage(_message.Message):
    __slots__ = ("operation", "data")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    operation: Operation
    data: WebSocketRecievedMessageData
    def __init__(self, operation: _Optional[_Union[Operation, str]] = ..., data: _Optional[_Union[WebSocketRecievedMessageData, _Mapping]] = ...) -> None: ...
