increases = 0
previous = 0

# Part One
""" with open('input.txt') as file:
    while (line := file.readline().rstrip()):
      teller += 1
      if int(line) > previous:
        if previous != 0: increases +=1
      previous = int(line)
print(str(increases))
"""

# Part Two
with open('input.txt') as file:
  lines = file.readlines()
  lines = [line.rstrip() for line in lines]

while len(lines) > 3:
  firstSum = sum([int(lines[i]) for i in [0, 1, 2]])
  if firstSum > previous:
    if previous != 0:
      increases += 1
  secondSum = sum([int(lines[i]) for i in [1, 2, 3]])
  if secondSum > firstSum:
    increases += 1
  previous = secondSum
  lines.pop(0)
if sum([int(lines[i]) for i in [1, 2, 3]]) > previous: increases += 1

print(str(increases))
