import os
import random

# trainval_percent = 0.5
train_percent = 0.8
xmlfilepath = '/media/ubuntu/新加卷/dataset/DOTA/val/VOCcrop800val/Annotations'
txtsavepath = '/media/ubuntu/新加卷/dataset/DOTA/val/VOCcrop800val/ImageSets/Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
# tr = int(num * train_percent)
# tr = int(tv * train_percent)
# trainval = random.sample(list, tv)
# train = random.sample(list, tr)

# ftrainval = open(txtsavepath + '/trainval.txt', 'w')
# ftest = open(txtsavepath + '/test.txt', 'w')
# ftrain = open(txtsavepath + '/train.txt', 'w')
# fval = open(txtsavepath + '/val.txt', 'w')
ftest = open(txtsavepath + '/test.txt', 'w')


for i in list:
    name = total_xml[i][:-4] + '\n'
    # if i in train:
    #     ftrain.write(name)
    # else:
    #     fval.write(name)
    ftest.write(name)
# ftrainval.close()
# ftrain.close()
# fval.close()
ftest.close()