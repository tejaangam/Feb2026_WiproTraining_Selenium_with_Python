*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${MY_INFO_MENU}      xpath://span[text()='My Info']
${FIRSTNAME_FIELD}   xpath://input[@name='firstName']
${SAVE_BUTTON}       xpath://button[@type='submit']
${EMPLOYEE_ID}       xpath://label[text()='Employee Id']/../following-sibling::div/input
${LOADER}    xpath=//div[contains(@class,'oxd-form-loader')]

*** Keywords ***
Navigate To Personal Details
    Click Element    ${MY_INFO_MENU}
    Wait Until Element Is Not Visible    ${LOADER}    25s
    Wait Until Element Is Visible        ${FIRSTNAME_FIELD}    15s

Update First Name
    [Arguments]    ${new_name}
    Wait Until Element Is Not Visible    ${LOADER}    15s
    Wait Until Element Is Visible        ${FIRSTNAME_FIELD}    15s
    Scroll Element Into View             ${FIRSTNAME_FIELD}
    Click Element                        ${FIRSTNAME_FIELD}

    ${current_value}=    Get Value    ${FIRSTNAME_FIELD}
    ${length}=           Get Length    ${current_value}

    FOR    ${i}    IN RANGE    ${length}
        Press Keys    ${FIRSTNAME_FIELD}    BACKSPACE
    END

    Input Text    ${FIRSTNAME_FIELD}    ${new_name}

Click Save
    Wait Until Element Is Not Visible    ${LOADER}    10s
    Wait Until Element Is Enabled        ${SAVE_BUTTON}    10s
    Scroll Element Into View             ${SAVE_BUTTON}
    Click Element                        ${SAVE_BUTTON}

Verify First Name Updated
    [Arguments]    ${new_name}
    Textfield Value Should Be    ${FIRSTNAME_FIELD}    ${new_name}

#Verify Employee ID Disabled
#   Element Should Be Disabled    ${EMPLOYEE_ID}