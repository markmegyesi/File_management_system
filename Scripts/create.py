import os


def create_file(file_name,dir_name, text):
    file_path = f"Directories/{dir_name}/{file_name}.txt"
    with open(file_path, "x")as file:
        try:
            file.write(f"{text}")
        except FileExistsError:
            print(f'{file_name} already exists.')



def create_directory(dir_name):
    directory_path = f"Directories/{dir_name}"
    try:
        os.makedirs(directory_path)
    except FileExistsError:
        print(f"Directory '{directory_path}' already exists.")
    except OSError as e:
        print(f"An error occurred while creating the directory: {e}")

def delete(file_name, dir_name):
    pass

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
        

