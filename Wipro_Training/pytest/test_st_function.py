# function level setup and tear down
#these run before and after each test function

#set up at function level

def setup_function(function):
    print("opening the browser")

def teardown_function(function):
    print("closing the browser")

import pytest

@pytest.mark.sanity
def testcase1():
    print("Testcase 1 is executed")

def testcase2():
    print("Testcase 2 is executed")

@pytest.mark.regression
#testcase 3
def test_case3():
    print("Testcase 3 is executed")

#testcase 4
def openbrowser():
    print("opening the browser")

