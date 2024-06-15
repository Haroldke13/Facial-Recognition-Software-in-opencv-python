import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # Import ttk separately
from PIL import Image, ImageTk
import mysql.connector
import cv2
import main
import train
import importlib
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog
import os


class Developer:
   def __init__(self, root):
      self.root = root
      self.root.geometry("1530x790+0+0")
      self.root.title("Developer System")
      
      self.var_name=StringVar()
      self.var_email=StringVar()
      self.var_complaint=StringVar()
      #Bg Image
      
                    
      title_lbl = Label(self.root, text=" Developer Management System ", font=("times new roman", 25, "bold"), bg="Yellow", fg="Green")
      title_lbl.place(x=0, y=0, width=1530, height=40)
      
      main_frame = Frame(self.root, bd=2, bg="grey")
      main_frame.place(x=10, y=55, width=1500, height=720)
        
      #Developer Label
      
      Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text=" Attendance Information", font=("times new roman", 10, "bold"))
      Left_frame.place(x=10, y=10, width=725, height=580)
        
      Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text=" Developer Information", font=("times new roman", 10, "bold"))
      Right_frame.place(x=760, y=10, width=725, height=580)
      
      developer_Label = Label(Right_frame, text="Hola , I am Harold Joel Onyango.", font=("times new roman", 13))
      developer_Label.place(x=4, y=10)
      
      img = Image.open(r"Christine.jpg")
      img = img.resize((200, 500))
      self.photoimg = ImageTk.PhotoImage(img)
            
      bg_img = Label(Right_frame, image=self.photoimg)
      bg_img.place(x=500, y=15, width=200, height=500)
        
      developer_Label = Label(Right_frame, text="I am a fullstack developer.", font=("times new roman", 13))
      developer_Label.place(x=4, y=33)  
      
      
      back_btn=Button(Left_frame, text="Back", command=self.back_button,font=("times new roman", 10, "bold"), cursor="hand2",width=10,bg="red", fg="white")
      back_btn.place(x=500,y=500)
      
      #==========================View Complaints============================
      
      
      tableFrame = Frame(Left_frame, bd=2, bg="white", relief=RIDGE)
      tableFrame.place(x=5, y=10, width=690, height=350)
        #Scroll Bar
      scroll_x=ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(tableFrame,orient=VERTICAL)
      self.complaintTable=ttk.Treeview(tableFrame,column=("name","email","complaint"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)
        
        
        #too move the scroll bar===============================
      scroll_x.config(command=self.complaintTable.xview)
      scroll_y.config(command=self.complaintTable.yview)
        
        #Table heading=========================================================
      self.complaintTable.heading("name",text="Name")
      self.complaintTable.heading("email",text="Email")
      self.complaintTable.heading("complaint",text="Complaint")
        
      self.complaintTable["show"]="headings"

        #Table columns==========================================================================
      self.complaintTable.column("name", width=100)
      self.complaintTable.column("email", width=100)
      self.complaintTable.column("complaint", width=100)
        
      self.complaintTable.pack(fill=BOTH,expand=1)
      
      self.fetch_data()  #===================================
      
      ####-================== Complaints tab==========================

   
      
   def back_button(self):
        #self.facerecog_window=Toplevel(self.root)
        #importlib.reload(FaceRecog)
        self.obj=main.FaceRecognition(self.root) 
        
   def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", user="root", passwd="programmer1.", database="facialrecognition",auth_plugin='mysql_native_password' )
        my_cursor=conn.cursor()
        my_cursor.execute("select * from complaint ")
        data=my_cursor.fetchall()
         
        if len(data)!=0:
            self.complaintTable.delete(*self.complaintTable.get_children())
            for i in data:
                self.complaintTable.insert("",END,values=i)
            conn.commit()
            conn.close()
        pass
     
   
     
   
   
   
   
        
if __name__=="__main__":
    
    root=Tk()
    obj=Developer(root)
    root.mainloop()
  
   

