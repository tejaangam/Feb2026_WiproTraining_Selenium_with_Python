*** Settings ***
Library     SeleniumLibrary
Library     DataDriver      file=C:/Users/hp/Wipro_Training/WiproRobotFramework/Test Data/ddtLogindataCSV.csv   file_name=ddtLogindataCSV.csv
#testt template provide a data-driven approach to testing by a single keyword (the template)
#to be executed
Test Template       Login Test
Test Setup      Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    chrome
Test Teardown       Close Browser

*** Test Cases ***
Login Test      ${username} and ${password}

*** Keywords ***
Login Test
        [Arguments]     ${username}     ${password}
        #maximize the browser window
        Maximize Browser Window
        #wait until element is loaded
        Wait Until Element Is Visible    xpath://input[@name='username']
        #enter the username in the username field
        Input Text    xpath://input[@name='username']    ${username}
        #enter text into the password
        Input Text    xpath://input[@name='password']    ${password}
        #click the log in button
        Click Element    xpath://button[@type='submit']
        #validate that the user is on the home page
        Wait Until Element Is Visible    //h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']
        Element Should Be Visible    //h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']
        #close browser
        Sleep    10s
        Close Browser