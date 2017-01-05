from sinc2d import *
import numpy as np

def test_x_0_y_0():
	inputX = 0
	inputY = 0
	expected_value = 1
	calculated_value = sinc2d(inputX, inputY)
	assert expected_value == calculated_value

def test_x_0_y_n():
        inputX = 0
        inputY = 1
        expected_value = np.sin(y)/y
        calculated_value = sinc2d(inputX, inputY)
        assert expected_value == calculated_value 

def test_x_n_y_0():
        inputX = 1
        inputY = 0
        expected_value = np.sin(x)/x
        calculated_value = sinc2d(inputX, inputY)
        assert expected_value == calculated_value
