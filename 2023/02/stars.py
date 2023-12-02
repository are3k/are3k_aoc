import re

def check_max(list, max):
  for n in list:
    if int(re.search('\d+', n).group()) > max:
      return False
  return True

def star1():
  # sum all game numbers that has any color number above 12
  with open('input.txt', 'r') as file:
    sum = 0
    for line in file:
      possible = True
      game_number = int(re.search('\d+', line).group())
      game_numbers_red = re.findall('\d+ red', line)
      possible = check_max(game_numbers_red, 12)
      if possible:
        game_numbers_green = re.findall('\d+ green', line)
        possible = check_max(game_numbers_green, 13)
      if possible:
        game_numbers_blue = re.findall('\d+ blue', line)
        possible = check_max(game_numbers_blue, 14)
      if possible: sum += game_number
  return sum
      

def star2():
  with open('input.txt', 'r') as file:
    sum = 0
    for line in file:
      game_number = int(re.search('\d+', line).group())
      game_numbers_red = re.findall('\d+ red', line)
      max_red = max(list(map(int, (re.findall('\d+', ' '.join(game_numbers_red))))))
      game_numbers_green = re.findall('\d+ green', line)
      max_green = max(list(map(int, (re.findall('\d+', ' '.join(game_numbers_green))))))
      game_numbers_blue = re.findall('\d+ blue', line)
      max_blue = max(list(map(int, (re.findall('\d+', ' '.join(game_numbers_blue))))))
      sum += max_red * max_green * max_blue
    return sum

print(
    f"""Day 2:
    first solution: {star1()}
    second solution: {star2()}"""
 )