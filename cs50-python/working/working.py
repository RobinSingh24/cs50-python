import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):

    match = re.search("^(([1][0-2]|[1-9]):?[0-5]?[0-9]?) (AM|PM)? to (([1][0-2]|[1-9]):?[0-5]?[0-9]?) (AM|PM)$", s)

    if not match:
        raise ValueError

    return (format(match.group(1), match.group(3)) + " to " + format(match.group(4), match.group(6)))

def format(time, time_ap):
    split_time = time.split(":")
    time_hour = split_time[0]
    time_minutes = "00"

    if( not 1<=int(split_time[0])<=12):
            raise ValueError

    if(len(split_time)==2):
        if(not 0<=int(split_time[1])<=59):
            raise ValueError

    if time_ap == "AM":
        if split_time[0] == "12":
            time_hour = "00"
    else:
        if split_time[0] != "12":
            time_hour = str(12 + int(split_time[0]))

    if len(split_time) == 2:
        time_minutes = split_time[1]

    return time_hour.zfill(2) + ":" + time_minutes


if __name__ == "__main__":
    main()
