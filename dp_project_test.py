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
    bp_table = [[0] * n for _ in range(n)]
    
    for i in range(n):
        bp_table[i][i] = list_nums[i]
    
    for length in range(2, n + 1): # this is for seg. of len 2 to n
        for i in range(n - length + 1):
            j = i + length - 1
            # if you take the ith segment, opponent will choose optimally from i + 1 to j
            take_i = list_nums[i] + min(bp_table[i + 2][j], bp_table[i + 1][j - 1]) if i + 2 <= j else list_nums[i]
            # if you take the jth segment, opponent will choose optimally from i to j - 1
            take_j = list_nums[j] + min(bp_table[i + 1][j - 1], bp_table[i][j - 2]) if i <= j - 2 else list_nums[j]
            bp_table[i][j] = max(take_i, take_j)
    return bp_table[0][n - 1]

def run_timing_tests(start_n, end_n, step_n):
    times = []
    for n in range(start_n, end_n + 1, step_n):
        timber_lengths = [random.randint(1, 1000) for _ in range(n)]

        start = time.time()
        #timber(timber_lengths, 0, n - 1)
        timber_bp(timber_lengths)
        end = time.time()

        total_time = end - start
        times.append((n, total_time))
        print(f'Time for n = {n} is {total_time:.6f} seconds.')
    return times

def main():
    if len(sys.argv) > 1:
        file = sys.argv[1]
        timber_lengths = read_input_file(file)
    else:
        timber_lengths = read_input_stdin()
    #max_length = timber(timber_lengths, 0, len(timber_lengths) - 1)
    max_length = timber_bp(timber_lengths)
    print(max_length)

    #print("Starting timing tests...")
    #run_timing_tests(2, 2000, 1)
    #print("Timing tests completed.")

if __name__ == "__main__":
    main()