import sys
count = 0;

if len(sys.argv)==2:
    filename = sys.argv[1]
    if filename.endswith('.py'):
        try:
            with open(filename, 'r') as file:
                reader = file.readlines()
                for line in reader:
                    if(line.strip().startswith('#')):
                        pass
                    elif(line.isspace()):
                        pass
                    else:
                        count+=1
                print(count)

        except FileNotFoundError:
            print('File does not exist')
            sys.exit()
    else:
        sys.exit('Not a Python file')

elif len(sys.argv)>2:
    sys.exit('Too many command-line arguments')
else:
    sys.exit('Too few command-line arguments')
