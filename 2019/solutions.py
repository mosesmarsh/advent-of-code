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

from collections import defaultdict

def segment(point, step):
    '''0: xaxis, 1: yaxis'''
    axis = (step[0] in 'UD')        
    sign = (step[0] in 'UR')*2 - 1 
    position = point[not axis]
    start = point[axis] 
    end = start + sign*int(step[1:]) 
    return axis, position, start, end

def points(point, step):
    '''0: xaxis, 1: yaxis'''
    axis = (step[0] in 'UD')        
    sign = (step[0] in 'UR')*2 - 1
    delta = sign*int(step[1:]) 
    p = point.copy()
    pts = []
    for n in range(sign, delta + sign, sign):
        p[axis] += sign
        pts.append(tuple(p))
    return pts

def path_to_segments(path):
    '''segs[0]: horizontal segments as y: {(x1,x2):plen,...}
       segs[1]: vertical segments as x:{(y1,y2):plen,...}
    '''
    point = [0,0]
    segs = [defaultdict(dict), defaultdict(dict)]
    path_length=0
    for step in path:
        ax, pos, start, end = segment(point, step)
        path_length += abs(end - start)
        if (start, end) not in segs[ax][pos]:
            segs[ax][pos][(start, end)] = path_length
        point[ax] = end
    return segs

def path_to_points(path):
    point = [0,0]
    visited = {}
    path_length=0
    for step in path:
        for pt in points(point, step):
            path_length += 1
            if pt not in visited:
                visited[pt] = path_length
        point = list(pt)
    return visited

def day3_1(paths):
    segs = path_to_segments(paths[0])
    point = [0,0]
    min_dist = 1e27
    for step in paths[1]:
        ax, pos, start, end = segment(point, step)
        rev = ((end - start) > 0)*2 - 1
        for cross_pos in range(start, end+rev, rev):
            cross_segs = segs[not ax][cross_pos]
            for c_start, c_end in cross_segs:
                if ((pos > min((c_start, c_end))) and
                    (pos < max((c_start, c_end)))):
                    dist = abs(pos)+abs(cross_pos)
                    if dist < min_dist:
                        min_dist = dist
        point[ax]=end
    return min_dist

def day3_1_pts(paths):
    visited_1 = path_to_points(paths[0])
    visited_2 = path_to_points(paths[1])
    min_dist = 1e24
    for k in visited_1:
        if k in visited_2:
            dist = abs(k[0]) + abs(k[1])
            if dist < min_dist:
                min_dist = dist
    return min_dist

def day3_2(paths):
    visited_1 = path_to_points(paths[0])
    visited_2 = path_to_points(paths[1])
    min_dist = 1e24
    for k,v in visited_1.items():
        if k in visited_2:
            dist = v + visited_2[k]
            if dist < min_dist:
                min_dist = dist
    return min_dist
