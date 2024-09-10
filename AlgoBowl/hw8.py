def lps(s, i, j, stored):
    if (i, j) in stored:
        return stored[(i, j)]
    if i > j:
        return 0
    if i == j:
        return 1
    if s[i] == s[j]:
        stored[(i, j)] = 2 + lps(s, i+1, j-1, stored)
    else:
        stored[(i, j)] = max(lps(s, i+1, j, stored), lps(s, i, j-1, stored))
    return stored[(i, j)]

# Example usage
s = "COMPUTERSCIENCE"
stored = {}
print(lps(s, 0, len(s)-1, stored))