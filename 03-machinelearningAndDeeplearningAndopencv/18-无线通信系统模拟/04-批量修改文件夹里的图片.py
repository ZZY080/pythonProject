import os

folder_path = 'E:/onedrive/桌面/'

# 获取文件夹内的所有文件名
file_names = os.listdir(folder_path)
print(file_names)

# 对文件名进行排序
file_names = sorted(file_names)
#
# # 遍历文件夹内的所有文件
for i, file_name in enumerate(file_names):
    # 获取文件的扩展名
    ext = os.path.splitext(file_name)[1]
    # 如果文件是图片
    if ext in ['.webp']:
        # 构造新的文件名
        new_file_name = '{:03d}{}'.format(i+1000, ".png")
        print(new_file_name)
        # 对文件进行重命名
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))