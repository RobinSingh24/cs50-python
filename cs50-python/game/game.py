from random import randint

while True:
    try:
        level = int(input('Level: '))
        if(level<1):
            raise Exception()
        else:
            break
    except:
        continue


ans = randint(1,level)
while True:
    try:
        guess = int(input('Guess: '))
        if(guess<1):
            raise Exception()

        if(guess<ans):
            print('Too small!')
        elif(guess>ans):
            print('Too large!')
        else:
            print('Just right!')
            break;
    except:
        continue
