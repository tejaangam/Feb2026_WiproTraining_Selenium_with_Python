from sys import platform

import pytest
#1.Write a test that is skipped because a feature is not implemented yet.
@pytest.mark.skip(reason = "Feature is not available")
def test_new_feature():
    print("This feature is skipped")
#2.write a test that runs only on Linux and skips on Windows.
#@pytest.mark.skipif(
 #   platform.system() != "Linux",
  #  reason="Runs only on Linux"
#)
#def test_linux_only():
 #   assert True

#3.Write a test that checks an API health endpoint.
#If status code is not 200 → skip the test dynamically

#4.Mark a failing test as xfail with reason: "Bug #123".

@pytest.mark.xfail(reason = "Bug 123")
def test_fail():
    assert False

#5.You have 5 parameterized cases.
#2 are known bugs.Mark only those 2 cases as xfail without marking entire test.

@pytest.mark.parametrize(
"a, b, result", [
    (2, 3, 5),
    (6, 4, 10),
    (10, 20, 30),
        pytest.param(
            5, 8, 7,
            marks=pytest.mark.xfail(reason="Known bug")
        ),

        pytest.param(
            3, 4, 9,
            marks=pytest.mark.xfail(reason="Known bug")
        ),
]
)
def test_add(a, b, result):
    assert a + b == result

