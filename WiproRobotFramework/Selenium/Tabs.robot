*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}                  https://the-internet.herokuapp.com/windows
*** Test Cases ***
Verify Links texts

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        Click Element    link=Click Here
        @{windows}=     Get Window Handles
        Log To Console    ${windows}
        @{titles}=      Get Window Titles
        Log To Console    ${titles}
        Switch Window   title= New Window
        Element Text Should Be    xpath://h3[normalize-space()='New Window']    New Window
        Switch Window       MAIN
        #close browser
        Close Browser

