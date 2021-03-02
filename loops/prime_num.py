n = int(input())
isPrime = True

if n < 2:
    print("no")
    quit()

for x in range(2, n):
    if n % x == 0:
        isPrime = False
        break

print("yes") if isPrime else print("no")
