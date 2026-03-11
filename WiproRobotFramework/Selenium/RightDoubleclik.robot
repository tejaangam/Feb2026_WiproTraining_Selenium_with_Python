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
        Wait Until Element Is Visible       xpath://a[normalize-space()='Fresh']
        Sleep    2s
        #Right Click
        Open Context Menu   xpath://a[normalize-space()='Fresh']
        Sleep    3s
        #Double click
        Double Click Element    xpath://a[normalize-space()='Sell']
        #close browser
        Close Browser

