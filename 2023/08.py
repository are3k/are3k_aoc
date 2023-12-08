from math import prod
from re import findall, search

def find_coordinate(coordinates, start):
  return [coordinate for coordinate in coordinates if start in coordinate[0]]

def star_1(commands, coordinates):
  result = 0
  funnet = False
  steps = 0
  location = find_coordinate(coordinates, 'AAA')
  print(location, location[0])
  print('antall kommandoer:', len(commands))
  while location[0][0] != 'ZZZ':# and steps < 50:
    for command in commands:
      print('utgangspunkt:', command, location, steps)
      steps += 1
      if command == 'L':
        location = find_coordinate(coordinates, location[0][1])
      elif command == 'R':
        location = find_coordinate(coordinates, location[0][2])
      print('etter steg:', command, location, steps)
      if location[0][0] == 'ZZZ':
        print('vi er framme:', location)
        funnet = True
        break
  return steps-1


def star_2(input):
  result = 0
  
  # for command in commands:
  #   print(command)
  
  return result


input = list(open('input/08_input.txt'))
commands = input[0]
coordinates = []
for i in range(2, len(input)):
  coordinates.append(findall('\w+', input[i]))
print(
    f"""Day 8:
    first solution: {star_1(commands, coordinates)}
    second solution: {star_2(input)}"""
)