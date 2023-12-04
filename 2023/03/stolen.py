# Stolen from the subreddit
from collections import defaultdict
from math import prod
from re import finditer

parts = defaultdict(list)
board = list(open('input.txt'))
# find position of all valid symbols
chars = {(r, c) for r in range(140)
                for c in range(140)
                if board[r][c] not in '01234566789.'}

# loop over all lines in board, r = row number, row = the full string of the row
for r, row in enumerate(board):
    # find all numbers in the row
    for m in finditer(r'\d+', row):
        # find all positions where a symbol can be found to indicate that the
        # number indeed is a part number
        # This presupposes that no number has more than one symbol adjacent
        nexts = {(r+s, c+d) for s in (-1, 0, 1) 
                            for d in (-1, 0, 1)
                            for c in range(*m.span())}
        # add integers next to a symbol position to the parts dict, where
        # symbol position is key, and part numbers adjacent is values
        for c in nexts & chars:
            parts[c].append(int(m[0]))

print(sum(sum(p)  for p in parts.values()),
      sum(prod(p) for p in parts.values() if len(p)==2))