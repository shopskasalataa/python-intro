input_name = input()
color_name = input_name.split()
input_code = input()
color_code = input_code.split()

colors = dict(zip(color_name, color_code))

template = "color_name: {}, color_code: {}"

for key in colors:
    print(template.format(key, colors[key]))

# това не работи, отново не знам защо, би трябвало да работи
#for key, value in colors:
#    print(template.format(key, value))
