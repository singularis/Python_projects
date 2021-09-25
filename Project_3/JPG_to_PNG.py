from PIL import Image
import sys
import os

original_folder = sys.argv[1]
new_folder = str(sys.argv[2])
files_list = os.listdir(original_folder)


if os.path.isdir(new_folder):
    print(f'Folder exists, putting in folder: {new_folder}')
else:
    os.mkdir(new_folder)
    print(f'Next folder created : {new_folder}')


for item in files_list:
    if '.jpg' in item:
        os.chdir(original_folder)
        converted = Image.open(item)
        new_item = item.replace(".jpg", '')
        os.chdir(new_folder)
        converted.save(new_item + '.png', 'png')
        gray = converted.convert('L')
        file_name = new_item + '_gray_' + '.png'
        gray.save(file_name, 'png')
        print(f'File create with name {file_name}')
print('Work is done')
