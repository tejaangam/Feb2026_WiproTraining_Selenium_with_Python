*** Settings ***
Library     SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}                  https://www.tutorialspoint.com/selenium/practice/upload-download.php
*** Test Cases ***
Verify File Downloads

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        Wait Until Element Is Visible       xpath://input[@id='uploadFile']
        # choose the file
        Choose File             xpath://input[@id='uploadFile']         "C:\Users\hp\Downloads\sampleFile.jpeg"
        Sleep    2s
        #Element text should be visible
        Sleep    3s

        #close browser
        Close Browser

