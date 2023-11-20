*** Settings ***
Resource  resource.robot


*** Keywords ***
Increase Counter Three Times
    Increase Counter
    Increase Counter
    Increase Counter

*** Test Cases ***
Increase Counter Once
    Counter Value Should Be  0
    Increase Counter
    Counter Value Should Be  1

Increase Counter Many Times
    Counter Value Should Be  0
    Increase Counter Three Times
    Counter Value Should Be  3

Increment Counter By Amount
    Counter Value Should Be  0
    Increment Counter By  5
    Counter Value Should Be  5

Reset Counter After One Increment
    Counter Value Should Be  0
    Increase Counter
    Counter Value Should Be  1
    Reset Counter
    Counter Value Should Be  0

Reset Counter After Several Increments
    Counter Value Should Be  0
    Increment Counter By  5
    Counter Value Should Be  5
    Reset Counter
    Counter Value Should Be  0
