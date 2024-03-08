n = int(input())
notThreeHourCount = 0
notThreeMinuteCount = 0
notThreeSecondCount = 0
notThreeCount = 0
def isNotInThree(number):
    first = number // 10
    second = number % 10

    if first != 3 and second != 3:
        return True

for i in range(60):
    if isNotInThree(i) == True:
      notThreeSecondCount += 1

notThreeMinuteCount = notThreeSecondCount

for j in range(n+1):
    if isNotInThree(j):
        notThreeHourCount += 1

notThreeCount = (notThreeHourCount * notThreeMinuteCount * notThreeSecondCount)
result = (n+1) * 60 * 60 - notThreeCount
print(result)
