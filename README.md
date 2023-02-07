# **Duplicate Photos Remover**
A python script that can remove duplicate photos in a directory.

## **Functionality**
The script uses the SHA-1 hash of each file to determine if it is a duplicate or not. It loops over all files in the specified directory, calculates the hash of each file, and stores it in a dictionary. If a file's hash is already present in the dictionary, it is added to the list of duplicates. Finally, the list of duplicates is returned.

## **Usage**
To use the Duplicate Photos Remover, follow these steps:
1. Clone or download the script.
2. Open a terminal and navigate to the directory where the script is stored.
3. Run the script using the following command:


    python app.py path/to/folder

Where ``path/to/folder`` is the path to the directory where you want to remove the duplicate photos.

4. The script will print the list of duplicate photos found in the directory.

## **Dependencies**
The script requires the following libraries:

- ``os``: for accessing the file system
- ``hashlib``: for calculating the SHA-1 hash of the files

## **Limitations**
The script only considers the contents of the files, not their names, sizes, or any other attributes, to determine if they are duplicates or not.
It also only checks for duplicates within the specified directory and its subdirectories, not in any other location.

## **Conclusion**
The Duplicate Photos Remover is a simple and efficient tool for removing duplicate photos in a directory. By using the SHA-1 hash of each file, it can accurately identify and remove duplicates, saving you valuable storage space.
