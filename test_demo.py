import pytest

@pytest.fixture()
def setup_teardown():
    print("\nBefore Test") # Before test
    yield # Here test is executed.
    print("\nTaking Screenshot") # After test
    print("Taking Logs") # After test

def test_demo1():
    assert 1 == 1

def test_demo2(setup_teardown):
    print("Testing!")
    assert 2 > 1