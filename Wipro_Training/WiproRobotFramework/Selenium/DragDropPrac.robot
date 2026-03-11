*** Settings ***
Library     SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}                  https://www.tutorialspoint.com/selenium/practice/droppable.php
*** Test Cases ***
Verify Drag and Drop

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        Wait Until Element Is Visible       xpath://p[normalize-space()='Drag me to my target']
        Sleep    2s
        Drag And Drop    xpath://p[normalize-space()='Drag me to my target']    xpath://div[@id='droppable']

        Sleep    3s

        #close browser
        Close Browser

