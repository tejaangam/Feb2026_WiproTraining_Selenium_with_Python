# scope is run before and after every function

import pytest

@pytest.mark.usefixtures("openbrowser")
def test_login():
    print("enter the name")
    print("enter the password")
    print("click the login button")

@pytest.mark.usefixtures("closebrowser")
def test_logout():
    print("user logged out")