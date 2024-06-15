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


class Help:
   def __init__(self, root):
      self.root = root
      self.root.geometry("1530x790+0+0")
      self.root.title("Developer System")
      
      #Bg Image
      
                    
      title_lbl = Label(self.root, text=" Help Desk ", font=("times new roman", 25, "bold"), bg="Yellow", fg="Green")
      title_lbl.place(x=0, y=0, width=1530, height=40)
      
      main_frame = Frame(self.root, bd=2, bg="grey")
      main_frame.place(x=10, y=55, width=1500, height=720)
        
      #Developer Label
      
      Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text=" Complainant Information", font=("times new roman", 10, "bold"))
      Left_frame.place(x=10, y=10, width=725, height=580)
        
      Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text=" Developer Information", font=("times new roman", 10, "bold"))
      Right_frame.place(x=760, y=10, width=725, height=580)
      
      developer_Label = Label(Right_frame, text="Call 0754168528 for any inquiries.", font=("times new roman", 13))
      developer_Label.place(x=4, y=10)
      
      
      img = Image.open("Christine.jpg")
      img = img.resize((200, 500))
      self.photoimg = ImageTk.PhotoImage(img)
            
      bg_img = Label(Right_frame, image=self.photoimg)
      bg_img.place(x=500, y=15, width=200, height=500)
        
      developer_Label = Label(Right_frame, text="Email any complaints to joelharold@ymail.com", font=("times new roman", 13))
      developer_Label.place(x=4, y=37)  
      
      
      back_btn=Button(Right_frame, text="Back", command=self.back_button,font=("times new roman", 10, "bold"), cursor="hand2",width=10,bg="red", fg="white")
      back_btn.place(x=500,y=520)
      
      self.var_name=StringVar()
      self.var_email=StringVar()
      self.var_complaint=StringVar()
      
      
      nameLabel = Label(Left_frame, text="Name : ", font=("times new roman", 10, "bold"))
      nameLabel.place(x=4,y=5)
      nameEntry=Entry(Left_frame,width=20, textvariable=self.var_name,font=("times new roman", 10, "bold"))           
      nameEntry.place(x=94,y=5) 
        
      emailLabel = Label(Left_frame, text="Email Address: ", font=("times new roman", 10, "bold"))
      emailLabel.place(x=4,y=35)
      emailEntry=Entry(Left_frame,width=20,textvariable=self.var_email, font=("times new roman", 10, "bold"))           
      emailEntry.place(x=94,y=35)
       
      complaintLabel = Label(Left_frame, text="What is  \n your \n Complaint ?", font=("times new roman", 10, "bold"))
      complaintLabel.place(x=4,y=65)
      complaintEntry=Entry(Left_frame,textvariable=self.var_complaint, font=("times new roman", 10, "bold"))           
      complaintEntry.place(x=94,y=65,width=400,height=200)
      
      submit_btn=Button(Left_frame,text="Submit Complaint", cursor="hand2",command=self.add_data, font=("times new roman", 10, "bold"),width=15,bg="blue",fg="white")
      submit_btn.place(x=94,y=405)
      
   def back_button(self):
        #self.facerecog_window=Toplevel(self.root)
        #importlib.reload(FaceRecog)
        self.obj=main.FaceRecognition(self.root) 
        
   def add_data(self):
             
        if self.var_name.get()=="" or self.var_email.get()=="" or self.var_complaint.get()=="":
             messagebox.showerror("Error","Enter all details to submit your complaint",parent=self.root)
        else:
            try: 
                conn=mysql.connector.connect(host="localhost", user="root", passwd="programmer1.", database="facialrecognition",auth_plugin='mysql_native_password' )
                my_cursor=conn.cursor()
                
                my_cursor.execute('''CREATE TABLE IF NOT EXISTS complaint (
                                    name TEXT,
                                    email TEXT,
                                    complaint TEXT,
                                )''')
                conn.commit()
                
                my_cursor.execute("INSERT INTO complaint VALUES(%s,%s,%s)",(
                                                                                            self.var_name.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_complaint.get()
                                                                                            ))
                
                conn.commit()
                
                conn.close()
                
                messagebox.showinfo("Success","Comlplaint Submitted. You willl receive a response in 24 hours",parent=self.root)
                
            except Exception as e:
                messagebox.showerror("Error", f"Due To : {str(e)}",parent=self.root)
                
   
                
                
    
        
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
  
   

