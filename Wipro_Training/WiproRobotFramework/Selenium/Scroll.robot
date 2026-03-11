*** Settings ***
Library     SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}                  https://www.amazon.in/
*** Test Cases ***
Verify Drag and Drop

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        #Wait Until Element Is Visible       xpath://a[normalize-space()='Fresh']
        Sleep    2s
        Scroll Element Into View    link= Sell on Amazon
        Sleep    2s
        Click Element    link= Sell on Amazon
        Sleep    2s
        Title Should Be    Amazon.in: Selling on Amazon - Start Selling Now
        #close browser
        Close Browser

