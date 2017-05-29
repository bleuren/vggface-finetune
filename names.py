import os
fileList = os.listdir(os.getcwd())
text = ''
for f in fileList:
    text = '{}{}\n'.format(text, f)
f = open('names.txt', 'w')
f.write(text)
f.close()