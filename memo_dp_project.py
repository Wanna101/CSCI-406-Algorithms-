def min_max(segments, i, j, turn, memo):
    # Base case: no more segments to choose from
    if i > j:
        return 0
    
    # If we have already solved this subproblem, return the stored result
    if memo[i][j] is not None:
        return memo[i][j]
    
    # Maximizing player's turn
    if turn:
        pick_i = segments[i] + min_max(segments, i + 1, j, False, memo)
        pick_j = segments[j] + min_max(segments, i, j - 1, False, memo)
        result = max(pick_i, pick_j)
    # Minimizing opponent's turn
    else:
        pick_i = min_max(segments, i + 1, j, True, memo)
        pick_j = min_max(segments, i, j - 1, True, memo)
        result = min(pick_i, pick_j)
    
    memo[i][j] = result
    return result

def reconstruct_sequence(segments, i, j, memo):
    sequence = []
    player_turn = True
    while i <= j:
        if player_turn:
            # Player's turn, choose the option with the higher score from memo table
            if (i+1 <= j and memo[i+1][j] < memo[i][j-1]) or i+1 > j:
                sequence.append(j+1)  # +1 to convert to 1-based indexing
                j -= 1
            else:
                sequence.append(i+1)  # +1 to convert to 1-based indexing
                i += 1
        else:
            # Opponent's turn, choose the option with the lower score
            if (i+1 <= j and memo[i+1][j] < memo[i][j-1]) or i+1 > j:
                i += 1
            else:
                j -= 1
        player_turn = not player_turn  # Switch turns
    return sequence

segments = [5, 6, 9, 7]
# Initialize memoization table
n = len(segments)
memo = [[None for _ in range(n)] for _ in range(n)]

# Get the maximum length the player can obtain
max_length = min_max(segments, 0, n-1, True, memo)

# Reconstruct the sequence of choices
sequence = reconstruct_sequence(segments, 0, n-1, memo)

actual_sequence = [segments[i-1] for i in sequence]

print(max_length)
print(" ".join(map(str, sequence)))  # This prints the sequence of indices taken
print(" ".join(map(str, actual_sequence)))    # This prints the actual lengths in the order they were taken