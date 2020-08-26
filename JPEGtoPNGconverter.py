from PIL import Image
from os import path, listdir, mkdir
import sys

# grab first and second arg
arg1 = sys.argv[1]
arg2 = sys.argv[2]

# check if new/ exists if not create it
if not path.isdir('./' + arg2):
    mkdir('./' + arg2)

for i in listdir('./' + arg1):
    img = Image.open('./' + arg1 + i)
    img.save('./' + arg2 + '/' + i.split('.')[0] + '.png')

