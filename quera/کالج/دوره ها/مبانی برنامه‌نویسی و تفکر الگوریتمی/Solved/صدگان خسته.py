a = input()
b = input()
if 99 < int(a) and int(b) < 1000:
    x = a[::-1]
    y = b[::-1]
    if x > y:
        print(f'{b} < {a}')
    elif x < y:
        print(f'{a} < {b}')
    else:
        print(f'{a} = {b}')
