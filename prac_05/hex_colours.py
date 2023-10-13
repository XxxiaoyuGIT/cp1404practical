Color_Codes = {
    "BABYBLUE": "#89CFF0",
    "BABYPINK": "#F4C2C2",
    "CADETBLUE1": "#98F5FF",
    "CELESTE": "#B2FFFF",
    "CRYSTL": "#A7D8DE",
    "COTTONCANDY": "#FFBCD9",
    "ICEBERG": "#71A6D2",
    "LAVENDERBLUE": "#CCCCFF",
    "LIGHTBLUE": "#ADD8E6",
    "LIGHTSKYBLUE": "#87CEFA"
}

while True:
    color_name = input("Enter a color name (or blank to exit): ").upper()

    if not color_name:
        break

    try:
        color_code = Color_Codes[color_name]
        print(f"{color_name} is {color_code}")
    except KeyError:
        print("Invalid color name")

print("Program exited.")
