from robot import Robot


def test_instruction_limits():
    robot = Robot(0,0,"N")
    assert robot.move("F") != -1
    assert robot.move("L") != -1
    assert robot.move("R") != -1
    assert robot.move("Q") == -1
    assert robot.move("W") == -1
    assert robot.move("1") == -1
    assert robot.move(1) == -1
    assert robot.move(["F"]) == -1

def test_l_instruction_stays_on_current_gridpoint():
    robot = Robot(0,0,"N")
    initial_gridpoint = robot.get_location()
    robot.move("L")
    assert initial_gridpoint == robot.get_location()

def test_r_instruction_stays_on_current_gridpoint():
    robot = Robot(0,0,"N")
    initial_gridpoint = robot.get_location()
    robot.move("L")
    assert initial_gridpoint == robot.get_location()

def test_l_instruction_rotates_anticlockwise_to_correct_orientation():
    robot = Robot(0,0,"N")
    robot.set_orientation("N")
    robot.move("L")
    assert "W" == robot.get_orientation()
    robot.move("L")
    assert "S" == robot.get_orientation()
    robot.move("L")
    assert "E" == robot.get_orientation()
    robot.move("L")
    assert "N" == robot.get_orientation()

def test_r_instruction_rotates_clockwise_to_correct_orientation():
    robot = Robot(0,0,"N")
    robot.set_orientation("N")
    robot.move("R")
    assert "E" == robot.get_orientation()
    robot.move("R")
    assert "S" == robot.get_orientation()
    robot.move("R")
    assert "W" == robot.get_orientation()
    robot.move("R")
    assert "N" == robot.get_orientation()

def test_f_instruction_maintains_orientation():
    robot = Robot(0,0,"N")
    robot.set_orientation("N")
    robot.move("F")
    assert "N" == robot.get_orientation()

def test_f_instruction_increments_y_axis_when_facing_north():
    robot = Robot(0,0,"N")
    robot.set_orientation("N")
    initial_y = robot.get_location()["y"]
    robot.move("F")
    assert (initial_y + 1) == robot.get_location()["y"]

def test_f_instruction_increments_x_axis_when_facing_east():
    robot = Robot(0,0,"N")
    robot.set_orientation("E")
    initial_x = robot.get_location()["x"]
    robot.move("F")
    assert (initial_x + 1) == robot.get_location()["x"]

def test_f_instruction_decrements_y_axis_when_facing_south():
    robot = Robot(0,0,"N")
    robot.set_orientation("S")
    initial_y = robot.get_location()["y"]
    robot.move("F")
    assert (initial_y - 1) == robot.get_location()["y"]

def test_f_instruction_decrements_x_axis_when_facing_west():
    robot = Robot(0,0,"N")
    robot.set_orientation("W")
    initial_x = robot.get_location()["x"]
    robot.move("F")
    assert (initial_x - 1) == robot.get_location()["x"]

def test_leaving_grid_marks_robot_lost():
    assert False

def test_last_gridpoint_marked_when_robot_lost():
    assert False
