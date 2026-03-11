*** Settings ***
Library           SeleniumLibrary
Suite Setup       Open Browser To Store
Suite Teardown    Close Browser
Test Setup        Maximize Browser Window

*** Variables ***
${URL}            https://practice.automationtesting.in/
${BROWSER}        chrome
${FIRST_NAME}     John
${LAST_NAME}      Doe
${EMAIL}          john.doe@example.com
${PHONE}          9999999999
${ADDRESS}        123 Main Street
${CITY}           Hyderabad
${STATE}          Telangana
${POSTCODE}       500001
${COUNTRY}        India

*** Test Cases ***
End To End Shop Checkout
    Add Product To Basket
    View Basket
    Proceed To Checkout
    Fill Billing Details
    Place The Order
    Order Should Be Successful

*** Keywords ***
Open Browser To Store
    Open Browser    ${URL}    ${BROWSER}

Add Product To Basket
    # Navigate to Shop
    Click Element    xpath=//a[text()="Shop"]

    # Add first product
    Click Button    xpath=(//div[contains(@class,"products")]//a[text()="Add to basket"])[1]

    Sleep    1s

View Basket
    # View Basket
    Click Element    xpath=//a[contains(@class,"view-cart") or contains(text(),"Basket")]

Proceed To Checkout
    # Click Proceed to Checkout button
    Click Element    xpath=//a[contains(text(), "Proceed to Checkout")]

Fill Billing Details
    # Billing form
    Input Text    xpath=//input[@id="billing_first_name"]       ${FIRST_NAME}
    Input Text    xpath=//input[@id="billing_last_name"]        ${LAST_NAME}
    Input Text    xpath=//input[@id="billing_email"]            ${EMAIL}
    Input Text    xpath=//input[@id="billing_phone"]            ${PHONE}

    # Country selection
    Click Element    xpath=//span[@id="select2-chosen-1"]
    Input Text       xpath=//input[@id="s2id_autogen1_search"]    ${COUNTRY}
    Press Keys       xpath=//input[@id="s2id_autogen1_search"]    ENTER

    Input Text    xpath=//input[@id="billing_address_1"]         ${ADDRESS}
    Input Text    xpath=//input[@id="billing_city"]              ${CITY}
    Input Text    xpath=//input[@id="billing_state"]             ${STATE}
    Input Text    xpath=//input[@id="billing_postcode"]          ${POSTCODE}

    Sleep    1s

Place The Order
    Scroll Element Into View    xpath=//button[@id="place_order"]
    Click Button               xpath=//button[@id="place_order"]

Order Should Be Successful
    Wait Until Element Is Visible    xpath=//p[contains(text(),"Thank you. Your order has been received")]
    Log    Order placed successfully!

*** Teardown ***
Close Browser