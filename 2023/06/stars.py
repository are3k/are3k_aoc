from math import prod
from re import findall, search


def star_1(input):
  result = []
  times = list(map(int, findall('\d+', input[0])))
  distances = list(map(int, findall('\d+', input[1])))
  for i in range(len(times)):
    local_result = 0
    for time in range(1, times[i]):
      distance = time * (times[i] - time)
      if distance >= distances[i]:
        local_result += 1
    result.append(local_result)
  return prod(result)

def star_2(input):
  result = 0
  time = int(''.join(list(findall('\d+', input[0]))))
  distance = int(''.join(list(findall('\d+', input[1]))))
  #find first and list time qualifying
  for i in range(1, time):
    if i * (time - i) >= distance:
      first = i
      break
  for i in range(time, 1, -1):
    if i * (time - i) >= distance:
      last = i
      break
  # Result is difference between last and first
  result = (last - first) + 1
  return result


input = list(open('input.txt'))
print(
    f"""Day 6:
    first solution: {star_1(input)}
    second solution: {star_2(input)}"""
)