import os 
import shutil



path = 'downloads'
os.chdir(path)




folders =['sound','picture','pdf','videos']
for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)


'''['.mp3', '.jpg', '.mp4', '.m4a', '.pdf', '.png']'''


for file in os.listdir('.'):
    file_name , file_extention =os.path.splitext(file)

    if file_extention in ['.mp3','.m4a']:
        shutil.move(file,'sound')
        print(f'Moving file : {file}')
    


    elif file_extention in ['.jpg','.png']:
        shutil.move(file,'picture')
        print(f'Moving File   :   {file}')


    elif file_extention in ['.pdf']:
        shutil.move(file,'pdf')
        print(f'Moving File   :  {file}')
    

    elif file_extention in ['.mp4']:
        shutil.move(file,'videos')
        print(f'Moving File   :   {file}')