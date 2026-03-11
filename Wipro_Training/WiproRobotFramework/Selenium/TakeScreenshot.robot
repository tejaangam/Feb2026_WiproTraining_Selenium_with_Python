*** Settings ***
Library     SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}                  https://the-internet.herokuapp.com/upload
*** Test Cases ***
Verify Upload
        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        Wait Until Element Is Visible       xpath://input[@id='file-upload']
        Sleep    3s
        #Capture page screen shot
        Capture Page Screenshot         C://Pictures//Robo5.png
        #Captur Element Screen shot
        Capture Element Screenshot    xpath://input[@id='file-upload']    C://Pictures//Robo6.png
        #close browser
        Close Browser

