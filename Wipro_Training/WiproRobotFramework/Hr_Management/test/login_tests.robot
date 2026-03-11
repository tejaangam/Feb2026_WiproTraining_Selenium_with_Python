*** Settings ***
Resource    ../resources/common_keyword.robot
Resource    ../pages/LoginPage.robot
Test Setup     Open Browser To Login Page
Test Teardown  Close Browser Session

*** Test Cases ***
TC_01 Verify Successful Employee Login
    [Documentation]    Verify successful login with valid credentials
    Given User enters valid username
    And User enters valid password
    When User clicks login button
    Then User should login successfully

TC_02 Verify Unsuccessful Employee Login
    [Documentation]    Verify error message for invalid password
    Given User enters valid username
    And User enters invalid password
    When User clicks login button
    Then Error message should be displayed

*** Keywords ***
User enters valid username
    Enter Username    ${VALID_USERNAME}

User enters valid password
    Enter Password    ${VALID_PASSWORD}

User enters invalid password
    Enter Password    ${INVALID_PASSWORD}

User clicks login button
    Click Login Button

User should login successfully
    Verify Successful Login

Error message should be displayed
    Verify Error Message