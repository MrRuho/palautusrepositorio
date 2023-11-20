*** Settings ***
Resource  resource.robot
# Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Create User  ka  kalle123
    Valid Username  ka  kalle
    Output Should Contain  Liian lyhyt nimi tai salasana

*** Keywords ***