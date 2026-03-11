*** Settings ***
Library     SeleniumLibrary

*** Keywords ***
Login
        Log    Enter username
        Log    Enter password
        Log    click on login button
        Log     user is on the home page

Launch Browser
        Log     Launching the browser
Close the Browser
        Log    Closing the browser


open db
        Log     opening the db
close db
        Log    Closing the db