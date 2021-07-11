import math


def to_digits(n):
    if n < 0:
        n *= -1
    return [int(x) for x in str(n)]


def sum_of_digits(n):
    return sum(to_digits(n))


def fact_digits(n):
    return sum(math.factorial(x) for x in to_digits(n))


# return str(x) == str(x)[::-1]
def palindrome(str):
    return str == str[::-1]


def count_vowels(str):
    count = 0
    str = str.lower()
    for x in str:
        if(x == 'a' or x == 'e' or x == 'i'
            or x == 'o' or x == 'u' or x == 'y'):
            count += 1
    return count


def char_histogram(str):
    res_dict = {}
    for x in str:
        if res_dict.get(x, -1) != -1:
            res_dict[x] += 1
        else:
            res_dict.update({x: 1})
    return res_dict


def sum_matrix(m):
    count = 0
    for x in m:
        count += sum(x)
    return count


def max_consecutive(items):
    count = 1
    max_count = 0
    for index, value in enumerate(items):
        if index < (len(items) - 1) and items[index] == items[index + 1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 1
    return max_count


print("Task 1:")
print(to_digits(123))
print(to_digits(99999))
print(to_digits(123023))

print("Task 2:")
print(sum_of_digits(1325132435356))
print(sum_of_digits(123))
print(sum_of_digits(6))
print(sum_of_digits(-10))

print("Task 3:")
print(fact_digits(111))
print(fact_digits(145))
print(fact_digits(999))

print("Task 4:")
print(palindrome(str(121)))
print(palindrome("kapak"))
print(palindrome("baba"))

print("Task 5:")
print(count_vowels("Python"))
print(count_vowels("Theistareykjarbunga"))
print(count_vowels("grrrrgh!"))
print(count_vowels("A nice day to code!"))

print("Task 6:")
print(char_histogram("Python"))
print(char_histogram("AAAAaaa"))

print("Task 7:")
print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))

print("Task 8:")
print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
