from create import create_file, create_directory, full_list



def menu():
    print('Menu:')
    print('1. Create a file.')
    print('2. Create a directory.')
    print('3. Delete a file.')
    print('4. List of the files')
    print('5. Exit')

def users_choice():
    return input("Enter your choice: ")

def main():
    while True:
        menu()
        choice = users_choice()

        if choice == '1':
            file_name = input("Enter a file name: ")
            dir_name = input ("Enter the directory name: ")
            text = input ("Enter your text: ")
            create_file(file_name, dir_name, text)

        elif choice == '2':
            dir_name = input ("Enter the directory name: ")
            create_directory(dir_name)
        elif choice == '3':
            pass
        elif choice == '4':
            dir_file_list= full_list()
            for i in dir_file_list:
                print(i)
                

        elif choice == '5':
            break
        else: 
            print("Invalid choice. Please select a valid choice.")

if __name__ == '__main__':
    main()