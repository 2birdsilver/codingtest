def solution(dots):
  answer = 0
  for i in range(1, len(dots)):
    inclination_1 = 0
    inclination_2 = 0

    copy_list = dots.copy()
    counter_dot = copy_list.pop(i)
    standard_dot = copy_list.pop(0)

    if standard_dot[0] >= counter_dot[0]:
      inclination_1 = counter_dot[
          1] - standard_dot[1] / counter_dot[0] - standard_dot[0]
      print("inclination_1={}".format(inclination_1))
    else:
      inclination_1 = counter_dot[
          0] - standard_dot[0] / counter_dot[1] - standard_dot[1]
      print("inclination_1={}".format(inclination_1))

    if copy_list[0][0] >= copy_list[1][0]:
      inclination_2 = copy_list[
          0][1] - copy_list[1][1] / copy_list[0][0] - copy_list[1][0]
      print("inclination_2={}".format(inclination_2))
    else:
      inclination_2 = copy_list[
          0][0] - copy_list[1][0] / copy_list[0][1] - copy_list[1][1]
      print("inclination_2={}".format(inclination_2))

    if inclination_1 == inclination_2:
      answer = 1

  return answer


print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))