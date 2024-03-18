horizon = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
d = [-1, 1]

input = input()
x, y = horizon.index(input[0]), int(input[1])
result = 0

for i in d:
    dx = x + (2 * i)
    for j in d:
        dy = y + j
        if (dx>=1 and dy>=1):
            result += 1

for i in d:
    dy = y + (2 * i)
    for j in d:
        dx = x + j
        if (dx>=1 and dy>=1):
            result += 1

print(result);



