from PIL import Image
import os
import sys

rootdir = os.getcwd() + '\\' + sys.argv[1]
cvtdir = os.getcwd() + '\\' + sys.argv[2]

if not os.path.exists(cvtdir):
    os.makedirs(cvtdir)

for filename in os.listdir(rootdir):
    img = Image.open(rootdir + filename)
    newname = filename.replace('jpg', 'png')
    img.save(f'{cvtdir}{newname}', 'png')
