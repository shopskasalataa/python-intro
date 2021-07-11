input = input("Input the elements of the list: ")
list = input.split()
unique_list = []

unique_list.append(list[0])

unique_list += [list[i] for i in range(1, len(list)) if list[i] != list[i - 1]]

print(unique_list)
