*** Settings ***
Documentation   Test start of game. \n Mockups images: \n\n https://github.com/level-up-program/team-39-lean-boby-6051ea9d/blob/main/Team39%20mockup%20image.jpg Test start of game. Let's play \n\n https://raw.githubusercontent.com/level-up-program/python-robot-reference/main/tests/robot/images/gamerErin.png 
Test Template     Start new game
Library           StartGameLibrary.py

*** Test Cases ***      numPositions     startingPositionX    startingPositionY  startingMoveCount
Blank character name    100              0                    0                  0

*** Keywords ***
Start new game
    [Arguments]    ${numPositions}  ${startingPositionX}  ${startingPositionY}  ${startingMoveCount}
    Initialize controller
    Number of map positions should be  ${numPositions}
    Starting X coordinate should be    ${startingPositionX}
    Starting Y coordinate should be    ${startingPositionY}
    Starting move count should be      ${startingMoveCount}
