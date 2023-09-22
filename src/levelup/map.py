from levelup.position import Position
from levelup.controller import Direction
class Map:
    numPositions = 100

    def getPositions (self):
        pass
    #TODO

    def calculateposition(self, startingPosition: Position, direction: Direction):
       pass
    #TODO
        
    def isPositionValid(self, positionCoordinateX,positionCoordinateY):
        if (positionCoordinateX > 9) or (positionCoordinateY > 9):
            return False
        return True
    

    def getTotalPositions (self):
        return self.numPositions
    



