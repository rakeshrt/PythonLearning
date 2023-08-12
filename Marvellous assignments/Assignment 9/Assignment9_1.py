import os


def Filecheck(FileName):
    if os.path.exists(FileName):
        print("File exist in current directory")
        return
    else:
        print("File is not exist in current directory")


def main():
    print("Enter filename to check :")
    Name = input()

    Filecheck(Name)


if __name__ == "__main__":
    main()
