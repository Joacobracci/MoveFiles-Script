import os
import shutil
import json


f = open ("config.json", "r")

config = json.loads(f.read())

dir_list = os.listdir(config["start"])

count = 0
for file in dir_list:
    if count == int(config["lote"]) :
        break
    else:
        relativePath = config["start"]+"/"+ file
        shutil.move(relativePath, config["finalPath"])
        count = count +1 