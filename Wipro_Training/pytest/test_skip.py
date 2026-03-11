#skip - if defects are there
#skip - if the testcases are absolute
#windows, mobile, -OS dependency
#browsers - Firefox, chrome, IE

import pytest

def testcase1():
    print("Testcase 1 is executed")

def testcase2():
    print("Testcase 2 is executed")

@pytest.mark.skip
#testcase 3
def test_case3():
    print("Testcase 3 is executed")

#testcase 4
def openbrowser():
    print("opening the browser")
