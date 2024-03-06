
row, column = map(int, input().split())
result = 0

for i in range(row):
    data = list(map(int, input().split()))
    result = max(result, min(data))

print(result)

