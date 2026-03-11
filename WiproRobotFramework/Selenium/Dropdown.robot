*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}              https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify dropdowns


        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        Wait Until Element Is Visible    id=dropdown-class-example
        ${labels}=      Get Selected List Label    id=dropdown-class-example
        Log         ${labels}
        #select by label
        Select From List By Label    id=dropdown-class-example      Option3
        Sleep    2s

        #select by index
        Select From List By Index    id=dropdown-class-example          2
        Sleep    2s
        #Select by value
        Select From List By Value     id=dropdown-class-example        option1
        Sleep    2s


        #close browser
        Close Browser

