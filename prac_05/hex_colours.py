COLOR_CODES = {"black": "#000000", "azure1": "#f0ffff", "azure2": "#e0eeee",
               "azure3": "#c1cdcd", "azure4": "#838b8b", "beige": "#f5f5dc",
               "bisque1": "#ffe4c4", "bisque2": "#eed5b7", "bisque3": "#cdb79e",
               "bisque4": "#8b7d6b"}

color_name = input("Enter color name: ")
while color_name != "":
    if color_name in COLOR_CODES:
        print("The code for {} is {}".format(color_name, COLOR_CODES[color_name]))
    else:
        print("Invalid color name")
    color_name = input("Enter color name (blank to stop): ")
