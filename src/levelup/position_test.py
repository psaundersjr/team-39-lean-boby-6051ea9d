from unittest import TestCase
from levelup.position import Position

class postiontest(TestCase):
    def test_init(self):
        ARBITRARY_POSITION = "MyPosition"
        testobj = Position(ARBITRARY_POSITION)
        self.assertEqual(ARBITRARY_POSITION, testobj.position)