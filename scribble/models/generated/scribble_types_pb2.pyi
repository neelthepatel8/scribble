from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class RoundStatus(_message.Message):
    __slots__ = ("guessWord", "time", "wordProgress", "drawingPlayer", "correctGuessingPlayers")
    GUESSWORD_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    WORDPROGRESS_FIELD_NUMBER: _ClassVar[int]
    DRAWINGPLAYER_FIELD_NUMBER: _ClassVar[int]
    CORRECTGUESSINGPLAYERS_FIELD_NUMBER: _ClassVar[int]
    guessWord: str
    time: int
    wordProgress: str
    drawingPlayer: Player
    correctGuessingPlayers: _containers.RepeatedCompositeFieldContainer[Player]
    def __init__(self, guessWord: _Optional[str] = ..., time: _Optional[int] = ..., wordProgress: _Optional[str] = ..., drawingPlayer: _Optional[_Union[Player, _Mapping]] = ..., correctGuessingPlayers: _Optional[_Iterable[_Union[Player, _Mapping]]] = ...) -> None: ...
