"""Day 1 Advent code 2017"""


with open('input.txt', 'r') as inp:
    s = inp.read().strip()

# First part
print(sum(int(x) for x, y in zip(s[-1] + s, s) if x == y))

# Second part
print(2 * sum(int(x) for x, y in zip(s, s[len(s) // 2:]) if x == y))
