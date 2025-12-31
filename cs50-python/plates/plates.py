def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if(len(plate)>6 or len(plate)<2):
        return False
    elif not (plate.isalnum()):
        return False
    elif not(plate[0].isalpha() and plate[1].isalpha()):
        return False

    # find the occurence of first digit
    digit = len(plate) -1
    for char in plate:
        if(char.isnumeric()):
            if(char == '0'):
                return False

            digit = plate.index(char)

            for num in plate[digit:]:
                if(num.isalpha()):
                    return False
            break

    return True




main()
