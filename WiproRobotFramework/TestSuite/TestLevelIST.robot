*** Settings ***
#setting we add the external library details, resources

Resource        ./../Resources/Resources.robot
Library         SeleniumLibrary
Test Setup      Launch Browser
Test Teardown   Close the Browser

*** Test Cases ***
Verify login with valid credentials
        Login
Verify Add to cart functionality
        Login

       Log    User selects the product
       Log    User adds the product to the cart
       Log    User verifies that the product with details is added to the cart