from unittest import TestCase
from levelup.map import Map
#from levelup.position import Position

class TestMap(TestCase):
    def test_init(self):
        testObj = Map()
        assert testObj.numPositions == 100

    def test_get_total_positions(self):   
        testObj = Map()
        assert testObj.getTotalPositions() == 100