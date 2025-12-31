filename = input("File name: ").strip().lower()
filename = '.' + filename.split('.')[-1]

match filename:
    case '.gif':
        print('image/gif')
    case '.jpg' | '.jpeg':
        print('image/jpeg')
    case '.png':
        print('image/png')
    case '.pdf':
        print('application/pdf')
    case '.txt':
        print('text/plain')
    case '.zip':
        print('application/zip')
    case default:
        print('application/octet-stream')

