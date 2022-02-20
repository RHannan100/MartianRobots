# MartianRobots

## How to run
With Python3 installed run `python3 main.py`  
Edit instructions.txt to change input values.

## What comes next
Currently the robots do not leave or look for scented gridpoints.  

The plan was to update Mars to keep a list of x,y pairs which are "scented" and pass that into the Robot's move() method. The forward() method (rotations wouldn't matter) would be updated to check that position_x/poistion_y +/-1 (depending on the orientation) wouldn't cause them to be equal to any scented gridpoints before executing the instruction.