import os
import shutil
# os.makedirs('excelfiles')
root = os.getcwd()
files =  os.listdir()
for file in files:
    if file.endswith('.xlsx'):
        if os.path.exists(f'excelfiles/{file}'):
            os.remove(f'excelfiles/{file}')
            shutil.move(file,'excelfiles/')