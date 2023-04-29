x, y = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
if x == x2:
    if y1 == y2:
        print(x1, y)
    elif y == y1:
        print(x1, y2)
elif x == x1:
    print(x2, y1)
