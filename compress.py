import os
from PIL import Image
input_dir = os.path.join(os.getcwd(), 'input')
output_dir = os.path.join(os.getcwd(), 'output')
fileList = os.listdir(input_dir)
for f in fileList:
    subPath = os.path.join(input_dir, f)
    subList = os.listdir(subPath)
    if not os.path.exists(os.path.join(output_dir, f)):
        os.makedirs(os.path.join(output_dir, f))
    for f2 in subList:
        if not os.path.exists(os.path.join(output_dir, f, f2)):
            im = Image.open(os.path.join(subPath, f2))
            width = 256
            ratio = float(width)/im.size[0]
            height = int(im.size[1]*ratio)
            im = im.resize((width,height),Image.BILINEAR)
            im.save(os.path.join(output_dir, f, f2),optimize=True,quality=95)
            print '{} compressed!'.format(f2)