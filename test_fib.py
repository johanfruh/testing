from fib import *

def test_zero():
	value = 0
	expected_value = 1
	calculated_value = fib(value)
	assert expected_value == calculated_value

def test_one():
	value = 1
	expected_value = 1
	calculated_value = fib(value)
	assert expected_value == calculated_value

def test_intNumber():
	value = 4
	expected_value = 5
	calculated_value = fib(value)
	assert expected_value == calculated_value

def test_floatNumber():
	value = 4.0
	expected_value = 5.0
	calculated_value = fib(value)
	assert expected_value == calculated_value

