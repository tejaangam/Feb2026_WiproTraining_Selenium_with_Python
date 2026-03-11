*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}             https://jqueryui.com/datepicker/

*** Test Cases ***
Verify Frames

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        Set Selenium Implicit Wait    3s
        Select Frame    xpath://iframe[@class='demo-frame']
        Click Element    xpath://input[@id='datepicker']
        Sleep    2s
        Click Element    xpath://a[normalize-space()='21']
        Sleep    2s
        #close browser
        Close Browser

