*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}          https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

*** Test Cases ***
Verify login scenario with valid credentials

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        #Wait till the element is loaded
        Wait Until Element Is Visible    xpath://input[@name = 'username']
        #enter text in the username field
        Input Text    xpath://input[@name='Username']    admin
        #enter text in the password field
        Input Text    xpath://input:[@name ='Password']   admin123
        #click login buttob
        Click Element    xpath://button[@type='submit']
        #validate that the user is on the home page
        Wait Until Element Is Visible   xpath://h6[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']
        Element Should Be Visible    xpath://h6[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']
        #close browser
        Close Browser

