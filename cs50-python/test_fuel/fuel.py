def main():
    fraction = input("Fraction: ")
    perc = convert(fraction)
    print(gauge(perc))


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if x > y or x < 0 or y < 0:
        raise ValueError()
    elif y == 0:
        raise ZeroDivisionError()
    return int(round((x / y) * 100))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
