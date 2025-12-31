list = {}

while True:
    try:
        item = input('').strip().upper()
        if(list.get(item)):
            list[item]+= 1
        else :
            list[item] = 1

    except EOFError:
        break

sorted_keys = sorted(list.keys())
sorted_dict = {key:list[key] for key in sorted_keys}

for key in sorted_dict:
    print(f'{sorted_dict[key]} {key}')
