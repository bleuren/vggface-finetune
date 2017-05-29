#format images name from xxxx/yyy.jpg to xxxx/xxxx_{0000(seq)}.jpg
import os
fileList = os.listdir(os.getcwd())
for f in fileList:
    subPath = os.path.join(os.getcwd(), f)
    subList = os.listdir(subPath)
    i = 0
    for f2 in subList:
        os.rename(os.path.join(os.getcwd(), f, f2), os.path.join(os.getcwd(), f, '{}_{:04d}.jpg'.format(f,i)))
        print 'new name: {}'.format(os.path.join(os.getcwd(), f, '{}_{:04d}.jpg'.format(f,i)))
        i = i + 1
