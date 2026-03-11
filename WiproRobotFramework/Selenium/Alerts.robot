*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}              https://the-internet.herokuapp.com/javascript_alerts
*** Test Cases ***
Verify Alerts

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        Wait Until Element Is Visible       xpath:(//button)[1]

        #Simple alert - accecpt is for ok
        Click Element    xpath:(//button)[1]
        Handle Alert    action=ACCEPT       timeout=3
        Sleep    5s

        #confirmational alert - accept is for ok, dismiss is for cancel
        Click Element    xpath:(//button)[2]
        Handle Alert    action=DISMISS      timeout=3
        Sleep    5s

        #Prompt alert - accept is for ok, dismiss is for cancel
        Click Element    xpath:(//button)[3]
        Input Text Into Alert   Teja
        Sleep    5s

        #close browser
        Close Browser

