import os
 
#机场#绿化城镇#小河沟#大海#工厂#红色城镇
def readname():
    filePath = '/media/ubuntu/新加卷/dataset/DOTA/train/traincrop800/Annotation'
    name = os.listdir(filePath)
    return name
 
path=os.path.join('/home/ubuntu/dataset/DIOR/muti_scene_label',"%s.txt")
if __name__ == "__main__":
    name = readname()
    # f=open('scene_label.txt','w')
    for i in name:
        print(i)
        lable_path=os.path.join('/home/ubuntu/dataset/DIOR/labels','%s')
        lable_path=(lable_path%i).replace('jpg','txt')
        f=open(lable_path,'r')
        dic=[]
        f2=open(path%i,'w')
        # f2.write('2')
        # f2.close()
        for j in f.readlines():
            if j[0] not in dic:
                dic.append(j[0])
                f2.write(j[0])
                f2.write("\n")
        f2.close()
    print(len(name))
    # for i in name:
    #     print(i)