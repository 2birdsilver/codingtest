
row, column = map(int, input().split())
data = [0] * row
minimum = 0
result = 0

for i in range(row):
    data[i] = list(map(int, input().split()))
    data[i].sort()

    if minimum <= data[i][0]:
        minimum = data[i][0]

print(minimum)

