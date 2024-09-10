import sys
import random
import time

def read_input_file(file):
    with open(file, 'r') as f:
        input = f.read().strip()
        lines = input.strip().split('\n')
        list_length = int(lines[0])
        timber_lengths = list(map(int, lines[1].split()))
    return timber_lengths

def read_input_stdin():
    try:
        lines = [input() for _ in range(2)]
        list_length = int(lines[0])
        timber_lengths = list(map(int, lines[1].split()))
    except EOFError:
        print("Invalid Input.")
        sys.exit(1)
    return timber_lengths

def timber(list_nums, i, j):
    if i > j:
        return 0
    if i == j:
        return list_nums[i]
    return sum(list_nums[i:j+1]) - min(timber(list_nums, i + 1, j), timber(list_nums, i, j - 1))

def timber_bp(list_nums):
    n = len(list_nums)
    bp_table = [[(0, '') for _ in range(n)] for _ in range(n)]
    total_lengths = calculate_total_lengths(list_nums)
    
    for i in range(n):
        bp_table[i][i] = (list_nums[i], '')
    
    for length in range(2, n + 1): # this is for seg. of len 2 to n
        for i in range(n - length + 1):
            j = i + length - 1
            
            # calculates total sum of the lengths if player takes i
            take_i = list_nums[i] + total_lengths[j + 1] - total_lengths[i + 1] - bp_table[i + 1][j][0]
            # calculates total sum of the lengths if player takes j
            take_j = list_nums[j] + total_lengths[j] - total_lengths[i] - bp_table[i][j - 1][0]
            
            bp_table[i][j] = (take_i, 'left') if take_i >= take_j else (take_j, 'right')
    return bp_table[0][n - 1][0], bp_table

def calculate_total_lengths(segments):
    total_lengths = [0]
    for segment in segments:
        total_lengths.append(total_lengths[-1] + segment)
    return total_lengths

def reconstruct_path(bp_table, n):
    path = []
    i = 0
    j = n - 1
    
    # traceback
    while i <= j:
        direction = bp_table[i][j][1]
        if direction == 'left':
            path.append(i + 1)
            i += 1
        else:
            path.append(j + 1)
            j -= 1
    
    return path

def main():
    if len(sys.argv) > 1:
        file = sys.argv[1]
        timber_lengths = read_input_file(file)
    else:
        timber_lengths = read_input_stdin()
    max_length, bp_table = timber_bp(timber_lengths)
    path_sequence = reconstruct_path(bp_table, len(timber_lengths))
    print(max_length)
    print(' '.join(map(str, path_sequence)))

if __name__ == "__main__":
    main()