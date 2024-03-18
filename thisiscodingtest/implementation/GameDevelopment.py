row, column = map(int, input().split())
d = [[0] * row for _ in range(column)]
x, y, direction = map(int, input().split())
game_map = []
for i in range(column):
    game_map.append(list(map(int, input().split())))
move=[(-1,0), (0,1), (1,0),(0,-1)]
directions = [0, 1, 2, 3]
result = 0
fail = 0

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

while True:

    # 네 방향 모두 가본 칸이거나 바다로 되어 있는 칸인 경우
    if fail == 4:
        dx = x - move[direction][0]
        dy = y - move[direction][1]
        if (game_map[dx][dy] == 0 and dx >= 0 and dx <= row and dy >= 0 and dy <= column):
            x, y = dx, dy
            fail = 0
        else:
            break

    # 왼쪽방향으로 회전
    turn_left()
    dx = x - move[direction][0]
    dy = y + move[direction][1]
    
    # 전진 가능
    if (game_map[dx][dy] == 0 and d[dx][dy] == 0 and dx >= 0 and dx <= row and dy >= 0 and dy <= column):
        d[dx][dy] = 1
        x, y = dx, dy
        result += 1
        fail = 0
        continue
    
    # 전진 불가능
    else:
        fail += 1
        continue

print(result)