from PIL import Image
import sys,os

if len(sys.argv) > 1:
    if os.path.isfile("./"+sys.argv[1]):
        im = Image.open("./"+sys.argv[1])
        im.show()
    else:
        error("Invalid file.")
else:
    fl = input("Which picture do you want to open?\n")
    if os.path.isfile("./"+fl):
        im = Image.open("./"+fl)
        im.show()
    else:
        error("Invalid file.")
