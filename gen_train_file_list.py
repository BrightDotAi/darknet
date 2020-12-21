import os
from glob import glob


src_path = '/workspace/AB_darknet/data/coco/train2017'
file='/workspace/AB_darknet/data/laundry_train.txt'

file_list = glob(src_path+"/*.jpg")
print("total files:",len(file_list))

with open(file,"w") as f:
   for jpg in file_list:
      f.write(jpg+"\n")
print(file,"is generated")
   
