import pytest
from Test_fixtures import api_url
def testcase1():
    print("Testcase 1 is executed")

def testcase2():
    print("Testcase 2 is executed")

#testcase 3
def test_case3():
    print("Testcase 3 is executed")

#testcase 4
def test_case4():
    print("Testcase 4 is executed")

#testcase 4
def test_case5():
    print("Testcase 5 is executed")

def test_login():
    print("Login is executed")

def test_api(api_url):
    assert "https" in api_url