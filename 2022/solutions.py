def parse_line(line, sep=',', 
               dtype=str,
               one_field=False):
    if one_field:
        return dtype(line)
    return [dtype(x) for x in line.split(sep)]


def load_data(fpath, one_line=False,
                one_field=False,
                sep=',', dtype=int):
    kwargs = {'sep':sep,
              'one_field':one_field,
              'dtype':dtype}
    with open(fpath) as f:
        raw = f.read().strip()
    if one_line:
        return parse_line(raw, **kwargs) 
    return [parse_line(l, **kwargs) for l in raw.split()] 

def day1(cals):
    elves = cals.strip().split('\n\n')
    elf_cals = [sum(int(n) for n in elf.split('\n')) for elf in elves]
    max_cal = max(elf_cals)
    top_3_sum = sum(sorted(elf_cals)[-3:])
    return max_cal, top_3_sum

def day2(strat):
    vals = {'A':'1', 'B':'2', 'C':'3', 'X':'1', 'Y':'2', 'Z':'3'}
    rounds = strat.translate(str.maketrans(vals)).strip().split('\n')
    rounds = [(int(r[0]), int(r[-1])) for r in rounds]
    score_map = [3, 6, 0]  # {0:3, 1:6, -1:0, 2:0, -2:6}
    scores_1 = [r[1] + score_map[r[1]-r[0]] for r in rounds]
    # score_map_2 = {1:0, 2:3, 3:6} --> (r-1)*3
    # strat_map_2 = {1:-1, 2:0, 3:1} --> (r-2)
    scores_2 = [(r[0] + r[1] - 2 - 1)%3 + 1 + (r[1]-1)*3 for r in rounds]
    return (sum(scores_1), sum(scores_2))

def day3(sacks):
    sacks = sacks.strip().split('\n')
    alph = 'abcdefghijklmnopqrstuvwxyz'
    vals = {x:v for x,v in zip(alph+alph.upper(), range(1,53))}
    total = 0
    for sack in sacks:
        n = len(sack)
        total += vals[set(sack[:n//2]).intersection(sack[n//2:]).pop()]
    
    total_2 = 0
    for i in range(0, len(sacks), 3):
        total_2 += vals[set(sacks[i]).intersection(sacks[i+1]).intersection(sacks[i+2]).pop()]
    return total, total_2

def day4(sections):
    return


def day5(raw):
    initial, moves = raw.split('\n\n')
    stacks = list(zip(*(reversed(initial.split('\n')))))
    stacks = [list(c for c in stacks[i][1:] if (c != ' ')) for i in range(1, len(stacks), 4)]
    moves = moves.strip().split('\n')
    for move in moves:
        _, n, _, source, _, target = move.split()
        n = int(n)
        source, target = int(source) - 1, int(target) -1
        
        ### part 1 logic
        #for i in range(n):
        #    crate = stacks[source].pop()
        #    stacks[target].append(crate)

        ### part 2 logic
        stacks[target].extend(stacks[source][-n:])
        for i in range(n):
            stacks[source].pop()

    return ''.join(s[-1] for s in stacks)



########

for i, fn in zip(range(1,26), (day1, day2, day3, day4)):
    print(f"day {i:02}: ", fn(open(f'day{i}.txt','r').read()))




