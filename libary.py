#Library indexing system
from pathlib import Path

def menu():
    #A simple menu system to all additional functionality
    print("Please select an option from the meny below:")
    print("1) Index a new file")
    print("2) Exit")
    userChoice = input()

    if userChoice == "1":
        IndexNewFile()
    elif userChoice == "2":
        quit()
    else:
        print("Invalid choice")
        menu()

def OpenFile(filename):
    return open(filename, "w")

def GetFile(filename):
    returnFile = Path(filename)
    if returnFile.is_file():
        return open(returnFile, "r")
    else:
        print("Not a valid file")
        IndexNewFile()

def GetIndex(value=0, ident="prog"):
    return ident + str(value + 1)

def IndexNewFile():
    #This function will start the process of adding indexes to the books
    rawFileName = input("Please enter name/location of file to index:")
    destinationFileName = input("Please enter name/location of new file:")
    rawFile = GetFile(rawFileName)
    destinationFile = OpenFile(destinationFileName)
    rawFileContents = rawFile.readlines()
    for i, book in enumerate(rawFileContents):
        index = GetIndex(i)
        print(index + ": " + book)
        destinationFile.write(index + ": " + book)
    rawFile.close()
    destinationFile.close()
    menu()


print("Welcome to the Library indexing system")
menu()
