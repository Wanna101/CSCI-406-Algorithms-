class MazeSolver:
    
    def __init__(self, number_of_rooms, number_of_corridors, rocket_initial, lucky_initial, colors_of_rooms):
        self.number_of_rooms = number_of_rooms
        self.number_of_corridors = number_of_corridors
        self.rocket_initial = rocket_initial
        self.lucky_initial = lucky_initial
        self.colors_of_rooms = colors_of_rooms
        self.corridors = [[] for i in range(number_of_rooms - 1)]
        self.states = [[[] for p in range(number_of_rooms - 1)] for j in range(number_of_rooms - 1)]
        self.visited = [[False for k in range(number_of_rooms)] for f in range(number_of_rooms)]
        self.path = []

    def construct_graph(self):
        for i in range(self.number_of_corridors):
            line = input().split()
            self.corridors[int(line[0]) - 1].append({'dest': int(line[1]) - 1, 'color': line[2]})

        for i in range(self.number_of_rooms - 1):
            for j in range(self.number_of_rooms - 1):
                for k in range(len(self.corridors[i])):
                    if self.corridors[i][k]['color'] == self.colors_of_rooms[j]:
                        self.states[i][j].append({'rocket': self.corridors[i][k]['dest'], 'lucky': j})
                for k in range(len(self.corridors[j])):
                    if self.corridors[j][k]['color'] == self.colors_of_rooms[i]:
                        self.states[i][j].append({'rocket': i, 'lucky': self.corridors[j][k]['dest']})

    def dfs(self, v, u):
        if v == self.number_of_rooms - 1 or u == self.number_of_rooms - 1:
            return True
        self.visited[v][u] = True
        for i in range(len(self.states[v][u])):
            x = self.states[v][u][i]['rocket']
            y = self.states[v][u][i]['lucky']
            if not self.visited[x][y] and self.dfs(x, y):
                if v == x:
                    self.path.append({'person': 'L', 'corridor': y + 1})
                elif u == y:
                    self.path.append({'person': 'R', 'corridor': x + 1})
                return True
        return False
    
    def run(self):
        self.construct_graph()
        if not self.dfs(self.rocket_initial, self.lucky_initial):
            print('No Path')
            exit(0)
        while len(self.path) != 0:
            instruction = self.path.pop()
            print(instruction['person'], instruction['corridor'])

