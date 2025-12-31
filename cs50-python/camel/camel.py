def main():

    camel = input('Input: ')
    snake = print('Output: ')

    convert(camel)
    print('')

def convert(camel):
    for char in camel:
        if(char.isupper()):
            print('_' + char.lower(), end='')
        else:
            print(char, end='')

main()
