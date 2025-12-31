exp = input('Expression: ').strip()
exp = exp.split(' ')
x = int(exp[0])
y = exp[1]
z = int(exp[2])

match y:
    case '+':
        print(f"{x+z:.1f}")
    case '-':
        print(f"{x-z:.1f}")
    case '*':
        print(f"{x*z:.1f}")
    case '/':
        print(x/z)
