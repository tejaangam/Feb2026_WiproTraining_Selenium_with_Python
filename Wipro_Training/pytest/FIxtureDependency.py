#fixture dependency : The second fixture works only when the first dependency

import pytest

def test(fixture_b):
    assert fixture_b == "Data from A + Data from B"
