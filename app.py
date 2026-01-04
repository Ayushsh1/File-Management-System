import os

def create_file(filename):
    try:
        with open(filename, "x") as file:
            print(f"File Name {filename} created successfully.")
    except FileExistsError:
        print(f"File Name {filename} already exists.")
    except Exception as e:
        print(f"An error occured: {e}")

def view_file():
    files=os.listdir()
    if not files:
        print("No files found in the current directory.")
    else:
        print("Files in the current directory....")
        for file in files:
            print(file) 

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File Name {filename} deleted successfully.")
    except FileNotFoundError:
        print(f"File Name {filename} does not exits.")
    except Exception as e:
        print(f"An error occured: {e}")


def read_file(filename):
    try:
        with open(filename, "r") as file:
            content=file.read()
            print(f"Content of the {filename} : \n{content}")
    except FileNotFoundError:
        print(f"File Name {filename} does not exits.")
    except Exception as e:
        print(f"An error occured: {e}")   


def edit_file(filename):
    try:
        with open(filename, "a") as file:
            content=input("Enter the content to file: ")
            file.write(content + "\n")
            print(f"File Name {filename} edited successfully.")
    except FileNotFoundError:
        print(f"File Name {filename} does not exits.")
    except Exception as e:
        print(f"An error occured: {e}")

def main():
    while True:
        print("\nFile Management System")  
        print("1: Create File")
        print("2: View All File")
        print("3: Read File")
        print("4: Edit File")
        print("5: Delete File")
        print("6: Exit")

        choice=int(input("\nEnter your choice: "))
        if choice==1:
            filename=input("Enter the file name to create:")
            create_file(filename)
        elif choice==2:
            view_file()
        elif choice==3:
            filename=input("Enter the file name to read:")
            read_file(filename)
        elif choice==4:
            filename=input("Enter the file name to edit:")
            edit_file(filename)
        elif choice==5:
            filename=input("Enter the file name to delete:")
            delete_file(filename)                           
        elif choice==6:
            print("Exiting the File Management System. Goodbye!")
            break

if __name__ =="__main__":
    main()                                      