*** Settings ***
Library     SeleniumLibrary
*** Test Cases ***
#Test case 1
Register User
    Page Should Contain    AutomationExercise
Go To Login Page
    Page Should Contain    New User Signup!

    ${random}=    Generate Random String    5
    ${email}=    Set Variable    test${random}@gmail.com

    Input Text    name=name    TestUser
    Input Text    xpath=//input[@data-qa='signup-email']    ${email}
    Click Button    xpath=//button[@data-qa='signup-button']

    Page Should Contain    ENTER ACCOUNT INFORMATION

    Click Element    id=id_gender1
    Input Text    id=password    Test@123
    Select From List By Value    id=days    10
    Select From List By Value    id=months    5
    Select From List By Value    id=years    1995

    Click Element    id=newsletter
    Click Element    id=optin

    Input Text    id=first_name    Test
    Input Text    id=last_name    User
    Input Text    id=address1    Hyderabad
    Input Text    id=state    Telangana
    Input Text    id=city    Hyderabad
    Input Text    id=zipcode    500001
    Input Text    id=mobile_number    9876543210

    Click Button    xpath=//button[@data-qa='create-account']
    Page Should Contain    ACCOUNT CREATED!
    Click Element    xpath=//a[contains(text(),'Continue')]
    Page Should Contain    Logged in as