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
        Wait Until Element Is Visible    xpath://input[@name = 'user-name']
        #enter text in the username field
        Input Text    xpath://input[@name='user-name']    standard_user
        #enter text in the password field
        Input Text    xpath://input[@id='password']   secret_sauce
        #click login buttob
        Click Element    xpath://input[@id='login-button']
        #validate that the user is on products page
        Wait Until Element Is Visible   xpath://span[@class='title']
        Element Should Be Visible    xpath://span[@class='title']
        Sleep    5s
Adding products to cart
        Wait Until Element Is Visible   xpath://button[@id='add-to-cart-sauce-labs-backpack']
        Click Element    xpath://button[@id='add-to-cart-sauce-labs-backpack']
        Sleep    3s
        Click Element    xpath://button[@id='add-to-cart-sauce-labs-bolt-t-shirt']
        Sleep    3s
        Wait Until Element Is Visible    xpath://a[@class='shopping_cart_link']
        Click Element    xpath://a[@class='shopping_cart_link']
        Sleep    5s
Checking out the Products
        Wait Until Element Is Visible    xpath://span[@class='title']
        Click Element    xpath:(//button[normalize-space()='Checkout'])[1]
        Sleep    3s
Checkout: Your Information
        Wait Until Element Is Visible    xpath://span[@class='title']
        Input Text    xpath://input[@id='first-name']    Teja
        Input Text    xpath://input[@id='last-name']    Angam
        Input Text    xpath:(//input[@id='postal-code'])[1]    518543
        Click Element    xpath://input[@id='continue']
        Sleep    5s
Checkout: Overview
        Wait Until Element Is Visible    xpath://span[@class='title']
        Sleep    3s
        Click Element    xpath://button[@id='finish']
        Sleep    5s
        Wait Until Element Is Visible    xpath://span[@class='title']
        Sleep    6s
        #close browser
        Close Browser


