from unittest import TestCase
from levelup.controller import GameStatus

class TestGameStatus(TestCase):
    def test_init(self):
        testObj = GameStatus()
        assert testObj.move_count ==0
        