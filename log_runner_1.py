def solveEquation1(equation):
    # 4:13 10/24/20
    def get_coefs(s):
        x, n, sgn = 0, 0, 1
        for t in re.split(r'(\+|-)', s):
            if t in ['+', '-']:
                sgn = (-1) ** (t == '-')
            elif t.isdigit():
                n += sgn * int(t)
            elif t and t[-1] == 'x':
                x += sgn * int(t[:-1] or '1')
        return (x, n)

    l, r = equation.split('=')
    l, r = get_coefs(l), get_coefs(r)
    x, n = l[0] - r[0], r[1] - l[1]
    if x == 0:
        return 'Infinite solutions' if n == 0 else 'No solution'
    return 'x={}'.format(n // x)

def solveEquation(equation):
    # 4:13 10/24/20
    def helper(s):
        coef, constant = 0, 0
        s += ' '
        i = 0
        for j, c in enumerate(s):
            if j != i and c in '+- ':
                expr = s[i:j]
                i = j
                if expr[-1] == 'x':
                    expr = expr[:-1]
                    if expr in '+-':
                        expr += '1'
                    coef += int(expr)
                else:
                    constant += int(expr)

        return coef, constant

    def helper_1(s):
        sign, n = 1, len(s)
        # i, coef, const stand for current index, and accumulative 'x' coefficient and constant
        i = coef = const = 0
        while i < n:
            if s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i].isdigit():
                j = i
                while j < n and s[j].isdigit():
                    j += 1
                tmp = int(s[i:j])
                if j == n or s[j] != 'x':
                    const += tmp * sign
                else:
                    coef += tmp * sign
                    j += 1
                i = j
                continue
            else:  # 'x'
                coef += sign
            i += 1
        return coef, const

    l, r = equation.split('=')
    l, r = get_coefs(l), get_coefs(r)
    x, n = l[0] - r[0], r[1] - l[1]
    if x == 0:
        return 'Infinite solutions' if n == 0 else 'No solution'
    return 'x={}'.format(n // x)



