*** Settings ***

Library     SeleniumLibrary

*** Test Cases ***
#name of the testcase
Verify login with valid credentials
        Login
Verify Add to cart functionality
                Login
        Log     user selects the product
        Log     user adds the product to the cart
        Log     user verifies that the product is same


*** Keywords ***
Login
        Log    Enter usecdrname
        Log    Enter password
        Log    click on login button
        Log     user is on the home page