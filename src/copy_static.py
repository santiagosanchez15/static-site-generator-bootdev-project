import os
import shutil

def copy_static(source:str, destination:str) ->None:
    '''copies all information from souce and puts it into the destination'''
    #create the path strings
    

    if not os.path.exists(source): raise ValueError("Not existant source, maybe typo")
    if os.path.exists(destination): #check if the directory exists if does then delete
        shutil.rmtree(destination)

    os.mkdir(destination) # create the directory
    copy_file_recursive(source=source, destination=destination)
    

def copy_file_recursive(source:str, destination: str) -> None:
    '''Recursively checks and copies the files and directories from source to destination'''

    list_files = os.listdir(source) #get list of files/ directories in source

    for file in list_files:
        path = os.path.join(source, file) #create full path to check/copy
        if os.path.isfile(path=path): #check if file if file then just copy to destinatino
            shutil.copy(src=path, dst=destination) #copy to full dest
        else:#not a file then directory
            dir_path = os.path.join(destination, file) #create path name
            os.mkdir(path=dir_path) #create directory inside public
            copy_file_recursive(source=path, destination=dir_path) #recurse and repeat 

    

    #copy all files and subdirectories and nested files

    #copy and log the files you already copied (maybe a set), do a bfs