def star1():
  with open('input.txt', 'r') as file:
    sum = 0
    for line in file:
      digits = ''
      for char in line:
        if char.isdigit(): digits += char
      sum += (int(digits[0] + digits[-1]))
    return sum

def star2():
  with open('input.txt', 'r') as file:
    sum = 0
    for line in file:
      line = line.replace('one', 'one1one')
      line = line.replace('two', 'two2two')
      line = line.replace('three', 'three3three')
      line = line.replace('four', 'four4four')
      line = line.replace('five', 'five5five')
      line = line.replace('six', 'six6six')
      line = line.replace('seven', 'seven7seven')
      line = line.replace('eight', 'eight8eight')
      line = line.replace('nine', 'nine9nine')
      digits = ''
      for char in line:
        if char.isdigit(): digits += char
      sum += (int(digits[0] + digits[-1]))
    return sum

print(
    f"""Day 1:
    first solution: {star1()}
    second solution: {star2()}"""
 )