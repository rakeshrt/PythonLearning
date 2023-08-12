import os


def Fileview(FileName):
    if(os.path.exists(FileName)):
        fd = open(FileName, "r")
        Data = fd.read()
        print("Requested file content is as below :")
        print(Data)

        fd.close()

    else:
        print("File not exist")
        return

def main():
    print("Enter file name")
    Name = input()

    Fileview(Name)


if __name__ == "__main__":
    main()