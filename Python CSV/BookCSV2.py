# -*- coding: utf-8 -*-
"""
Created on Sun May 31 09:31:50 2020

@author: Ashutosh Kedar
"""
import os.path
import csv


FILE_HEADER = ["Book","Author","Released"]
FILE_PATH = "Books.csv"



def getRecords():
    numberOfRecords = int(input("How many records do you want to add:"))
    recordNo = 0
    listOfRecords = []
    while recordNo != numberOfRecords:
        aRecordTuple = ()
        print("Enter the ",recordNo," record")
        book = input("Book name:").strip()
        author = input("Author name:").strip()
        year = input("Year Released:").strip()
        aRecordTuple = book,author,year
        listOfRecords.append(aRecordTuple)
        recordNo = recordNo + 1
    return listOfRecords


def writeToCSV(listOfRecords,append = False):
    isFileExists = os.path.exists(FILE_PATH)
    finalRecord = []
    if isFileExists or append:
        with open(FILE_PATH,"a",newline='') as file:
            csvWriter = csv.DictWriter(file,delimiter=';',fieldnames=FILE_HEADER)
            for record in listOfRecords:
                finalRecord.append(dict(zip(FILE_HEADER,record)))
            for row in finalRecord:
                csvWriter.writerow(row)
    else:
        with open(FILE_PATH,"w",newline='') as file:
            csvWriter = csv.DictWriter(file,delimiter=';',fieldnames=FILE_HEADER)
            csvWriter.writeheader()
            for record in listOfRecords:
                finalRecord.append(dict(zip(FILE_HEADER,record)))
            for row in finalRecord:
                csvWriter.writerow(row)


def printHorizontalLine(numberOfLines):
    line = ''
    while numberOfLines != 0:
        line += '-'
        numberOfLines -= 1
    print(line)

def getChoice():
    print("Please select the attribute based on which you want to search.\n")
    print("1) Book Name\n2) Author Name\n3) Released Date\n4) Display All")
    while True :
        try:
            choice = int(input("Your choice:"))
        except (NameError, SyntaxError, ValueError):
            print("Please enter a integer value. Try again.")
        else:
            if choice==1:
                value = input("Enter the name of the book:")
                value = value.strip()
                break
            elif choice == 2:
                value = input("Enter the name of the author:")
                value = value.strip()
                break
            elif choice == 3:
                value=[]
                print("Enter released years between which you want to list:")
                value.append(input("Enter the start year:").strip())
                value.append(input("Enter the end year:").strip())
                break
            elif choice == 4:
                value = ''
                break
            else:
                print("Invalid input.Try again.")
    return choice,value


def displayHeader():
    printHorizontalLine(57)
    print("|{:^6s}|{:^15s}|{:^15s}|{:^15s}|".format("Sr. No",FILE_HEADER[0]\
,FILE_HEADER[1],FILE_HEADER[2]))
    printHorizontalLine(57)

def displayAllRecord():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH,'r') as file:
            csvReader = csv.DictReader(file)
            displayHeader()
            srNo = 1
            for record in csvReader:
                string = list(record.values())[0]
                data = string.split(';')
                print("|{:^6d}|{:^15s}|{:^15s}|{:^15s}|".format(srNo,data[0],data[1],data[2]))
                srNo += 1
            else:
                printHorizontalLine(57)
    else:
        print("There is no entry in the file.")
       
def displayFromCSV():    
    if os.path.exists(FILE_PATH):
        choice,value = getChoice()   
        
        if choice == 4:
                displayAllRecord()
        else:
            with open(FILE_PATH,'r') as file:
                csvReader = csv.DictReader(file)
                displayHeader() 
                visited = False
                srNo = 1
                for record in csvReader:
                    string = list(record.values())[0]
                    data = string.split(';')
                    if choice==1:
                        if data[0].lower() == value.lower():
                            visited = True
                            print("|{:^6d}|{:^15s}|{:^15s}|{:^15s}|".format(srNo,data[0],data[1],data[2]))
                            srNo += 1
                    elif choice == 2:
                        if data[1].lower() == value.lower():
                            visited = True
                            print("|{:^6d}|{:^15s}|{:^15s}|{:^15s}|".format(srNo,data[0],data[1],data[2]))
                            srNo += 1
                    elif choice == 3:
                        if   value[0]  <= data[2] <= value[1]:
                            visited = True
                            print("|{:^6d}|{:^15s}|{:^15s}|{:^15s}|".format(srNo,data[0],data[1],data[2]))
                            srNo += 1                    
                else:
                    if not visited:
                        print("No Record Found.")
                    else:
                        printHorizontalLine(57)
    else:
        print("There is no entry in the file.")
            
            
def deleteRecord():
    if os.path.exists(FILE_PATH):
         print("Deleting the record stored in the file.")
         finalListToWrite = []
         with open(FILE_PATH,"r") as file:
             csvReader = csv.DictReader(file)
             displayAllRecord() 
#             file.seek(0)
             listOfRecord = list(csvReader)
             numberOfRecords = len(listOfRecord)
             if numberOfRecords != 0:
                 while True:
                     try:
                         recordNumber = int(input("Enter the serial no. of the record which you want to delete:"))
                     except (NameError, SyntaxError, ValueError):
                         print("Invalid input, please try again.")
                     else:
                         if recordNumber in range (1,numberOfRecords+1):
                             break
                         else:
                             print("Invalid input, record not present at the position.")                                          
    #             listOfRecord.pop(0)
                 listOfRecord.pop(recordNumber-1)   
                 for record in listOfRecord:
                     recordInString = list(record.values())[0]
                     recordInList = recordInString.split(';')
                     finalListToWrite.append(recordInList)
                 os.remove(FILE_PATH)
                 writeToCSV(finalListToWrite)
                 print("Deleted successfully.")
             else:
                 print("There is no entry in the file to delete.")
    else:
        print("There is no entry in the file to delete.")
            
     
def getTaskChoice():
    print("1) Create Entry In The File\n2) Search Based On The Attribute\
\n3) Display All Records In The File\n4) Delete A Specific Record\n5)\
 Exit")
    while True:
        try:
            choice = eval(input("Enter your choice:"))
        except (ValueError,NameError):
            print("Wrong input Supplied, Try Again")
        else:
            if choice in range(1,6):
                break
            else:
                print("Invalid input supplied.")
    return choice
    
if __name__ == '__main__':
    while True:
        print("\n*Books Directory System*")
        choice = getTaskChoice()
        if choice == 1:
            listOfRecords = getRecords()
            writeToCSV(listOfRecords)
        elif choice == 2:
            displayFromCSV()
        elif choice == 3:
            displayAllRecord()
        elif choice == 4:
            deleteRecord()
        elif choice == 5:
            break
        


