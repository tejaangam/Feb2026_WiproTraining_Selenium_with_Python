# used inside the class
# it will run for every class definition 0nce  it will run starting and  at ending of the class
#function in class won't work
#module in class won't work

import pytest
class Testclass1:
    #class level set up
    def setup_class(cls):
        print("API authorization needed with username and password")
    def teardown_class(cls):
        print("API authorization closed")

#using method in class **WORKS**
    def setup_method(method):
        print("opening the browser")

    def teardown_method(method):
        print("closing the browser")

    #testcase 1
    def testcase1(self):
        print("Testcase 1 is executed")
    #testcase2
    def testcase2(self):
        print("Testcase 2 is executed")
    #testcase 3
    def test_case3(self):
        print("Testcase 3 is executed")
    #testcase 4
    def openbrowser(self):
        print("opening the browser")




class Testclass2(Testclass1):
    #class level set up
    def setup_class(cls):
        print("API authorization needed with username and password")
    def teardown_class(cls):
        print("API authorization closed")

#using method in class **WORKS**
    def setup_method(method):
        print("opening the browser")

    def teardown_method(method):
        print("closing the browser")

    #testcase 1
    def testcase1(self):
        print("Testcase 1 is executed")
    #testcase2
    def testcase2(self):
        print("Testcase 2 is executed")
    #testcase 3
    def test_case3(self):
        print("Testcase 3 is executed")
    #testcase 4
    def openbrowser(self):
        print("opening the browser")
