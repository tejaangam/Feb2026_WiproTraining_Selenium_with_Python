*** Settings ***
#setting we add the external library details, resources

Resource        ./../Resources/Resources.robot
Library         SeleniumLibrary
Test Setup      open db
Test Teardown   close db

*** Test Cases ***
Verify login with valid credentials
        Login
Verify Add to cart functionality
        Login

       Log    User selects the product
       Log    User adds the product to the cart
       Log    User verifies that the product with details is added to the cart