def load_data(fpath, sep=None):
    return [int(x) for x in
            open(fpath).read().split(sep)]


def day1_1(masses):
    return sum(int(mass)//3 - 2
               for mass in masses)

def day1_2(masses):
    tot=0
    for mass in masses:
        cost = mass//3 - 2
        while cost >= 0:
            tot += cost
            cost = cost//3 - 2
    return tot

def day2_1(prog):
    ops = {1: int.__add__,
           2: int.__mul__}
    for i in range(0,len(prog),4):
        op_id, x_ind, y_ind, idx = prog[i:i+4]
        if op_id == 99:
            return prog
        x, y = prog[x_ind], prog[y_ind]
        prog[idx] = ops[op_id](x,y)
    return "never got to 99"

def run_program(prog):
    ops = {1: int.__add__,
           2: int.__mul__}
    for i in range(0,len(prog),4):
        op_id, x_ind, y_ind, idx = prog[i:i+4]
        if op_id == 99:
            return prog
        x, y = prog[x_ind], prog[y_ind]
        prog[idx] = ops[op_id](x,y)
    return "never got to 99"

def day2_2(prog, target):
    out = 0
    for a in range(100):
        for b in range(100):
            p = prog.copy()
            p[1:3] = a, b
            out = run_program(p)[0]
            if out==target:
                return (100*a) + b
    return 'never got there'
