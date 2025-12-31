from pyfiglet import Figlet
import sys
import random


figlet = Figlet()
list_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    random_font = random.choice(list_fonts)
    figlet.setFont(font=random_font)

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if not sys.argv[2] in list_fonts:
            sys.exit('Invalid usage')
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')

input_text = input("Input: ")
print(figlet.renderText(input_text))
