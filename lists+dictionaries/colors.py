input_name = input()
color_name = input_name.split()
input_code = input()
color_code = input_code.split()

colors = dict(zip(color_name, color_code))

template = "color_name: {}, color_code: {}"

for key in colors:
    print(template.format(key, colors[key]))
