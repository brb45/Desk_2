import re

equation = "x+5-3+x=6+x-2"


def get_coefs(s):
    x, n, sgn = 0, 0, 1
    # print(re.split())
    for t in re.split(r'(\+|-)', s):
        # print(f"type(t) is {type(t)}")
        if t in ['+', '-']:
            sgn = (-1) ** (t == '-')
        elif t.isdigit():
            n += sgn * int(t)
        elif t and t[-1] == 'x':
            # print(t[-1])
            x += sgn * int(t[:-1] or '1')
    return (x, n)

s,t = equation.split("=")

print(re.split(r'\+|-',s))
print(re.split(r'\+|-', t))

print(re.split(r'(\+|-)',s))
print(re.split(r'(\+|-)', t))
get_coefs(s)
