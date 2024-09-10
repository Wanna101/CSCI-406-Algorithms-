'''
def stirling(n, k):
        if n == k:
            return 1
        elif n == 0 or k == 0:
            return 0
        elif k == 1:
            return 1
        elif n < k:
            return 0
        return k * stirling(n - 1, k) + stirling(n - 1, k - 1)
'''

'''
stored = {}
def stirling(n, k, stored):
    if (n, k) in stored:
        return stored[(n, k)]
    if n == k:
        return 1
    elif n == 0 or k == 0:
        return 0
    elif k == 1:
        return 1
    elif n < k:
        return 0
    stored[(n, k)] = k * stirling(n - 1, k, stored) + stirling(n - 1, k - 1, stored)
    return stored[(n, k)]
'''
'''
def stirling(n, k):
    table = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n+1):
        table[i][0] = 0
    for i in range(min(n, k) + 1):
        table[i][i] = 1
    for i in range(2, n+1):
        for j in range(1, min(i, k)+1):
            table[i][j] = j * table[i-1][j] + table[i-1][j-1]
    return table[n][k]
'''
'''
n_example, k_example = 0, 0
stirling_result = stirling(n_example, k_example)
print(stirling_result)

'''
'''
def F(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return F(n - 1) + F(n - 2) + F(n - 3)
'''
'''
def F(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    ways = [0] * (n+1)
    ways[0] = 1  

    for i in range(1, n+1):
        ways[i] += ways[i - 1] if i - 1 >= 0 else 0
        ways[i] += ways[i - 2] if i - 2 >= 0 else 0
        ways[i] += ways[i - 3] if i - 3 >= 0 else 0

    return ways[n]
'''

def F(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    ways = [0, 1, 2, 4] + [0] * (n - 3)
    for length in range(4, n + 1):
        ways[length] = ways[length - 1] + ways[length - 2] + ways[length - 3]
    return ways[n]




for i in range(0, 7):
    print(F(i))



'''
for i in range(8):
     for j in range(8):
            n_example, k_example = i, j
            stirling_result = stirling(n_example, k_example)
            print(f"({i},{j}): {stirling_result}")
'''