n = input()
if n[0] == "0":
    for digit in str(n):
        N = int(digit)
        print(f"{digit}: {N*digit}")
else:
    n= int(n)
    if n < 0:
        n = -n

    if n == 0:
        print("0: ")
    else:
        i = 1
        while i <= n:
            i = i*10
        if i == n:
            pass
        else:
            i = i//10
        # print(i)

        j = i
        while j > 0:
            digit = n // j
            n = n - (j*digit)
            j = j//10
            # print(digit)
            digit_counter = 0
            print(str(digit)+": ", end="")
            while digit_counter < digit:
                print(digit, end="")
                digit_counter += 1
            print()
