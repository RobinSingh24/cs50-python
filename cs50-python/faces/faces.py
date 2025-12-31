def main():
    text = input("Enter text ")
    print(convert(text))

def convert(str):
    return str.replace(":)", "🙂").replace(":(","🙁")

main()


