from pytest_check import check


#basic assertion
#hard assertions - this will stop the execution of the test cases / test suite
#soft assertions - continue if assertion fails also

#1.basic assertion
def test_add():
    result = 2 +3
    assert result == 5

#2.checking true or false
def test_boolean():
    assert True
    assert not False

#3.none value
def test_none():
    value = None
    assert value is None

#4.List assertion
def test_list():
    fruits = ["apple", "banana", "mango", "pineapple"]
    assert "banana" in fruits

#5.Dict assertion
def test_dict():
    creds = {"username" : "admin", "password" : "admin123"}
    assert creds["password"] == "admin123"

#6.assertion with custom message
def test_custommsg():
    result = 10
    assert result == 10 , "Result should be 10"

#7.soft assertion
def test_multiple():
    check.equal(1,2)
    check.equal(3,3)