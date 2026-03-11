*** Settings ***
Library     SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}                  https://the-internet.herokuapp.com/upload
*** Test Cases ***
Verify Upload
        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        Set Selenium Implicit Wait    2s
        Wait Until Element Is Visible       xpath://input[@id='file-upload']
        # choose the file
        Choose File     xpath://input[@id='file-upload']            C:\Users\hp\Downloads\sample.jpg
        Click Element    xpath://input[@id='file-submit']
        Sleep    2s
        #Element text should be visible
        Element Text Should Be    xpath://h3[normalize-space()='File Uploaded!']    File Uploaded!
        Sleep    3s

        #close browser
        Close Browser

