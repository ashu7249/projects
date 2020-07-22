# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 16:26:25 2020

@author: Ashutosh Kedar
"""
import tkinter
import tkinter.messagebox
import tkinter.simpledialog
import sqlite3

class Working:
    def __init__(self):
        pass
#        self.UIObject = UIObject
        
        
        
        
    def getName(self):
        name = ""
        while True:
            name = tkinter.simpledialog.askstring("Ask name","Enter name")
#            print(name)
            if name.isspace() :
                tkinter.messagebox.showwarning("Oppps","Please provide a valid name.")
            else:
                break
        return name
    
    def getState(self):
        state = ""
        while True:
            state = tkinter.simpledialog.askstring("Ask state","Enter state")
            if state.isspace():
                tkinter.messagebox.showwarning("Oppps","Please provide a valid state name.")
            else:
                break
        return state
        
        
#    def getAge(self):
#        age = tkinter.simpledialog.askinteger("Ask Age","Enter your Age")

    
    def addButton(self,UIObject):
        UIObject.textArea.config(state='normal')
        name = self.getName()
        age = tkinter.simpledialog.askinteger("Ask Age","Enter Age")
        state = self.getState()
#        self.UIObject.textArea.getData()
        self.__addToDatabase(name,age,state)
        
        UIObject.textArea.insert(tkinter.END,"\n\t\t"+name+"\t\t"+str(age)+"\t\t"+state)
        UIObject.textArea.config(state=tkinter.DISABLED)
        
        
        
    def __addToDatabase(self,name,age,state):
        connection = sqlite3.connect("UserData.db")
        dbCursor = connection.cursor()
        creatTablequery = "CREATE TABLE IF NOT EXISTS users (name TEXT , age INTEGER, state TEXT)"
        dbCursor.execute(creatTablequery)
        addDataQuery = "INSERT INTO users VALUES (?,?,?)"
        dbCursor.execute(addDataQuery,(name,age,state))
        connection.commit()
        connection.close()
        
    
        
        
        
    def updateButton(self,UIObject):
        name = self.getName()
        if self.__checkIfExist(name):
            age = tkinter.simpledialog.askinteger("Ask Age","Enter Age")
            state = self.getState()
            self.__deleteRecords(name , True, silent = False)
            self.__addToDatabase(name,age,state)
            tkinter.messagebox.showinfo("Success","Data Updated Successfully")
            self.refreshTextArea(UIObject)
        else:
            tkinter.messagebox.showerror("Wrong","There is no entry with this name")
    
    
    def removeButton(self,UIObject):
        name = self.getName()
        if self.__checkIfExist(name):
            self.__deleteRecords(name , True)
            self.refreshTextArea(UIObject)
        else:
            tkinter.messagebox.showerror("Wrong","There is no entry with this name")
            
    
    def clearDatabaseButton(self,UIObject):
        connection = sqlite3.connect("UserData.db")
        cursor = connection.cursor()
        sqlCheckQuery = "SELECT * FROM users"
        if cursor.execute(sqlCheckQuery).fetchall():
            self.__deleteRecords()
            self.refreshTextArea(UIObject)
        else:
            tkinter.messagebox.showerror("Wrong","Database is Empty")
    
    
    def __checkIfExist(self,name):
        connection = sqlite3.connect("UserData.db")
        cursor = connection.cursor()
        sqlCheckQuery = "SELECT * FROM users WHERE name = '{}'".format(name)
        if cursor.execute(sqlCheckQuery).fetchall():
            return True
        else:
            return False
     
    def __deleteRecords(self,key = "ALL" ,  singledata = False ,silent=True):
        connection = sqlite3.connect("UserData.db")
        cursor = connection.cursor()
        if not singledata:
            dropTableQuery = "DELETE FROM users"
            cursor.execute(dropTableQuery)
            tkinter.messagebox.showinfo("Success", "Table Data Cleared Successfully") 
            
        else:
            deleteRecordQuery = "DELETE FROM users WHERE name = '{}'".format(key)
            cursor.execute(deleteRecordQuery)
            if silent:
                tkinter.messagebox.showinfo("Success", "Data Cleared Successfully")
        
        connection.commit()
        connection.close()
     
    def refreshTextArea(self,UIObject):
#        print("Allllllllllllllllo")
        UIObject.textArea.config(state='normal')
        UIObject.textArea.delete('1.0',tkinter.END)
        connection = sqlite3.connect("UserData.db")
        cursor = connection.cursor()
        selectQuery = "Select * from users"
        listOfData = cursor.execute(selectQuery).fetchall()
        for record in listOfData:
            UIObject.textArea.insert(tkinter.END,"\n\t\t"+record[0]+"\t\t"+str(record[1])+"\t\t"+record[2])
        
        if not listOfData:
            tkinter.messagebox.showinfo("Empty","Database is now Empty")
        
        UIObject.textArea.config(state=tkinter.DISABLED)
        
    