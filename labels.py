#generate train.txt and val.txt
import os
train = os.listdir(os.path.join(os.getcwd(), 'train'))
val = os.listdir(os.path.join(os.getcwd(), 'val'))
text = ''
for f in train:
    text = '{}{} {}\n'.format(text, f, int(f[:2]))
f = open('train.txt', 'w')
f.write(text)
f.close()
text = ''
for f in val:
    text = '{}{} {}\n'.format(text, f, int(f[:2]))
f = open('val.txt', 'w')
f.write(text)
f.close()

