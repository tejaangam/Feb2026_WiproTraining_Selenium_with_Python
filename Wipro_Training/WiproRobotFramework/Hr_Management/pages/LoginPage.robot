*** Settings ***
Library     SeleniumLibrary

*** Variables ***

${USERNAME_FIELD}       xpath://input[@placeholder='Username']
${PASSWORD_FIELD}       xpath://input[@placeholder='Password']
${LOGIN_BUTTON}         xpath://button[normalize-space()='Login']
${ERROR_MESSAGE}        xpath://p[@class='oxd-text oxd-text--p oxd-alert-content-text']

*** Keywords ***

Enter Username
        [Arguments]     ${username}
        Input Text    ${USERNAME_FIELD}    ${username}
Enter Password
        [Arguments]     ${password}
        Input Text    ${PASSWORD_FIELD}    ${password}
Click login Button
        Click Button    ${LOGIN_BUTTON}
Verify Successful Login
    Wait Until Page Contains    Dashboard

Verify Error Message
    Element Should Be Visible    ${ERROR_MESSAGE}
    Element Text Should Be    ${ERROR_MESSAGE}    Invalid credentials