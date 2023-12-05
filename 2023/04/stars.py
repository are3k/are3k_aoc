# Stolen from the subreddit
from collections import defaultdict
from re import findall, search

def star_1(cards):
  sum = 0
  for c, card in enumerate(cards):
    points = 0
    winning = set(findall('\d+', card.split(": ")[1].split(" | ")[0]))
    have = set(findall('\d+', card.split(": ")[1].split(" | ")[1]))
    for i in range(len(have & winning)):
      if i == 0: points = 1
      if i > 0: points += points
    sum += points
  return sum

def star_2(cards):
  sum = 0
  card_copies = {}
  for c, card in enumerate(cards):
    card_number = search('\d+', card.split(": ")[0])
    matches = (len(set(findall('\d+', card.split(": ")[1].split(" | ")[1])).\
                   intersection(findall('\d+', \
                    card.split(": ")[1].split(" | ")[0]))))
    card_copies[int(card_number.group())] = [matches, int(1)]
  for card in card_copies:
    for matches in range(1, card_copies[card][0] + 1):
      card_copies[card + matches][1] += card_copies[card][1]
  for card in card_copies:
    sum += card_copies[card][1]
  return sum

cards = list(open('input.txt'))
print(
    f"""Day 4:
    first solution: {star_1(cards)}
    second solution: {star_2(cards)}"""
)