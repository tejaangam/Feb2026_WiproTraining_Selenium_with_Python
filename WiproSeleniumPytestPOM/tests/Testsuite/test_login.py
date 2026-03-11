#Check the title of the web page

import pytest

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_title(self):
        print(self.driver.title)
        assert "OrangeHRM" in self.driver.title


    #    // input[ @ name = 'username']
    #   // input[ @ name = 'password']
    #  // button[normalize - space() = 'Login']
