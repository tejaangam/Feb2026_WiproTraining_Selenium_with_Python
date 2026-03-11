#xfail is a marker used to indicate that a test is expected to fail due to a known issue (e.g., a bug or an unimplemented feature)
import sys

import pytest

def test_function_with_bug():
    assert (1 + 1) == 3
def testcase1():
   print("Testcase 1 is executed")
def testcase2():
    print("Testcase 2 is executed")
    # testcase 3
@pytest.mark.xfail
def test_case3():
    print("Testcase 3 is executed")

#xfail with a condition
@pytest.mark.xfail(sys.platform == "win32", reason = "Bug on windows")
def test():
    print("test on windows")

#strict =True XFAIL FAILED Fails the test suite
@pytest.mark.xfail(strict=True, reason = "Bug #1234 is not fixed")
def test_function():
    assert True