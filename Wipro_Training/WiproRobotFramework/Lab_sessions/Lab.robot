'''
Create a scalar variable ${NAME} and print it.
Assign two numbers to variables and print their sum.
Create a variable ${CITY} and use it inside a sentence.
Reassign a variable value inside a test case and log the updated value.
Create a list variable @{FRUITS} and print the first item.
Loop through a list variable and print each element.
Find the length of a list variable.
Create a dictionary variable &{USER} and print one key value.
Add a new key-value pair to a dictionary variable.
Access dictionary values inside a loop and print key and value.
'''

*** Settings ***

Library     SeleniumLibrary
Library    Collections

*** Variables ***
${NAME}     Teja
${number1}  4
${number2}  5
${sum}      ${None}
${city}     Hyderabad
@{FRUITS}   mango   banana  apple
&{USER}    name=Teja    city=Hyderabad    age=23
*** Test Cases ***
My Test cases
        ${sum}=     Evaluate    ${number1} + ${number2}
        Log To Console  ${NAME}
        Log To Console  ${sum}
        Log To Console    I am from ${CITY}.
        Log To Console    Before update: ${CITY}
                         ${CITY}=    Set Variable    Chennai
        Log To Console    After update: ${CITY}
        Log To Console    ${FRUITS}[0]
        FOR    ${fruit}    IN    @{FRUITS}
            Log To Console    ${fruit}
        END
        ${length}=    Get Length    ${FRUITS}
        Log To Console    ${length}
        Log To Console    Name: ${USER}[name]
        Set To Dictionary    ${USER}    country=India
        Log To Console    Country: ${USER}[country]
        FOR    ${key}    ${value}    IN    &{USER}
        Log To Console    ${key} : ${value}
    END