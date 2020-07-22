# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:01:43 2020

@author: Ashutosh Kedar
"""
import tkinter

class Login:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("LOGIN")
        self.window.geometry("500x200+400+300")
        
        
        self.upperFrame = tkinter.Frame()
        self.upperFrame.pack()
        
        self.userNameLabel = tkinter.Label(self.upperFrame,text="Username",width = 20)
#                                           height =20)
        self.userNameLabel.grid(row = 1,column= 1,padx = 5,pady = 20 , sticky = (tkinter.W))
        
        self.userName = tkinter.StringVar()
        self.userNameEntry = tkinter.Entry(self.upperFrame,\
                                           textvariable = self.userName,\
                                           justify = tkinter.LEFT ,\
                                           width = 30)
#                                           height = 20)
        self.userNameEntry.grid(row = 1 , column = 2,padx = 5, pady = 20,sticky = (tkinter.E))
        
        self.passwordLabel = tkinter.Label(self.upperFrame,text = "Password",width = 20)
        self.passwordLabel.grid(row = 2,column= 1,padx = 5,pady = 15,sticky = (tkinter.W))
        
        self.password = tkinter.StringVar()
        self.passwordEntry = tkinter.Entry(self.upperFrame ,\
                                           textvariable = self.password , \
                                           justify = tkinter.LEFT ,   \
                                           width = 30
                                           )
        self.passwordEntry.grid(row = 2 , column = 2,padx = 5,pady = 15,sticky = (tkinter.E))
        
        self.bottomFrame = tkinter.Frame()
        self.bottomFrame.pack()
        
        self.loginButton = tkinter.Button(self.bottomFrame,text="LOGIN")
        self.loginButton.grid(row = 3 , column = 1,rowspan = 2,pady = 15)
        
        
        
        self.window.mainloop()
Login()