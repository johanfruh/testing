from mean import *

def test_ints():
	input = [1, 2, 3, 4, 5]
	calculated_value = mean(input)
	expected_value = 4
	assert calculated_value == expected_value

