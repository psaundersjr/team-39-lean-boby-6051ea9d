*** Settings ***
Documentation     Test stop of game. Stop playing \n\n https://raw.githubusercontent.com/level-up-program/python-robot-reference/main/tests/robot/images/gamerErin.png
Test Template     Stop game
Library           StopGameLibrary.py

*** Test Cases ***      numMoveCount    numPositions    endingPositionX endingPositionY     
Blank character name    0                100            0               0

*** Keywords ***
Stop game               
    [Arguments]    ${numMoveCount}  ${numPositions} ${endingPositionX}  ${endingPositionY}
    Number of map positions should be  ${numPositions}
    X coordinate should be    ${endingPositionX}
    Y coordinate should be    ${endingPositionY}
    Move count should be      ${numMoveCount}
