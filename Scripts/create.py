import os
from log import log_function_call



@log_function_call
def create_file(file_name,dir_name, text):
    file_path = f"Directories/{dir_name}/{file_name}.txt"
    with open(file_path, "x")as file:
        try:
            file.write(f"{text}")
            return (f'You created {file_name}.txt in {dir_name}.')
        except FileExistsError:
            print(f'{file_name} already exists.')
            return(f'{file_name} already exists.')


@log_function_call
def create_directory(dir_name):
    directory_path = f"Directories/{dir_name}"
    try:
        os.makedirs(directory_path)
        return (f'You created {dir_name} directory.')
    except FileExistsError:
        print(f"Directory '{directory_path}' already exists.")
        return(f"Directory '{directory_path}' already exists.")
    except OSError as e:
        print(f"An error occurred while creating the directory: {e}")
        return(f"An error occurred while creating the directory: {e}")

@log_function_call    
def delete(file_name, dir_name):
    file_path = f"Directories/{dir_name}/{file_name}.txt"
    try:
        os.remove (file_path)
        return (f'You deleted {dir_name}/{file_name}.')
    except FileNotFoundError:
        print (f'File {dir_name}/{file_name} not found.')
        return (f'File {dir_name}/{file_name} not found.')
    
def dir_list():
    directory_path = "Directories/"
    dir_list = os.listdir(directory_path)
    dirs = [item for item in dir_list]
    return dirs

def file_list(dir_name):
    directory_path = f"Directories/{dir_name}"
    file_list = os.listdir(directory_path)
    files = [item for item in file_list]
    files_dict = {dir_name : files}
    return files_dict

def full_list():
    dirs = dir_list()
    full_list = []
    for item in dirs:
        full_list.append(file_list(item))
    return full_list

                



    


if __name__ == "__main__" : 
     
    pass

