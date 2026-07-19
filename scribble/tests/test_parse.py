from typing import Any
from collections.abc import Mapping
from util import parse


class TestUtils:

    def test_parse_good_input_returns_true(
        self, good_input_format_data: Mapping[str, Any]
    ):
        assert parse.websocket_input(good_input_format_data)
