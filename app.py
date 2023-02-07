import hashlib
import os
import sys

def hash_file(filename):
    """"This function returns the SHA-1 hash
    of the file passed into it"""

    # make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename,'rb') as file:

        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()

def check_for_duplicates(path):
    """Checks for duplicates in the directory specified by 'path'"""

    # dictionary of files and their hash values
    files_dict = {}

    # list of duplicates
    duplicates = []

    # loop over all files in directory
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            # get the full path of the file
            file_path = os.path.join(dirpath, filename)

            # calculate hash of the file
            file_hash = hash_file(file_path)

            # if the file's hash is already in the dictionary
            if file_hash in files_dict:
                # add it to duplicates list
                duplicates.append(file_path)
            else:
                # add the hash to the dictionary
                files_dict[file_hash] = file_path

    return duplicates

if __name__ == "__main__":
    if len(sys.argv) < 2:
        duplicates = check_for_duplicates("./")
    else:
        duplicates = check_for_duplicates(sys.argv[1])

    if duplicates:
        print("Duplicate files:")
        for file_path in duplicates:
            print(file_path)
    else:
        print("No duplicate files found.")
