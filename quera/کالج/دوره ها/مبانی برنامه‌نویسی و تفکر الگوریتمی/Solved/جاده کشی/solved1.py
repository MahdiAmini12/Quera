n = int(input())
row = int(n  / 2) 
col = int((n % 2) + row)
print(int((row + 1) * (col + 1)))
