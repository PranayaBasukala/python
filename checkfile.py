import os
import shutil

types = [".mp4", ".mpeg", ".gif", ".jpg", ".jpeg", ".mp4", ".docx", ".py"]
folder_path = r'D:\\pythonLectures\\theory\\classes\\collection'

for filename in os.listdir(folder_path):
    src = os.path.join(folder_path, filename)
    if os.path.isfile(src):
        root, extension = os.path.splitext(filename)
        if extension in types:
            if extension == ".mp4":
                dst = r'D:\\pythonLectures\\theory\\classes\\videos'
            elif extension == ".docx":
                dst = r'D:\\pythonLectures\\theory\\classes\\mydocs'
            else:
                dst = r'D:\\pythonLectures\\theory\\classes\\other_files'
            shutil.move(src, dst)
