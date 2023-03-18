import os
import shutil

from_dir="C:\\Users\\shiva\\Desktop\\Downloaded_Files"
to_dir="C:\\Users\\shiva\\Desktop\\Coding"

list_of_files= os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension=os.path.splitext(file_name)
    if extension== '':
        continue
    if extension in ['.txt','.doc','.docx','.pdf', '.gif','.png','.jfif', '.jpg','.jpeg']:
        path1=from_dir + '/'+ file_name
        path2=to_dir + '/'+ "Document_Files"
        path3=to_dir + '/' + "Document_Files" + '/' + file_name
        print("Path 1",path1)
        print("Path 3",path3)
    if os.path.exists(path2):
        print("moving" + file_name + "...")
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print("moving" + file_name + "...")
        shutil.move(path1,path3)