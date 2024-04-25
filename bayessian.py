exam = [0.6, 0.4]
iq = [0.7, 0.3]
admission = [[0.6, 0.4], [0.9, 0.1]]
marks = [[0.6, 0.4], [0.9, 0.1], [0.5, 0.5], [0.8, 0.2]]

def p(a, m, e, i):
    return p1(a, m) * p2(m, i, e) * p3(e) * p4(i)

def p1(a, m):
    return admission[a][m]

def p3(e):
    return exam[e]

def p4(i):
    return iq[i]

def p2(m, i, e):
    if m == 0 and e == 0 and i == 0:
        return marks[0][0]
    elif m == 1 and e == 0 and i == 0:
        return marks[0][1]
    elif m == 0 and e == 1 and i == 0:
        return marks[1][0]
    elif m == 1 and e == 1 and i == 0:
        return marks[1][1]
    elif m == 0 and e == 0 and i == 1:
        return marks[2][0]
    elif m == 1 and e == 0 and i == 1:
        return marks[2][1]
    elif m == 0 and e == 1 and i == 1:
        return marks[3][0]
    elif m == 1 and e == 1 and i == 1:
        return marks[3][1]

if __name__ == "__main__":
    print("(Enter 0 in case of false and 1 in case of true)")
    a = int(input())
    m = int(input())
    e = int(input())
    i = int(input())
    if a not in [0, 1] or m not in [0, 1] or e not in [0, 1] or i not in [0, 1]:
        print("ENTER 0 AND 1 ONLY")
    else:
        print("The probability for the given case is:", p(a, m, e, i))
