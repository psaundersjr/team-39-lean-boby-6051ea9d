from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):
    def test_init(self):
        testObj = Position(2, 4)
        assert (testObj.xCoordinate == 2) & (testObj.yCoordinate == 4)
        

