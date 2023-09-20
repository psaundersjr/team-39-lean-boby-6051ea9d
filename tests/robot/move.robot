*** Settings ***
Documentation   I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Documentation   Exmple test case using the data-driven (table) syntax.
                http://arcbotics.com/wp-content/uploads/2015/12/sparki-driver-icon.png
Test Template   Move character
Library     MoveLibrary.py

*** Test Cases ***      StartingX   StartingY   Direction EndingX   EndingY
Move in middle of board     0       0           NORTH       0       1
Move on edge of board       0       0           SOUTH       0       0

*** Key Words ***
Move character
    [Arguments] ${startingX}    ${startingY}    ${direction}    ${endingX}  ${endingY}
    Initialize character xposition with     ${startingX}
    Initialize character yposition with     ${startingY}
    Move in direction       ${direction}
    Character xposition should be   ${endingX}
    Character yposition should be   ${endingY}