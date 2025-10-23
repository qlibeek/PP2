#1
import os

path= r"/Users/burakhanov/Documents"
all=list(os.listdir(path))
print(all)

#2
import os
def check_access(path):
    if not os.path.exists(path):
        print("path doesn't exist")
        return 
    else:
        print('path does exist')
        if os.access(path, os.R_OK):
            print("readable")
        else:
            print("don't readable")
        if os.access(path, os.W_OK):
            print("writable")
        else:
            print("don't writable")
        if os.access(path, os.X_OK):
            print("executable")
        else:
            print("don't executable")

if __name__ == "__main__":
    path_to_check = r"C:/Users/burakhanov/Documents"
    
check_access(path_to_check)

#3
import os
path= r"/Users/burakhanov/Documents"
def checker(path):
    if os.path.exists(path):
        print("Name of file: ", os.path.basename(path))
        print("name of directory: ", os.path.dirname(path))
        return "success"
    
print(checker(path))

#4
import os
import string

with open("sometext.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()

#5
def writesome(list_of_elements):
    with open("sometext.txt", '+a') as f:
        text = "\n"
        for i in list_of_elements:
            text+=str(i)+' '
        f.write(text)
        f.close()
    
 

writesome([12345, 56789, 90987654, "dfghjkl","efrgf",34,34])

#6
import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write("hello world")

if __name__ == "__main__":
    generate_files()

#7
def copier():
    string = str(input("Enter the name of file: "))
    with open(string) as file:
        data = file.read()
    file.close()
    copy_path = ""
    for i in range(len(string)):
        if string[i]=='.':
            copy_path+='_1'
        copy_path+=string[i]
    with open(copy_path, "+w") as file_copy:
        file_copy.write(data)
    file.close()
    
    return 0

copier()

#8
import os
def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path,os.W_OK):
            try:
                os.remove(file_path)
                print(f"file {file_path} delete") 
            except Exception as e:
                print("Error")
                
                
        else:
            print("You do not have write access")
    else:
        print(f"File '{file_path}' does not exist.")
            
        
path_delete=str(input("path_delere_file:"))

delete_file(path_delete)