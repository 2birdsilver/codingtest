n = int(input())
warehouses = list(map(int, input().split()))
# print(warehouses)

def antWarrior():
    sum = 0
    while(len(warehouses) != 0):
        index = warehouses.index(max(warehouses))
        # print(max(warehouses))
        sum += warehouses[index]
        # print(sum)

        if (index == 0):
            warehouses.pop(0)
            warehouses.pop(0)
        elif(index == len(warehouses) - 1):
            warehouses.pop(len(warehouses) - 1)
            warehouses.pop(len(warehouses) - 1)
        else :
            warehouses.pop(index - 1)
            warehouses.pop(index - 1)
            warehouses.pop(index - 1)
    print(sum)

antWarrior()
