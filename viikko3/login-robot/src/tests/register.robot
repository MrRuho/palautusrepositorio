*** Settings ***
Resource  resource.robot
# Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password 
    Create User  kalle  kalle123
    Output Should Contain  Kelvollinen käyttäjänimi ja salasana

Register With Already Taken Username And Valid Password  

Register With Too Short Username And Valid Password
    Create User  ka  kalle123
    Output Should Contain  Virheellinen käyttäjänimi

Register With Enough Long But Invalid Username And Valid Password
    Create User  ka_¤%66  kalle123
    Output Should Contain  Virheellinen käyttäjänimi

Register With Valid Username And Too Short Password
    Create User  kalle  kalle
    Output Should Contain  Virheellinen salasana

Register With Valid Username And Long Enough Password Containing Only Letters
    Create User  kalle  kallekallekalle
    Output Should Contain  Virheellinen salasana

*** Keywords ***
