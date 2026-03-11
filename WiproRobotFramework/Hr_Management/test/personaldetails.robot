*** Settings ***
Resource    ../resources/common_keyword.robot
Resource    ../pages/LoginPage.robot
Resource    ../pages/PersonalDetailsPage.robot
Test Setup     Open Browser To Login Page
Test Teardown  Close Browser Session

*** Test Cases ***
TC_03 Modify First Name With Valid Data
    Given User logs into the system
    When User navigates to Personal Details
    And User updates first name with valid value
    And User clicks save button
    Then First name should be updated
    And Employee ID field should be disabled

*** Keywords ***
User logs into the system
    Enter Username    ${VALID_USERNAME}
    Enter Password    ${VALID_PASSWORD}
    Click Login Button
    Verify Successful Login

User navigates to Personal Details
    Navigate To Personal Details

User updates first name with valid value
    Update First Name       Teju

User clicks save button
    Click Save

First name should be updated
    Verify First Name Updated    Teju

#Employee ID field should be disabled
#    Verify Employee ID Disabled