from collections import defaultdict
from datetime import datetime
from re import findall, search

def create_maps(input):
  maps=defaultdict(list)
  for line in input:
    if line.strip():
      if "seeds:" in line:
        maps['seeds'].append(list(map(int, findall('\d+', line))))
      elif "map:" in line:
        map_title = line.split(" map:")[0]
      else:
        maps[map_title].append(list(map(int, findall('\d+', line))))
  return maps

def find_in_map(map, value):
  for n in map:
    if value >= n[1] and value < n[1] + n[2]:
      return n[0]+(value - n[1])
  return value


def star_1(input):
  locations = []
  maps = create_maps(input)
  for seeds in maps['seeds']:
    for seed in seeds:
      soil = find_in_map(maps['seed-to-soil'], seed)
      fertilizer = find_in_map(maps['soil-to-fertilizer'], soil)
      water = find_in_map(maps['fertilizer-to-water'], fertilizer)
      light = find_in_map(maps['water-to-light'], water)
      temperature = find_in_map(maps['light-to-temperature'], light)
      humidity = find_in_map(maps['temperature-to-humidity'], temperature)
      location = find_in_map(maps['humidity-to-location'], humidity)
      locations.append(location)
  return min(locations)

def star_2(input):
  # Brute force, but works...
  low_loc_num = 111525792406
  maps = create_maps(input)
  for seeds in maps['seeds']:
    for i in range(0, len(seeds), 2):
      for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
        soil = find_in_map(maps['seed-to-soil'], seed)
        fertilizer = find_in_map(maps['soil-to-fertilizer'], soil)
        water = find_in_map(maps['fertilizer-to-water'], fertilizer)
        light = find_in_map(maps['water-to-light'], water)
        temperature = find_in_map(maps['light-to-temperature'], light)
        humidity = find_in_map(maps['temperature-to-humidity'], temperature)
        location = find_in_map(maps['humidity-to-location'], humidity)
        if location < low_loc_num: low_loc_num = location
  return low_loc_num

input = list(open('input.txt'))
print(
    f"""Day 5:
    first solution: {star_1(input)}
    second solution: {star_2(input)}"""
)