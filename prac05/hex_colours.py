# Dictionary of color names and their hexadecimal codes
COLOR_TO_CODE = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}

print("Color Codes:")
for color_name, color_code in COLOR_TO_CODE.items():
    print(f"{color_name.capitalize()}: {color_code}")

color_name = input("Enter color name: ").lower()
while color_name != "":
    try:
        print(f"The hexadecimal code for {color_name} is {COLOR_TO_CODE[color_name]}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").lower()
