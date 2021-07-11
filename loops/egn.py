regions = {
    'Blagoevgrad': (0, 43),
    'Burgas': (44, 93),
    'Varna': (94, 139)
}
year = '19'


egn = input()
control = int(egn[9])
region = int(egn[6:9])
day = egn[4:6]
month = egn[2:4]
year = year + egn[:2]

if month[0] >= '2':
    month = list(month)
    year = list(year)
    if month[0] >= '4':
        month[0] = chr(ord(month[0]) - 4)
        year[0] = chr(ord(year[0]) + 1)
    else:
        month[0] = chr(ord(month[0]) - 2)
        year[0] = chr(ord(year[1]) - 1)
    month = "".join(month)
    year = "".join(year)

if control != ((sum([int(x) * (2 ** (i + 1)) for (i, x)
                in enumerate(egn[:9])]) % 11) % 10):
    print("Invalid EGN!")
    quit()

sex = ['woman', 'girl', 'her'] if region % 2 else ['man', 'boy', 'him']

children = 0
for city in regions.keys():
    if region >= regions[city][0] and region <= regions[city][1]:
        children = (region - regions[city][0]) // 2
        region = city
        break

str = f'{egn} is the EGN of a {sex[0]}, born on {day}.{month}.{year}'
str += f' in {region}, having {children} {sex[1]}{"s" if children > 1 else ""}'
str += f' being born before {sex[2]} in that day.'
print(str)


#2902260512
#2942260512