import re

def calc_mul(line):
    sum = 0
    all_mul = re.findall("mul\(\d{1,3},\d{1,3}\)", line )
    #print(all_mul)
    for mul in all_mul:
        mul = mul[4:]
        mul = mul[:-1]
        (x,y) = list(map(int, mul.split(',')))
        sum += x * y
    return sum    

def star_one(input):
    sum = 0
    #print(input)
    for line in input:
        #print(input)
        all_mul = re.findall("mul\(\d{1,3},\d{1,3}\)", line )
        #print(all_mul)
        for mul in all_mul:
            mul = mul[4:]
            mul = mul[:-1]
            (x,y) = list(map(int, mul.split(',')))
            sum += x * y
    return sum    

def star_two(input):
    sum = 0
    for line in input:
        parts = line.split("don't()")
        #print(len(parts))
        print('Skal beregne på: ', parts[0])
        sum += (calc_mul(parts[0]))
        for big_parts in parts[1:]:
            do_parts = big_parts.split("do()", 1)
            if len(do_parts) > 1:
             print('do_parts: ', do_parts[1])
             sum += calc_mul(do_parts[1])
    return sum

file = open('input.txt', 'r')
input = file.readlines()


#print("star one:", star_one(input))
#168539636
print("star two:", star_two(input))
#126184080 too high
#102631226 too high
    
