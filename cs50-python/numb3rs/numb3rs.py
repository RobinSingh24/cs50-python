import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)

    if match:
        matches = [match.group(1), match.group(2), match.group(3), match.group(4)]
        for sub in matches:
            sub = re.search(r"^[0]{1,2}[0-5]{1,2}$", sub)
            if sub:
                return False

        is_all_within_range = all(0 <= int(var) <= 255 for var in matches)
        if is_all_within_range:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
