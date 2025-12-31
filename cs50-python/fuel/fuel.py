
while True:
    try:
        x, y = input("Fraction: ").split('/')
        x , y = int(x), int(y)
        if x>y or x<0 or y<0:
            raise Exception()
        elif y==0:
            raise ZeroDivisionError()
    except:
        pass
    else:
        break

percent = float(x/y)*100
if(percent<=1):
    print('E')
elif(percent>=99):
    print('F')
else:
    print(f'{percent:.0f}%')


