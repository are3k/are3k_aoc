import time,sys,re,math
tstart=time.time()

inf = sys.argv[1] if len(sys.argv) > 1 else 'input/08_input.txt'
print('Haunted Wasteland - navigate the network')
with open(inf) as fi:
    instr,way = fi.read().strip().split('\n\n')
    ways = [w for w in way.split('\n')]
    W = dict()
    for w in ways:
        s,r,l = re.findall(r'(\w+)',w)
        W[s]=(r,l)
    #way = {s:(r,l) for s,r,l in re.findall(r'(\w+)',w)} 

def step(p,m):
    if m == 'R':
        return W[p][1]
    else:
        return W[p][0]

def length(p,part):
    steps = 0
    i = 0
    while (p != 'ZZZ' and part == 1) or (p[2]!= 'Z' and part == 2):
        steps += 1
        p = step(p,instr[i])
        i = i+1 if i+1 < len(instr) else 0
    return steps #print(p)

#p1:
print('part1',length('AAA',1))

#p2
ps = [p for p in W.keys() if 'A' == p[2]]
S = []
for p in ps:
    S.append(length(p,2))
lcm= 1
for i in S:
    lcm = lcm*i//math.gcd(lcm, i)
print('part2', lcm)

tend=time.time()
print(round(tend-tstart,5))

