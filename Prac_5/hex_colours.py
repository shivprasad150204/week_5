"""
CP1404/CP5632 Practical

"""

HEX_COLOURS = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "BlueViolet": "#8a2be2"
}

def main():
    print("Hexadecimal colour codes lookup program")
    colour_name = input("Enter colour name: ").title()
    while colour_name != "":
        try:
            print(f"{colour_name} is {HEX_COLOURS[colour_name]}")
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").title()

if __name__ == "__main__":
    main()
