from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_get_name(self):
        ARBITRARY_NAME = "testName"
        testobj = Character(ARBITRARY_NAME)
        assert testobj.getName() == ARBITRARY_NAME
