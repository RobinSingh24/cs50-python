def main():
    inp = input('Input: ')
    print(shorten(inp))

def shorten(word):
    res = ""
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for char in word:
        if(char in vowels):
            continue
        else:
            res+=char
    return res


if __name__ == "__main__":
    main()










