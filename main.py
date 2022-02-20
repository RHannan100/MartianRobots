from mars import Mars


instruction_set = open("instructions.txt", "r")
for index, instruction in enumerate(instruction_set):
    if index == 0:
        mars = Mars(int(instruction[0]), int(instruction[2]))
    elif (index % 2) != 0:
        mars.add_robot(int(instruction[0]), int(instruction[2]), instruction[4])
    else:
        mars.run_robot(mars.robots[-1], instruction)

instruction_set.close()