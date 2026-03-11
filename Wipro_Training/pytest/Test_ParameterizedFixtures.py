import pytest

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    print("Current browser:", request.param)
    return request.param

def testbrowser(browser):
    assert browser in ["chrome", "firefox"]


#selecting even or odd

@pytest.fixture(params=[2, 4, 6, 8])
def even(request):
    return request.param

def testeven(even):
    assert even % 2 == 0
