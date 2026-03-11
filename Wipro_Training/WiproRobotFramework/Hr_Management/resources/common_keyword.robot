*** Settings ***
Library    SeleniumLibrary
Resource   variables.robot

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    5

Close Browser Session
    Close Browser