"""Day 1 Advent code 2017"""


with open('input2.txt', 'r') as inp:
    S = inp.read().strip()

# First part
print(sum(int(x) for x, y in zip(S[-1] + S, S) if x == y))

# Second part
print(2 * sum(int(x) for x, y in zip(S, S[len(S) // 2:]) if x == y))
