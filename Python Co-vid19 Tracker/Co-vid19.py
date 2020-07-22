# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:06:04 2020

@author: Ashutosh Kedar
"""
import os
import json
import urllib.request
import sys
import time

listOFStates = "\n\n\t\t1.)Maharashtra\n\t\t2.)Tamil Nadu\n\t\t3.)Delhi\n\t\t4.)\
Gujarat\n\t\t5.)Rajasthan\n\t\t6.)Madhya Pradesh\n\t\t7.)Uttar Pradesh\n\
\t\t8.) West Bengal\n\t\t9.)Andhra Pradesh\n\t\t10.)Bihar\n\t\t11.)Karnataka\n\
\t\t12.)Punjab\n\t\t13.)Telangana\n\t\t14.)Jammu and Kashmir\n\t\t15.)Odisha\
\n\t\t16.)Haryana\n\t\t17.)Kerala\n\t\t18.)Assam\n\t\t19.)Uttarakhand\n\
\t\t20.)Jharkhand\n\t\t21.)Chhattisgarh\n\t\t22.)Chandigarh\n\t\t23.)\
Himachal Pradesh\n\t\t24.)Tripura\n\t\t25.)Goa\n\t\t26.)Ladakh\n\
\t\t27.)Puducherry\n\t\t28.)Manipur\n\t\t29.)Andaman and Nicobar Islands\n\
\t\t30.)Meghalaya\n\t\t31.)Nagaland\n\t\t32.)Dadra and Nagar Haveli and Daman and Diu\n\
\t\t33.)Arunachal Pradesh\n\t\t34.)Mizoram\n\t\t35.)Sikkim\n\
\t\t36.)Lakshadweep."

url = 'https://api.covid19india.org/data.json'

stateMappingDict = {1:"Maharashtra",2:"Tamil Nadu",3:"Delhi",4:"Gujarat",5:"Rajasthan",6:"Madhya Pradesh",7:"Uttar Pradesh",8:"West Bengal",9:"Andhra Pradesh"\
                    ,10:"Bihar",11:"Karnataka",12:"Punjab",13:"Telangana",14:"Jammu and Kashmir",15:"Odisha",16:"Haryana",17:"Kerala",18:"Assam"\
                    ,19:"Uttarakhand",20:"Jharkhand",21:"Chhattisgarh",22:"Chandigarh",23:"Himachal Pradesh",24:"Tripura",25:"Goa",26:"Ladakh",27:"Puducherry"\
                    ,28:"Manipur",29:"Andaman and Nicobar Islands",30:"Meghalaya",31:"Nagaland",32:"Dadra and Nagar Haveli and Daman and Diu",33:"Arunachal Pradesh",34:"Mizoram",\
                    35:"Sikkim",36:"Lakshadweep"}


terminalDimensions = os.get_terminal_size()
column = terminalDimensions.columns



def printHrizontalLine(linesToPrint):
    line = ""   
    while linesToPrint != 0:
        line += "-"
        linesToPrint -= 1
    else:
        print(line.center(column),end='')



def  printDayWise(var):
     printHrizontalLine(49)
     print("|{:^17s}|{:^14s}|{:^14s}|".format("Date","Active cases","Recovered").center(column),end='')
     printHrizontalLine(49)
     for data in var['cases_time_series']:
#           print("""On {0} there were {1} total confirmed cases and {2} total recovered cases in India""".format(data['date'],data['totalconfirmed']
#                ,data['totalrecovered']))
        print("|{:^17s}|{:^14s}|{:^14s}|".format(data['date'],data['totalconfirmed'],data['totalrecovered']).center(column),end='')
     else:       
        printHrizontalLine(49)
        
        
def getStateChoice():
    
    while True:
        try:
            choice = eval(input('''Please enter the corresponding number of the state you want to know (Enter '0' to go back):''' ))
            if isinstance(choice,int):
                pass
            else:
                raise ValueError("Please enter the corresponding number in Integer.".center(column))
        except ValueError as vlError:
            print(vlError,file=sys.stderr)
        except (SyntaxError , NameError) :
            print("Please enter the corresponding number in Integer.".center(column),file=sys.stderr)
        else:
            if choice in range(0,37):
                break
            else:
                print("Invalid input. Try again\n".center(column), file = sys.stderr)
    return choice
    

def stateWiseData(var):
    print(listOFStates)
    while True:
        choice = getStateChoice()
        if choice == 0:
            break
        state = stateMappingDict[choice]
        for stateRecord in var["statewise"]:
                if stateRecord['state'] == state:
                    print("\n{state} had total {confirmedcase} confirmed cases,\n\
Out of which {recovered} patients recovered,\n\
{death} patients died.\n\
At present {state} has {active} corona cases.\n\
\t(Last updated at:{updated})\n".format(state = stateRecord['state'],confirmedcase = stateRecord['confirmed'],recovered = stateRecord['recovered'],death=stateRecord['deaths'],active=stateRecord['active'],updated=stateRecord['lastupdatedtime']))
        
   

def testConducted(var):
    printHrizontalLine(59)
    print("|{:^18s}|{:^18s}|{:^20s}|".format("Samples Tested","Tests per million","Time updated" ).center(column),end='')
    printHrizontalLine(59)
    for record in var['tested']:
        if len(record['testspermillion']) == 0:
            record['testspermillion'] = "Yet to Update"
        if len(record['totalsamplestested']) == 0:
            record['totalsamplestested'] = "Yet to Update"
        print("|{:^18s}|{:^18s}|{:^20}|".format(record['totalsamplestested'],record['testspermillion'],record['updatetimestamp']).center(column),end='')
    else:
        printHrizontalLine(59)
        
 
              
def getChoice(column):
    
    print("\t\t1.) Press 1 to get State Wise records.")
    print("\t\t2.) Press 2 to get record of day to day leads (From 30th Janauary).")
    print("\t\t3.) Press 3 to get record of day to day tests conducted.")
    print("\t\t4.) Press 4 to exit")
    while True:
        try:
            choice = eval(input("\t\t*Enter you choice:"))
            if isinstance(choice,int):
                if choice in range(1,5):
                    break
                else:
                    print("Invalid input.Try again.")
        except (SyntaxError , NameError):
            print("Please enter the Integer value.")
        else:
            pass
    return choice

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(url) as dataset:
            var = json.loads(dataset.read())  
            while True:
                print("\n")
                print("\"Real Time Corona Patients Update\"".center(column))
                print("\n")
                choice = getChoice(column)
                if choice == 1:
                    stateWiseData(var)
                elif choice == 2:
                    printDayWise(var)
                elif choice == 3:
                    testConducted(var)
                elif choice == 4:
                    os.sys.exit()
    except Exception:
         print("Please connect to a network, and restart again.")
         time.sleep(5)
    
   
    