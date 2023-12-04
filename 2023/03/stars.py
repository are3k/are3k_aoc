import numpy as np
import re

def star_1(engine_matrix):
  sum = 0
  parts = list()
  for i in range(engine_matrix.shape[0]):
    numbers_in_row = re.findall('\d+', engine_matrix[i,])
    #print('row:',engine_matrix[i])
    #print('numbers:',numbers_in_row)
    for n in numbers_in_row:
      found = False
      number = re.search(n, engine_matrix[i])
      position = number.span()
      for x in range(position[0]-1, position[1]+1):
        for y in range(i-1, i+2):
          if x >= 0 and y >= 0 and x < engine_matrix.shape[0] and y < engine_matrix.shape[0]:
            # print('[x,y]:', x+1, y+1, 'symbol:', engine_matrix[y,][x])
            if not found and engine_matrix[y,][x] != "." and not engine_matrix[y][x].isdigit():
              parts.append(number.group())
              # print('Adding number', number.group(), 'to', sum ,' because of:', engine_matrix[y,][x])
              sum += int(number.group())
              found = True
  print(parts)
  return sum

def star_2(engine_matrix):
  return "working..."

with open('input.txt') as file:
  engine_matrix = np.loadtxt(file, dtype=str, comments=None,)

print(
    f"""Day 3:
    first solution: {star_1(engine_matrix)}
    second solution: {star_2(engine_matrix)}"""
)