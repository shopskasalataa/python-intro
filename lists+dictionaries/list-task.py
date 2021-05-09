input = input("Input the elements of the list: ")
list = input.split()
unique_list = []

unique_list = [int(x) for x in set(list)]

print(unique_list)