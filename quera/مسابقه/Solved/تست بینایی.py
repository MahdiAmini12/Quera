_ = input()

a = input()
b = input()
counter = 0
for index in range(len(a)):
    if a[index] != b[index]:
        counter+=1
print(counter)
