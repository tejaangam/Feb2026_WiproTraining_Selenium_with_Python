*** Settings ***
Library     SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}              https://the-internet.herokuapp.com/download
*** Test Cases ***
Verify File Downloads

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        Wait Until Element Is Visible       xpath://a[normalize-space()='bb.txt']

        Click Element    xpath://a[normalize-space()='bb.txt']
        ${files}=       List Files In Directory         C:\Users\hp\Local\Downloads
        List Should Contain Value      ${files}        upload.txt
        Sleep    5s

        #close browser
        Close Browser

