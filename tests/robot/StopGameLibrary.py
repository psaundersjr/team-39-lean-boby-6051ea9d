from levelup.controller import GameController
from robot.libraries.BuiltIn import BuiltIn

class StopGameLibrary:
    ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

    def number_of_map_positions_should_be(self, expected):
        actual = self.controller.get_total_positions()
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    def X_coordinate_should_be(self, expected):
        actual = self.controller.status.current_position[0]
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    def Y_coordinate_should_be(self, expected):
        actual = self.controller.status.current_position[0]
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    def move_count_should_be(self, expected):
        actual = self.controller.status.move_count
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"