n = int(input())

count = 1
prev_num = n

while not n == 1:
    if prev_num % 2 == 0:
        n = prev_num / 2
    else:
        n = 3 * prev_num + 1

    prev_num = n
    count += 1

print(count)
