import pytest
from mars import Mars

def test_mars_x_axis_cannot_exceed_50():
    with pytest.raises(ValueError):
        Mars(51,10)

def test_mars_y_axis_cannot_exceed_50():
    with pytest.raises(ValueError):
        Mars(10,51)

def test_mars_x_axis_cannot_be_negative():
    with pytest.raises(ValueError):
        Mars(-10,10)

def test_mars_y_axis_cannot_be_negative():
    with pytest.raises(ValueError):
        Mars(10,-10)

def test_maximum_instruction_string_is_less_than_100():
    assert False

def test_robot_created_at_input_gridpoint():
    assert False

def test_robot_created_for_each_instruction_pair():
    assert False

def test_robot_location_output_after_moving():
    assert False

def test_LOST_and_final_location_output_after_moving_oob():
    assert False