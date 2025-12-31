def main():
    time = input('What time is it? ')
    time = convert(time)

    if( 7<=time<=8):
        print('breakfast time')
    elif(12<=time<=13):
        print('lunch time')
    elif(18<=time<=19):
        print('dinner time')

def convert(time):
    fm = None
    if(time.endswith('a.m.') or time.endswith('p.m.')):
        time, fm = time.split()
    hours, minutes = time.split(':')

    if(fm == 'p.m.' and int(hours) < 12 ):
        hours = int(hours) + 12

    minutes = float(minutes)/60
    return float(hours) + minutes

if __name__ == "__main__":
    main()

