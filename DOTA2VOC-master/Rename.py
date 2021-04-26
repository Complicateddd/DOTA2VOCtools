
import os
path = "/media/ubuntu/新加卷/dataset/DOTA/val/VOCcrop800val/Annotations"
image_path="/media/ubuntu/新加卷/dataset/DOTA/val/VOCcrop800val/images"
filelist = os.listdir(path) #该文件夹下所有的文件（包括文件夹）
count=0





# for file in filelist:
#     print(file)
for file in filelist:   #遍历所有文件
    Olddir=os.path.join(path,file)   #原来的文件路径

    Olddir_image=os.path.join(image_path,file.strip('.xml')+'.png')

    # print(Olddir_image)

    # if os.path.isdir(Olddir):   #如果是文件夹则跳过
    #     continue
    # filename=os.path.splitext(file)[0]   #文件名
    # filetype=os.path.splitext(file)[1]   #文件扩展名
    xml_filetype='.xml'
    image_filetype='.png'
    Newdir_xml=os.path.join(path,str(count).zfill(6)+xml_filetype)  #用字符串函数zfill 以0补全所需位数
    Newdir_img=os.path.join(image_path,str(count).zfill(6)+image_filetype)  #用字符串函数zfill 以0补全所需位数
    os.rename(Olddir,Newdir_xml)#重命名
    os.rename(Olddir_image,Newdir_img)#重命名
    count+=1