cost = 50
due = cost

while due>0:
    print('Amount Due: '+ str(due))
    print('Insert Coin: ', end='')
    coin = int(input())
    if(coin== 5 or coin == 10 or coin == 25 ):
        due -= coin

if(due<=0):
    due = -due
    print('Change Owed: ' + str(due))
