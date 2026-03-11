*** Settings ***

Library     SeleniumLibrary

*** Variables ***
#A scalar variable can only contain one value- $
#A list variable can contain multiple values - @
#A dictionary variable can contain multiple key-pair values- &

${name}     John
${city}     Hyderabad
${address}  Gachibowli
@{list1}    green   blue    red
@{list2}    apple   mango   banana
&{creds}    username=admin  password=admin123

*** Test Cases ***
Verify the variables
    Log    ${name}
    Log    ${city}
    Log    ${address}
    FOR    ${element}    IN    @{list1}
        Log    ${element}

    END
    FOR    ${element}    IN    @{list2}
        Log    ${element}

    END
    Log     ${list1}[0]
    Log     ${list2}[1]
    Log     ${creds}[username]
    Log     ${creds}[password]