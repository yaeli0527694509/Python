import os
import shutil
from os import listdir

# הפונקציות המופעלות בהתאם לבחירת המשתמש
# 1
def create_new_folder(path):
    new_path = os.path.abspath(path)
    print("creating a new folder in " + new_path)
    os.mkdir(new_path)

# 2
def delete_folder(folder_name):
    if not os.path.isdir(folder_name):
        print("The folder " + folder_name + " does not exist.")
    elif os.stat(folder_name).st_size > 0:
        print("The folder " + folder_name + " does not empty.")
    else:
        print("Deleting folder " + folder_name)
        shutil.rmtree(folder_name)

# 3
def create_file_in_folder(file_name):
    print("creating a new folder on: " + file_name)
    open(file_name, 'w+')

# 4
def write_to_file(file_name):
    print("Enter the text you wish to write to the file")
    # אם שם התיקייה לא קיים - נוצרת כעת תיקייה בשם הזה
    if not os.path.isfile(file_name):
        file = open(file_name, 'r+')
    else:
        with open(file_name, 'a') as file:
            file.write(input())

# 5
def delete_file(path):
    # אם התיקיה לא קיימת התוכנית מציגה הודעה על כך
    if not os.path.isfile(path):
        print("The file " + path + " does not exist.")
    else:
        print("Deleting file " + path)
        save_path = os.path.abspath(path)
        os.remove(save_path)

# 6
def display_file_and_library(folder):
    # אם בטעות הכניסו ניתוב לא של תיקייה התוכנית מודיעה על הטעות ולא זורקת שגיאה
    if not os.path.isdir(folder):
        print("The routing is not directed to a folder.")
    else:
        python_folder = folder
        for file in listdir(python_folder):
            print(file)

# 7
def display_path_of_this_folder():
    print("current folder path: ", os.getcwd())


# הפונקציה עם התפריט שמפעילה בכל פעם את הפונקציה המתאימה לבחירה
def SelectAnActionToPerform():
    # הצגת תפריט למשתמש עם אפשרויות פעולות הניתנות לביצוע
    select = input("Please select an option:\n"
                   "To create a new folder in a specific location, press 1.\n"
                   "To delete an existing folder (provided it is empty), press 2.\n"
                   "To create a new file in the folder, press 3.\n"
                   "To write content to a file or add content to an existing file, press 4.\n"
                   "To delete a file at a specific location, press 5.\n"
                   "To display all files and libraries in a specific folder, press 6.\n"
                   "To display the full path of the current folder, press 7.\n")

    # בכל אפשרות בחירה מופעלת הפונקציה המתאימה שנכתבה לה
    if select == "1":
        new_path = input("enter path to new folder\n")
        create_new_folder(new_path)
    elif select == "2":
        folder_name = input("enter folder name to remove it\n")
        delete_folder(folder_name)
    elif select == "3":
        file_name = input("enter the new file name\n")
        create_file_in_folder(file_name)
    elif select == "4":
        name = input("enter file name to write in it\n")
        write_to_file(name)
    elif select == "5":
        path = input("enter file name (with a file extension) to remove\n")
        delete_file(path)
    elif select == "6":
        folder = input("enter a folder to see what's inside\n")
        display_file_and_library(folder)
    elif select == "7":
        display_path_of_this_folder()
    else:
        print("Action does not exist") # בחירה שגויה

# הפעלת הפונקציה המרכזית (שמפעילה את כל הפונקציות)
SelectAnActionToPerform()


