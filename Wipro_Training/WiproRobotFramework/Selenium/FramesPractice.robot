
#*** Settings ***
#Library     SeleniumLibrary

#*** Variables ***
${url}             https://www.tutorialspoint.com/selenium/practice/frames.php

#*** Test Cases ***
Verify Frames

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        Set Selenium Implicit Wait    3s
        Select Frame    xpath://body//main//iframe[1]
        Get WebElements    xpath://h1[normalize-space()='Selenium - Automation Practice Form']
        Sleep    2s
        Unselect Frame
        Select Frame    xpath://body//main//iframe[2]
        Get WebElements    xpath://a[normalize-space()='']//*[name()='svg']//*[name()='path']
        Sleep    2s
        Unselect Frame
        #close browser
        Close Browser


*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/frames.php
*** Test Cases ***
Verify iframe
    Open Browser    ${url}      firefox
    Maximize Browser Window
    Set Selenium Implicit Wait    3s
    Select Frame    xpath://body//main//iframe[1]
    Sleep    2s
    ${text1}=       Get Text    xpath://body
    Sleep    2s
    Log To Console    Frame 1 Text:
    Log To Console    ${text1}
    Unselect Frame
    Select Frame    xpath://body//main//iframe[2]
    Sleep    2s
    ${text2}=       Get Text    xpath://body
    Sleep    2s
    Log To Console    Frame 2 Text:
    Log To Console    ${text2}
    Unselect Frame
    Close Browser


