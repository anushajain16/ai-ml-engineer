import pytest
import day_05_pytest.exercises.pytest_basics as q8
import time

def test_add():
    result = q8.sum(2,3) #Addition of two numbers
    assert result == 5
    res = q8.sum("Hello ", "World") #Concatenation of two strings
    assert res == "Hello World"

def test_divide():
    result = q8.divide(10,2) #Division of two numbers
    assert result == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError): #Test for division by zero
        q8.divide(10,0)

@pytest.mark.slow 
def test_slow_function():
    print("\n This is a slow test function - Timer started")
    time.sleep(5) #Simulating a slow function
    print("This is a slow test function - Timer ended")
    result = q8.sum(2,3) #Addition of two numbers
    assert result == 5

@pytest.mark.skip(reason="Skipping this test for demonstration purposes")
def test_skipped_function():
    result = q8.sum(2.5,3.5) #Addition of two numbers
    assert result == 6.0

@pytest.mark.xfail(reason="This test is expected to fail for demonstration purposes")
def test_expected_failure():
    result = q8.divide(10,0) #Division by zero
    assert result == 0