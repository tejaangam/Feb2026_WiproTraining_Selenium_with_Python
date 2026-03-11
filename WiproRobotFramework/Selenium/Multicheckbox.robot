*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}              https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify login scenario with valid credentials

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
                #identify the common elements attribut
        @{elements}=     Get WebElements     xpath://input[@type='checkbox']
        FOR    ${element}    IN    @{elements}
           Click Element   ${element}
           Sleep    2s
        END
        #close browser
        Close Browser

