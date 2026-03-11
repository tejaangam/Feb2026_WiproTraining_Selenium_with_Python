*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}          https://www.saucedemo.com/
*** Test Cases ***
Verify login scenario with valid credentials

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        #Wait till the element is loaded
        Wait Until Element Is Visible    xpath://input[@name='user-name']
        #enter text in the username field
        Input Text    xpath://input[@name='user-name']    admin
        #enter text in the password field
        Input Text    xpath://input[@name='password']   admin123
        #click login buttob
        Click Element    xpath://button[@type='login-button']
        #validate that the user is on the home page
        Wait Until Element Is Visible   xpath://h6[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']
        Element Should Be Visible    xpath://h6[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']
        #close browser
        Close Browser

