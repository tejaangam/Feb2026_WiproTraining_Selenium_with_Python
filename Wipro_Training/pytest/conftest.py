#The conftest.py file in pytest serves as a local, per-directory plugin that is automatically discovered and
#used by tests within its directory and subdirectories
import pytest
@pytest.fixture
def simple_data():
    return 45


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    print("Current browser:", request.param)
    return request.param

@pytest.fixture()
def api_url():
    return  "https://api.example.com"

@pytest.fixture(scope = 'function')
def openbrowser():
    # precondition
    print("open the browser")

@pytest.fixture(scope = 'function')
def closebrowser():
     # post condition
    print("closing the browser")

#class level
@pytest.fixture(scope = 'class')
def dbconnection():
    # precondition
    print("open the db connection")
    yield
    print("closing the db connection")
#module level

@pytest.fixture(scope = "module")
def setupapi():
    print("Authorize apis with username and password") # setup
    yield
    print("Unauthorize apis with username and password") # tear down

@pytest.fixture(scope = "session")
def sessionsetup():
    print("Tests started on QA environment")
    yield
    print("Tests finished on QA environment")

#Fixture Dependency


@pytest.fixture()
def fixture_a():
    return "Data from A"

@pytest.fixture()
def fixture_b(fixture_a): # calling another fixture
    return f"{fixture_a} + Data from B"