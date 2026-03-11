# module level - runs once per module (file)
# use module level set up and tear down when you want to execute the set up and tear down once in the current file
# eg open the db connection execute all the testcases and at alst close the db connection
# setup_module - -> only one per file
# setup_class() → one per class
# setup_method() → one per class
# setup_function() → one per class

import pytest
def setup_module(module):
    print("open the db connection")

def teardown_module(module):
    print("closing the db connection")

#testcase 1
def test_read():
    print("Reading the db")

#test_case 3
def test_write():
    print("writing the data to db")

#testcase 3
def test_update():
    print("updating the db")

#testcase 4
def openbrowser():
    print("opening the browser")