*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}              https://www.tutorialspoint.com/selenium/practice/check-box.php

*** Test Cases ***
Verify login scenario with valid credentials

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window

        @{elements}=     Get WebElements    xpath://input[starts-with(@id,'c_bs_')]

        FOR    ${element}    IN    @{elements}
           Click Element   ${element}
           Sleep    2s
        END
        #close browser
        Close Browser

