import fileinput
import sys
from Graph import *
from copy import deepcopy


def algorithm():
    # backup is a stack for storing latest states
    backup = []
    index = 0
    # do this loop till reach goal or backup stack is empty
    while not g.goal_check():
        # get available actions
        actions = g.actions()
        # if there's no action available go to latest state in backup
        if index + 1 > len(actions):
            # if backup stack is empty this problem can not be solved
            if not backup:
                print("NOT SOLVABLE")
                return
            # change rocket and lucky location to previous location
            else:
                this_backup = backup.pop()
                g.rocket = this_backup[0]
                g.lucky = this_backup[1]
                # delete latest action from output
                del output[-1]
                # do next action in previous state
                index = this_backup[2] + 1
        else:
            # check if we can reach to goal from this state
            for i in range(len(actions)):
                if actions[i][0] == int(num_of_points) - 1:
                    g.do(actions[i])
                    output.append(actions[i])
                    return
            # do one of the actions and add it to output and make a backup of it
            backup.append([deepcopy(g.rocket), deepcopy(g.lucky), index])
            g.do(actions[index])
            output.append(actions[index])
            index = 0


# =========== GET INPUT FROM FILE ==================
Input = fileinput.input(sys.argv[1])
# gets line 1 - 3 line by line and assigns it to variables
print(sys.argv[1])
print(Input[0])
line1 = Input[0].replace('\n', '').split(' ')
line2 = Input[1].replace('\n', '').split(' ')
line3 = Input[2].replace('\n', '').split(' ')
num_of_points = line1[0]
num_of_edges = line1[1]
colors = line2
# color of goal node is goal for goal checking
colors.append('goal')
rocket_loc = line3[0]
lucky_loc = line3[1]
# read other lines for edges and encode it
edges = []
for line in Input:
        line_numbers = [num_of_edges for num_of_edges in line.split()]
        edges.append(line_numbers)
for edge in edges:
    edge[0] = int(edge[0]) - 1
    edge[1] = int(edge[1]) - 1
# =========== GENERATE OUTPUT USING ALGORITHM FUNCTION ==================
# generate a graph using given data
g = Graph(int(num_of_points), colors, int(rocket_loc), int(lucky_loc), edges)
output = []
# run algorithm function
algorithm()
# print output
for action in output:
    print(action[1], "   ", action[0] + 1)
