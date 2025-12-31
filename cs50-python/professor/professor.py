import random


def main():
    score = 0
    questions = 10

    level = get_level()
    while questions != 0:
        chances = 3
        x, y = generate_integer(level), generate_integer(level)
        while chances != 0:
            print(f"{x} + {y} = ", end="")
            ans = input("")
            if ans.isnumeric():
                ans = int(ans)
                if ans == x + y:
                    score += 1
                    break
                else:
                    chances -= 1
                    print("EEE")
                    if chances == 0:
                        print(f"{x} + {y} = {x+y}")
            else:
                chances -= 1
        questions -= 1

    print("Score: " + str(score))


def get_level():
    while True:
        try:
            level = input("Level: ")
            if level.isnumeric():
                level = int(level)
                if level == 1 or level == 2 or level == 3:
                    return level
        except:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
