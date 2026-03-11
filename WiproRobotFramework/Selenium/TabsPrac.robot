*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}                  https://rahulshettyacademy.com/AutomationPractice/
*** Test Cases ***
Verify Links texts

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        Click Element    xpath://button[@id='openwindow']
        @{windows}=     Get Window Handles
        Log To Console    ${windows}
        @{titles}=      Get Window Titles
        Log To Console    ${titles}
        Switch Window   title= QAClick Academy - A Testing Academy to Learn, Earn and Shine
        Switch Window       MAIN
        #close browser
        Close Browser

