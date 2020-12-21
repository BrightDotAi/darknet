import os
from glob import glob
import json
json_file = "/workspace/AB_darknet/data/coco/annotations/instances_val2017.json"

src_path = '/workspace/AB_darknet/data/coco/val2017'
file='/workspace/AB_darknet/data/laundry_val.txt'

with open(json_file, 'r', encoding='utf-8') as f:
   labels = json.load(f)

rev_files={}
del_files={}
annoed_files=[]
for anno in labels['annotations']:
    image_id = anno['image_id']
    annoed_files.append(image_id)

for image in labels['images']:
        id = image['id']
        file_name = image['file_name']
        if id not in annoed_files:
           del_files[file_name] = id
           labels['images'].remove(image)
        else:
           rev_files[file_name] = id

print("deleted files:",del_files)
fixed_anno_file = json_file+"-fixed.json"
with open(fixed_anno_file, 'w', encoding='utf-8') as f:
   json.dump(labels,f)


file_list = glob(src_path+"/*.jpg")
print("total files:",len(file_list))

with open(file,"w") as f:
   for jpg in file_list:
      filename = os.path.split(jpg)[-1]
      if filename in rev_files:
         f.write(jpg+"\n")
print(file,"is generated")
   
