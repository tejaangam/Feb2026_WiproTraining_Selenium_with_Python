*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}      https://automationexercise.com
${BROWSER}  chrome

*** Keywords ***
Open Browser To Website
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

Close Browser
    Close Browser

Go To Login Page
    Click Element    xpath=//a[contains(text(),'Signup / Login')]

Handle Ads If Present
    ${status}=    Run Keyword And Return Status    Wait Until Element Is Visible    xpath=//iframe[contains(@id,'google')]    3s
    IF    ${status}
        Select Frame    xpath=//iframe[contains(@id,'google')]
        ${close_status}=    Run Keyword And Return Status    Click Element    xpath=//div[@aria-label='Close']
        Unselect Frame
    END





