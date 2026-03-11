*** Settings ***
Library     SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}                  https://the-internet.herokuapp.com/hovers
*** Test Cases ***
Verify Drag and Drop

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        Wait Until Element Is Visible       xpath://div[@class='example']//div[1]//img[1]
        Sleep    2s

        #Mouse Hover
        Mouse Over    xpath://div[@class='example']//div[1]//img[1]
        Element Should Be Visible    xpath://h5[normalize-space()='name: user1']
        Sleep    2s
        #close browser
        Close Browser

