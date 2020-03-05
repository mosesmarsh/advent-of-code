def load_data(fpath, sep=None):
    return [int(x) for x in
            open(fpath).read().split(sep)]


def day1_1(fpath):
    with open(fpath) as f:
        return sum(int(num)//3 - 2
                   for num in f)

def day1_2(fpath):
    with open(fpath) as f:
        tot=0
        for line in f:
            num = int(line)
            cost = num//3 - 2
            while cost >= 0:
                tot += cost
                cost = cost//3 - 2
    return tot

def day2_1(fpath):
    program = [int(x) for x in
                open(fpath).read().split(',')]
    
