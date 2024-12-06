def star_one(input):
    safe = 0
    for line in input:
        seq = list(map(int, line.split(' ')))
        if (all(seq[i] < seq[i + 1] for i in range(len(seq) - 1)) or all(seq[i] 
            > seq[i + 1] for i in range(len(seq) - 1))):
            diff_list = []
            for x, y in zip(seq[0::], seq[1::]):
                diff_list.append(abs(y-x))
            if max(diff_list) < 4:
                safe += 1
    return safe


def star_two(input):
    safe = 0
    for line in input:
        seq = list(map(int, line.split(' ')))
        orig_seq = seq.copy()
        for i in range(0, len(seq)+1):
            if i > 0:
                print(' i skal være mindre enn ', len(seq), ' nå er i', i)
                print('  seq: ', orig_seq)
                seq = orig_seq.copy()
                seq.pop(i-1)
                print('  seq: ', seq)
                #print('i:' , i, 'seq: ', seq)
            if (all(seq[i] < seq[i + 1] for i in range(len(seq) - 1)) or all(seq[i] 
                > seq[i + 1] for i in range(len(seq) - 1))):
                diff_list = []
                for x, y in zip(seq[0::], seq[1::]):
                    diff_list.append(abs(y-x))
                if max(diff_list) < 4:
                    safe += 1
                    print('legger til')
                    break
    return safe


file = open('input', 'r')
input = file.readlines()

print("star one:", star_one(input))
print("star two:", star_two(input))
    
