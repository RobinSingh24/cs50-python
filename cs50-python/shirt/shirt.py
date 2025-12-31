from sys import argv, exit
from os.path import splitext
from PIL import Image, ImageOps

def main():
    if len(argv)!=3:
        if len(argv)>3:
            exit('Too many command-line arguments')
        else:
            exit('Too few command-line arguments')

    input = argv[1]
    output = argv[2]

    validate_files(splitext(input)[1].lower(), splitext(output)[1].lower() )

    shirt = Image.open("shirt.png")
    shirt_size = shirt.size

    try:
        photo = Image.open(input)
        # resize
        photo = ImageOps.fit(photo, shirt_size )

        photo.paste(shirt, shirt)
        photo.save(output)


    except FileNotFoundError:
        exit('Input does not exist')

def validate_files(input_extension, output_extension):
    allowed_extensions = ['.jpeg','.jpg','.png']

    if(input_extension not in allowed_extensions):
        exit('Invalid input')
    if(output_extension not in allowed_extensions):
        exit('Invalid output')
    if(input_extension != output_extension):
        exit('Input and output have different extensions')

main()
