#grouping-- set of testcases run together -- issue fix in that modu


import pytest

def testcase1():
    print("Testcase 1 is executed")

@pytest.mark.sanity
def testcase2():
    print("Testcase 2 is executed")

@pytest.mark.regression
#testcase 3
def test_case3():
    print("Testcase 3 is executed")


