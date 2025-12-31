months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# 9/8/1636
# September 8, 1636

date = []
date_type = 0
while True:
    try:
        input_date = input('Date: ').strip()
        if(input_date[0].isalpha()):
            date = input_date.split()

            if( ',' not in date[1]):
                raise Exception()

            if(date[0] not in months):
                raise Exception()

            date[1] = date[1].replace(',', '')

            if(int(date[1]) > 31):
                raise Exception()

            date_type = 1
            break
        else:
            date = input_date.split('/')
            if(int(date[0])>12):
                raise Exception()
            if(int(date[1])>31):
                raise Exception()
            date_type = 2
            break
    except:
        continue


if(date_type == 1):
    print(date[2].zfill(4), str(months.index(date[0]) + 1).zfill(2), date[1].zfill(2), sep='-')
if(date_type == 2):
    print(date[2].zfill(4),date[0].zfill(2), date[1].zfill(2), sep='-')

