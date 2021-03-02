n = 0
s = '+'
m = 0
 
for x in input().split():
    if x in ('+', '-', '/', '*', '='):
        s = x
    else:
        m = int(x)

        if s == '+':
            n += m
        elif s == '-':
            n -= m
        elif s == '*':
            n = n * m
        elif s == '/':
            n /= m
        elif s == '=':
            break

print(n)
