*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}          https://practice.automationtesting.in/

*** Test Cases ***
#Verify login scenario with valid credentials
Adding products to cart
        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        #Wait till the element is loaded
        #Wait Until Element Is Visible    xpath://input[@name = 'user-name']
        #enter text in the username field
       # Input Text    xpath://input[@name='user-name']    standard_user
        #enter text in the password field
        #Input Text    xpath://input[@id='password']   secret_sauce
        #click login buttob
        #Click Element    xpath://input[@id='login-button']
        #validate that the user is on products page
        #Wait Until Element Is Visible   xpath://span[@class='title']
        #Element Should Be Visible    xpath://span[@class='title']
        #Sleep    5s
        Wait Until Element Is Visible   xpath:(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'][normalize-space()='Add to basket'])[1]
        Click Element    xpath:(//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'][normalize-space()='Add to basket'])[1]
        #View Basket button
        Wait Until Element Is Visible    xpath=//a[contains(@class,"added_to_cart")]    10s
        Scroll Element Into View         xpath=//a[contains(@class,"added_to_cart")]
        Click Element                    xpath=//a[contains(@class,"added_to_cart")]
        Sleep    5s
#Checking out the Products
 #       Wait Until Element Is Visible    xpath://span[@class='title']
  #      Click Element    xpath:(//button[normalize-space()='Checkout'])[1]
   #     Sleep    3s
#Checkout: Your Information
 #       Wait Until Element Is Visible    xpath://span[@class='title']
  #      Input Text    xpath://input[@id='first-name']    Teja
   #     Input Text    xpath://input[@id='last-name']    Angam
    #    Input Text    xpath:(//input[@id='postal-code'])[1]    518543
     #   Click Element    xpath://input[@id='continue']
      #  Sleep    5s
#Checkout: Overview
 #       Wait Until Element Is Visible    xpath://span[@class='title']
  #      Sleep    3s
   #     Click Element    xpath://button[@id='finish']
    #    Sleep    5s
     #   Wait Until Element Is Visible    xpath://span[@class='title']
      #  Sleep    6s
        #close browser
        Close Browser


