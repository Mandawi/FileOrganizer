import os
import shutil

types_list=[]
files_list=[]
types=set()

for file in os.listdir():
    if os.path.isfile(file):
        typ=file[file.rfind(".")+1:].upper()
        types_list.append(typ)
        if types_list.count(typ)>1:
            types.add(typ)

for folder in types:
    if not os.path.exists(folder):
        os.mkdir(folder)

for file in os.listdir():
    typ=file[file.rfind(".")+1:].upper()
    if typ in types:
        os.rename(file, f"typ/{file}")


print(types)
