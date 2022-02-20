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
    mars = Mars(10, 10)
    mars.add_robot(1,1,"N")
    assert(1 == mars.robots[0].position_x)
    assert(1 == mars.robots[0].position_y)
    assert("N" == mars.robots[0].get_orientation())

def test_cannot_create_robot_outside_grid():
    mars = Mars(10, 10)
    with pytest.raises(ValueError):
        mars.add_robot(10,11,"N")

def test_robot_created_for_each_instruction_pair():
    assert False

def test_robot_location_output_after_moving(capfd):
    mars = Mars(10, 10)
    mars.add_robot(1,1,"N")
    mars.run_robot(mars.robots[-1], "F")
    out, err = capfd.readouterr()
    assert(out.strip() == "1 2 N")


def test_LOST_and_final_location_output_after_moving_oob():
    assert False