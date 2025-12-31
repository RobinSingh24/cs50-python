import inflect

p = inflect.engine()
list_names = []
while True:
    try:
        input_text = input()
        list_names.append(input_text)
    except EOFError:
        break

bye = p.join(list_names)
print(f'Adieu, adieu, to {bye}')

