*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}              https://www.tutorialspoint.com/seleniumpractice/selenium_automation_practice.php

*** Test Cases ***
Verify Drop down

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        Wait Until Element Is Visible    xpath://select[@id='state']
        ${labels}=      Get Selected List Label    xpath://select[@id='state']
        Log         ${labels}
        #select by label
        Select From List By Label   id=state    Uttar Pradesh
        Sleep    2s


        #Select by value
        Select From List By Value     id=city       Lucknow
        Sleep    2s


        #close browser
        Close Browser

