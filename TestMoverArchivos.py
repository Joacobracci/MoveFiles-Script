import os
import shutil
import json


f = open ("config.json", "r")

paths = json.loads(f.read())

dir_list = os.listdir(paths["start"])

count = 0
for file in dir_list:
    if count == 50 :
        break
    else:
        relativePath = paths["start"]+"/"+ file
        shutil.move(relativePath, paths["finalPath"])
        count = count +1 