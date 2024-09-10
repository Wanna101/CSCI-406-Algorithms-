"""
Initial Issue and HW#2 prb. 1: 
Describe the graph model for Spacewreck. How will you
encode the complexities and rules of the game into a graph? You must be able to run an
unmodified BFS to find the shortest sequence of moves for either Captain Rocket or
Lieutenant Lucky to reach the Goal. In order for BFS to work, your model must have
exactly one start vertex and exactly one finish vertex.
"""

"""
2 Input Format
Your code will first read the input from a file, which is specified as follows:
    • Line 1 contains two integers, 3 ≤ n ≤ 625 and 0 ≤ m ≤ 10n.
    • Line 2 contains n − 1 space-delimited items where the ith item represents the color of the ith vertex. 
      The vertex with index n is the goal and has no color. There can be up to n − 1 unique colors.
    • Line 3 contains two integers s1 and s2, representing the index of the starting rooms of Captain Rocket
      and Lieutenant Lucky, respectively. You may assume they will not start at the goal.
    • Each of the next m lines contains two integers a and b and item c, in that order, representing a corridor 
      with color c from a to b. Note that a, b ∈ [1, n]. The input below corresponds to the example in Fig. 1
      where 1 is A, 2 is B, . . ., 7 is G and 8 is the Goal vertex. The two colors are R (red) and G (green).

        8 15
        G R G G R R G
        1 2
        1 3 G
        1 4 G
        2 1 G
        2 3 R
        3 5 G
        3 6 R
        4 2 G
        4 3 G
        5 7 G
        5 8 R
        6 4 R
        6 5 R
        6 7 R
        6 8 G
        7 8 R

3 Output Format
The output will describe a path with each line describing one step. Each line contains a character (either R or L),
followed by a space, then an integer x, indicating that Rocket or Lucky respectively moved to room x. One possible
path may start off as follows
    L 1 // Lucky goes to A
    R 4 // Rocket goes to D
    L 3 // Lucky goes to C
    etc
Please output this path concatenated into a single line with all whitespace removed (e.g. L1R4L3).
The output should consist of the shortest path to solve the logic maze. If there are multiple
shortest paths, output the path that occurs first lexicographically. For example, if we had two
shortest paths L1R4L5 and L1L4R5, L comes before R in the alphabet, so we would output the path
L1L4R5. If we had two shortest paths L1L4L5 and L1L300L5, we would output L1L300L5. If no
valid sequence of moves exists from the start to the goal, then output “NO PATH”.
"""

"""
BFS Algorithm
Enqueue(R, R_s)
Enqueue(L, L_s)
while (R is not empty or L is not empty) do
    u = first element in R
    for each v adjacent to u
        if (visited_state[v] == WHITE) then
            visited_state[v] = GRAY
            d[v] = d[u] + 1
            parent[v] = u
            Enqueue(R, v)
    Dequeue(R)
    visited_state[u] = BLACK
"""

'''
NOTES:
- Set array of visted_state to all white initially
- visted_state[1] = white … visted_state[7] = white
- Parent[3] 
- Adjacency[1] = [ (3,'G') (4,'G') ]
- Need a current position array for character 1 and character 2 
- does each player do their own BFS?
- deriving the passageways the colors? Where to store?
- how does the algorithm find the shortest path with the distances? It doesn't do anything, it's not used it's only assigned
-node_color array representing each node color, adjacency_array of tuples representing the node link and color thus representing the graph (question: is this a valid construction as to not get the 25 pt deduction?)
'''