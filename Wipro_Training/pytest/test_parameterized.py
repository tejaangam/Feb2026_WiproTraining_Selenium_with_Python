import pytest


#multiple parameters
@pytest.mark.parametrize("a, b, result", [
    (2, 3, 5),
    (6, 4, 10),
    (10, 20, 30)
])

def test_add(a, b, result):
    assert a + b == result

#single parameter
@pytest.mark.parametrize("number", [2, 4, 6, 8])
def test_even(number):
    assert number % 2 == 0

#dictionary items
@pytest.mark.parametrize("payload", [
    {"name": "Teja", "age":22},
    {"name":"Bobby", "age":18}
])

def test_create_user(payload):
    assert payload["age"] >= 18