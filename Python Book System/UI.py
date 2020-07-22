# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:57:32 2020

@author: Ashutosh Kedar
"""
import tkinter
import Working

class UIFrame:
    def __init__(self,callBackObject):
       self.callBackObject = callBackObject
       self.window = tkinter.Tk()
       self.window.geometry("650x600+400+60")
       self.window.title("Data Storage system")
       self.window.resizable()
       self.window.withdraw()
       
       self.userName = callBackObject.getName()
       self.window.deiconify()
       
       self.textToDisplay = tkinter.StringVar()
       self.window.deiconify()
       self.topFrame = tkinter.Frame(self.window) 
       self.topFrame.pack()
       
       self.topLabel = tkinter.Label(self.topFrame,text="Welcome "\
                                     +self.userName ,fg="red")
       
       self.topLabel.config(font=("Courier",44))
       self.topLabel.pack()
       
       self.midFrame = tkinter.Frame(self.window)
       self.midFrame.pack()
       
       self.textArea = tkinter.Text(self.midFrame,font=('Verdana',8))
       self.textArea.pack()
       
       self.bottomFrame = tkinter.Frame(self.window)
       self.bottomFrame.pack()
       
       
       
       self.addButton = tkinter.Button(self.bottomFrame,text="Add a record",\
                                       padx=5,pady=5, command = self.__addButton)
       
       self.addButton.grid(row=2,column=1,sticky = (tkinter.W),padx=10,pady=10)
       
       self.updateButton = tkinter.Button(self.bottomFrame,text="Update a record",\
                                       padx=5,pady=5,command = self.__updateButton)
       
       self.updateButton.grid(row=2,column=2,sticky = (tkinter.W),padx=10,pady=10)
       
       self.removeButton = tkinter.Button(self.bottomFrame,text="Remove a record",\
                                       padx=5,pady=5,command=self.__removeButton)
       
       self.removeButton.grid(row=2,column=3,sticky = (tkinter.W),padx=10,pady=10)
       
       self.clearDatabaseButton = tkinter.Button(self.bottomFrame,text="Clear Database",\
                                       padx=5,pady=5,command = self.__clearDatabaseButton)
       
       self.clearDatabaseButton.grid(row=2,column=4,sticky = (tkinter.W),padx=10,pady=10)
       
       callBackObject.refreshTextArea(self)
       
       self.window.mainloop()

    def __addButton(self):
        self.callBackObject.addButton(self)
    
    def __updateButton(self):
        self.callBackObject.updateButton(self)
        
    def __removeButton(self):
        self.callBackObject.removeButton(self)
    
    def __clearDatabaseButton(self):
        self.callBackObject.clearDatabaseButton(self)

if __name__ == "__main__":
    working = Working.Working()
    UIframe = UIFrame(working)

