from os import path,walk
from zipfile import ZipFile

def get_all_file_paths(directory):

    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = path.join(root, filename)
            file_paths.append(filepath)

        # returning all file paths
    return file_paths

def ZIP(i,p):
    directory = "./"+i
    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)

    # printing the list of all files to be zipped
    # print('Following files will be zipped:')

    for file_name in file_paths:
        print(file_name)

    # writing files to a zipfile
    with ZipFile(p+".zip", 'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
    print('All files zipped successfully!')

def UNZIP(o):
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile(o+'.zip', 'r') as zipObj:

        # Extract all the contents of zip file in different directory
        zipObj.extractall()



def main():
    z = input("would you like to ZIP(z) or UNZIP(u): ")

    #for zipping a file

    if z == 'z' or z == 'Z':
        i=input("enter file path: ")
        #path to folder which needs to be zippe
        p=i
        ZIP(i,p)


    elif z == 'u' or z == "U":   #for unzipping file

        o=input("name of the zip file: ")
        UNZIP(o)


if __name__== "__main__":
    main()
