from maze_solver import MazeSolver

colors_of_rooms = []
line = input().split()
number_of_rooms = int(line[0])
number_of_corridors = int(line[1])
line = input().split()
for i in range(number_of_rooms - 1):
    colors_of_rooms.append(line[i])
line = input().split()
rocket_initial = int(line[0]) - 1
lucky_initial = int(line[1]) - 1

maze_solver = MazeSolver(number_of_rooms, number_of_corridors, rocket_initial, lucky_initial, colors_of_rooms)
maze_solver.run()
