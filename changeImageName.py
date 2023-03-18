import os

directory = 'D://recordings/InteractionHumanAndMachine/New folder' # replace with the path to your directory

for count, filename in enumerate(os.listdir(directory)):
    if filename.endswith('.jpg'): # replace with the extension of your images
        new_name = 'new_name_' + str(count) + '.jpg' # replace with your desired naming convention
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
