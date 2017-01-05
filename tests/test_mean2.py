from mean import *

def test_2():
	input = [2, 2, 2]
	input_value = mean(input)
	expected_value = 2
	calculated_value = mean(input)
	assert calculated_value == expected_value

