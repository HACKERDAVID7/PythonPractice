import os

if __name__ == "__main__":
    # Get Current Directory
    print(os.getcwd())
    # List Directories and Files
    print(os.listdir())
    # Making a New Directory
    os.mkdir('newdir')

    os.listdir()

    # rename a directory
    os.rename('newdir','new_one')

    os.listdir()

    # delete "myfile.txt" file
    os.remove("myfile.txt")

    # delete the empty directory "mydir"
    os.rmdir("new_one") 

    import shutil

    # delete "mydir" directory and all of its contents
    shutil.rmtree("mydir")