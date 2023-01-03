"""
1. Determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)
2. Find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. What is that sum?
3. cd - change directory.
    a) cd x moves in one level
    b) cd .. moves out one level
    c) cd / switches the current directory to the outermost directory, /.
    d) ls prints out all of the files and directories immediately contained by the current directory
    e) 123 abc means that the current directory contains a file named abc with size 123.
    f) dir xyz means that the current directory contains a directory named xyz.
"""

class Device:
    def __init__(self, name: str, size: int):
        self.name = "Christmas killer 2000"
        self.directories = {}
        self.files = {}

        # Directory has, name, size, subdirectories, path
        # File has, name, size, path
    
class Directory(Device):
    def __init__(self, name: str, size: int, path: str):
        self.name = name
        self.size = size
        self.path = path
        # Files has name as key and path as value
        self.files = {}

    def add_file(self, file: File):
        self.files[file.name] = file.path
        
    
class File(Device):
    def __init__(self, name: str, size: int, path: str):
        self.name = name
        self.size = size
        self.path = path


def main():
    # load data
    with open("day7/data.txt", "r") as i:
        data = i.read()



if __name__ == "__main__":
    main()