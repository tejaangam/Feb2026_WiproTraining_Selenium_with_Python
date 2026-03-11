*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}              https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify radio buttons and check box

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        #click radio button
        Click Element    xpath://input[@value='radio1']
        #click the checkbox3
        Click Element    xpath://input[@id='checkBoxOpion3']
        #close browser
        Close Browser

