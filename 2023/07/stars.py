from math import prod
from collections import Counter
from collections import defaultdict
from re import findall, search


def star_1(input):
  result = 0
  hands = defaultdict(list)
  for item in input:
    hands[item.split()[0].strip()] = [int(item.split()[1].strip())]
  high_card = {}
  one_pair = {}
  two_pair = {}
  three = {}
  full_house = {}
  four = {}
  five = {}
  rank = 1
  for (hand, bet) in hands.items():
    card_count = Counter(hand)
    # print(card_count.values())
    if len(card_count.values()) == 5:
      high_card[hand] = bet
    elif len(card_count.values()) == 4:
      one_pair[hand] = bet
    elif len(card_count.values()) == 3:
      if max(card_count.values()) == 2:
        two_pair[hand] = bet
      else:
        three[hand] = bet
    elif len(card_count.values()) == 2:
      if max(card_count.values()) == 3:
        full_house[hand] = bet
      else:
        four[hand] = bet
    else:
      five[hand] = bet
  card_values = "AKQJT98765432"
  sorted_high_cards = sorted(high_card.keys(), reverse=True, \
                        key=lambda word: [card_values.index(c) for c in word])
  sorted_one_pair = sorted(one_pair.keys(), reverse=True, \
                        key=lambda word: [card_values.index(c) for c in word])
  sorted_two_pair = sorted(two_pair.keys(), reverse=True, \
                        key=lambda word: [card_values.index(c) for c in word])
  sorted_three = sorted(three.keys(), reverse=True, \
                        key=lambda word: [card_values.index(c) for c in word])
  sorted_full_house = sorted(full_house.keys(), reverse=True, \
                        key=lambda word: [card_values.index(c) for c in word])
  sorted_four = sorted(four.keys(), reverse=True, \
                        key=lambda word: [card_values.index(c) for c in word])
  sorted_five = sorted(five.keys(), reverse=True, \
                        key=lambda word: [card_values.index(c) for c in word])
  for hand in sorted_high_cards:
    high_card.setdefault(hand, []).append(rank)
    rank += 1
  for hand in sorted_one_pair:
    one_pair.setdefault(hand, []).append(rank)
    rank += 1
  for hand in sorted_two_pair:
    two_pair.setdefault(hand, []).append(rank)
    rank += 1
  for hand in sorted_three:
    three.setdefault(hand, []).append(rank)
    rank += 1
  for hand in sorted_full_house:
    full_house.setdefault(hand, []).append(rank)
    rank += 1
  for hand in sorted_four:
    four.setdefault(hand, []).append(rank)
    rank += 1
  for hand in sorted_five:
    five.setdefault(hand, []).append(rank)
    rank += 1
  for hand in five:
    result += prod(hands[hand])
  for hand in four:
    result += prod(hands[hand])
  for hand in full_house:
    result += prod(hands[hand])
  for hand in three:
    result += prod(hands[hand])
  for hand in two_pair:
    result += prod(hands[hand])
  for hand in one_pair:
    result += prod(hands[hand])
  for hand in high_card:
    result += prod(hands[hand])
  return result

def joker(hand, card_count):
  if len(card_count.values()) == 5:
    return 'one_pair'
  if len(card_count.values()) == 4:
    return 'three'
  if len(card_count.values()) == 3:
    if max(card_count.values()) == 3 or card_count['J'] == 2:
      return 'four'
    else:
      return 'full_house'
  if len(card_count.values()) < 3:
    return 'five'

def star_2(input):
  result = 0
  hands = defaultdict(list)
  for item in input:
    hands[item.split()[0].strip()] = [int(item.split()[1].strip())]
  high_card = {}
  one_pair = {}
  two_pair = {}
  three = {}
  full_house = {}
  four = {}
  five = {}
  rank = 1
  for (hand, bet) in hands.items():
    card_count = Counter(hand)
    if 'J' in hand:
      joker_value = joker(hand, card_count)
      match joker_value:
        case 'one_pair':
          one_pair[hand] = bet
        case 'three':
          three[hand] = bet
        case 'full_house':
          full_house[hand] = bet
        case 'four':
          four[hand] = bet
        case 'five':
          five[hand] = bet
    elif len(card_count.values()) == 5:
      high_card[hand] = bet
    elif len(card_count.values()) == 4:
      one_pair[hand] = bet
    elif len(card_count.values()) == 3:
      if max(card_count.values()) == 2:
        two_pair[hand] = bet
      else:
        three[hand] = bet
    elif len(card_count.values()) == 2:
      if max(card_count.values()) == 3:
        full_house[hand] = bet
      else:
        four[hand] = bet
    else:
      five[hand] = bet
  card_values = "AKQT98765432J"
  sorted_high_cards = sorted(high_card.keys(), reverse=True, \
                        key=lambda word: [card_values.index(c) for c in word])
  sorted_one_pair = sorted(one_pair.keys(), reverse=True, \
                        key=lambda word: [card_values.index(c) for c in word])
  sorted_two_pair = sorted(two_pair.keys(), reverse=True, \
                        key=lambda word: [card_values.index(c) for c in word])
  sorted_three = sorted(three.keys(), reverse=True, \
                        key=lambda word: [card_values.index(c) for c in word])
  sorted_full_house = sorted(full_house.keys(), reverse=True, \
                        key=lambda word: [card_values.index(c) for c in word])
  sorted_four = sorted(four.keys(), reverse=True, \
                        key=lambda word: [card_values.index(c) for c in word])
  sorted_five = sorted(five.keys(), reverse=True, \
                        key=lambda word: [card_values.index(c) for c in word])
  for hand in sorted_high_cards:
    high_card.setdefault(hand, []).append(rank)
    rank += 1
  for hand in sorted_one_pair:
    one_pair.setdefault(hand, []).append(rank)
    rank += 1
  for hand in sorted_two_pair:
    two_pair.setdefault(hand, []).append(rank)
    rank += 1
  for hand in sorted_three:
    three.setdefault(hand, []).append(rank)
    rank += 1
  for hand in sorted_full_house:
    full_house.setdefault(hand, []).append(rank)
    rank += 1
  for hand in sorted_four:
    four.setdefault(hand, []).append(rank)
    rank += 1
  for hand in sorted_five:
    five.setdefault(hand, []).append(rank)
    rank += 1
  for hand in five:
    result += prod(hands[hand])
  for hand in four:
    result += prod(hands[hand])
  for hand in full_house:
    result += prod(hands[hand])
  for hand in three:
    result += prod(hands[hand])
  for hand in two_pair:
    result += prod(hands[hand])
  for hand in one_pair:
    result += prod(hands[hand])
  for hand in high_card:
    result += prod(hands[hand])
  return result

input = list(open('input.txt'))

print(
    f"""Day 7:
    first solution: {star_1(input)}
    second solution: {star_2(input)}"""
)