import os
from shutil import copyfile
from random import shuffle
fileList = os.listdir(os.getcwd())
i = 0
for f in fileList:
    subPath = os.path.join(os.getcwd(), f)
    if os.path.isdir(subPath) and subPath != os.path.join(os.getcwd(), 'train') and subPath != os.path.join(os.getcwd(), 'val'):
        subList = os.listdir(subPath)
        train = int(round(len(subList)*0.8))
        j = 0
        for f2 in subList:
            print '{}:{:02d}{:03d}'.format(f2, i, j)
            if j < train:
                copyfile(os.path.join(os.getcwd(), f, f2), os.path.join(os.getcwd(), 'train', '{:02d}{:03d}.jpg'.format(i,j)))
            else:
                copyfile(os.path.join(os.getcwd(), f, f2), os.path.join(os.getcwd(), 'val', '{:02d}{:03d}.jpg'.format(i,j)))
            j = j + 1
        i = i + 1