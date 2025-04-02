import os
from filecmp import dircmp

def compare_directories(dir1, dir2):
    """
    Compare two directories and list files that are unique to each directory.
    """
    comparison = dircmp(dir1, dir2)

    print("Files only in", dir1)
    for file in comparison.left_only:
        print(file)

    print("\nFiles only in", dir2)
    for file in comparison.right_only:
        print(file)

def main():
    # Replace these paths with the directories you want to compare
    dir1 = input("Enter path for the first directory: ")
    dir2 = input("Enter path for the second directory: ")

    if not os.path.exists(dir1) or not os.path.exists(dir2):
        print("One or both of the directories do not exist.")
        return

    compare_directories(dir1, dir2)

if __name__ == "__main__":
    main()
