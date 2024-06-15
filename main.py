import face_recog
#from kivy.uix.actionbar import Button
import importlib
from tkinter import *
from tkinter import messagebox
import tkinter as ttk
from PIL import Image,ImageTk
import UserDetailsButton
import os
import train 
import attendance
import help
import developer

import cv2

class FaceRecognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")
        #Bg Image
        img=Image.open("Christine1.jpg")
        img=img.resize((1530,1000))
        self.photoimg=ImageTk.PhotoImage(img)
        
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=1000)
        
        
        title_lbl=Label(bg_img,text="Facial Recognition Attendance System",font=("times new roman",25,"bold"),bg="grey",fg="purple")
        title_lbl.place(x=0,y=0,width=1530,height=40)
      
        
          
        #User Button###################
        img1=Image.open("Lavine.jpg")
        img1=img1.resize((220,220))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        
        
          
        b1=Button(bg_img,image=self.photoimg1,cursor="hand2",command=self.user_details)
        b1.place(x=200,y=100,width=220,height=220)
        
      
        #b1=Button(bg_img,image=self.photoimg1,cursor="hand2")
        #b1.place(x=200,y=100,width=220,height=220)       
        
        
        b1_1=Button(bg_img,text="User Details",cursor="hand2", font=("times new roman",15,"bold"),bg="blue",fg="white",command=self.user_details)
        b1_1.place(x=200,y=300,width=220,height=40)    
        
        #==============================Detect face button
        
        img2=Image.open("Me.jpg")
        img2=img2.resize((220,220))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        b2=Button(bg_img,image=self.photoimg2,cursor="hand2",command=self.face_data)
        b2.place(x=480,y=100,width=220,height=220)       
        
        b2_1=Button(bg_img,text="Detect Face",cursor="hand2",command=self.face_data, font=("times new roman",15,"bold"),bg="blue",fg="white")
        b2_1.place(x=480,y=300,width=220,height=40)    
        
           #======================Attendance face button
           
           
        img3=Image.open("Maureen.jpg")
        img3=img3.resize((220,220))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        b3=Button(bg_img,image=self.photoimg3,cursor="hand2",command=self.attendace_data)
        b3.place(x=740,y=100,width=220,height=220)       
        
        b3_1=Button(bg_img,text="Attendance ",cursor="hand2",command=self.attendace_data, font=("times new roman",15,"bold"),bg="blue",fg="white")
        b3_1.place(x=740,y=300,width=220,height=40)  
        
           #Help button
        img4=Image.open("Christine1.jpg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b4=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.help_data)
        b4.place(x=1000,y=100,width=220,height=220)       
        
        b4_1=Button(bg_img,text="Help ",cursor="hand2",command=self.help_data ,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b4_1.place(x=1000,y=300,width=220,height=40)  
        
        
           #Train Face
        img5=Image.open("Me.jpg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b5=Button(bg_img,image=self.photoimg5,cursor="hand2", command=self.train_data)
        b5.place(x=200,y=380,width=220,height=220)       
        
        b5_1=Button(bg_img,text="Train Face ",cursor="hand2", command=self.train_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b5_1.place(x=200,y=580,width=220,height=40)  
        
          #Photos Face Button
        img6=Image.open("Lavine.jpg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b6=Button(bg_img,image=self.photoimg6,command=self.open_img,cursor="hand2")
        b6.place(x=480,y=380,width=220,height=220)       
        
        b6_1=Button(bg_img,text="Photos",cursor="hand2", command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b6_1.place(x=480,y=580,width=220,height=40)  
        
          #Developer Face Button
        img7=Image.open("Maureen.jpg")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b7=Button(bg_img,image=self.photoimg7,command=self.developer_data,cursor="hand2")
        b7.place(x=740,y=380,width=220,height=220)       
        
        b7_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data, font=("times new roman",15,"bold"),bg="blue",fg="white")
        b7_1.place(x=740,y=580,width=220,height=40)  
        
          #Exit Button
        img8=Image.open("Christine1.jpg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b8=Button(bg_img,image=self.photoimg8,command=self.close,cursor="hand2")
        b8.place(x=1000,y=380,width=220,height=220)       
        
        b8_1=Button(bg_img,text="Exit",cursor="hand2", command=self.close,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b8_1.place(x=1000,y=580,width=220,height=40)  
        
    
    def open_img(self):
        os.startfile("data")
        
    
    def close(self):
            print('Product : Close Method Called')
            close_=messagebox.askyesno("CLOSE THE SYSTEM"," DO YOU REALLY WANT TO CLOSE ?")
            
            if close_:
                root.destroy()
                print('Product : Close Method Finished')
    
    
    

    #this opens the  user detaills button
     
    def user_details(self):
        importlib.reload(UserDetailsButton)  # Reload module.py to ensure the latest changes are applied
        obj=UserDetailsButton.User(self.root)
        
        
    def train_data(self):
        #self.new_window=Toplevel(self.root)
        self.obj=train.TrainButton(self.root)
        
    
    def face_data(self):
        #self.new_window=Toplevel(self.root)
        self.obj=face_recog.Facial_Recognition(self.root)
        
    def attendace_data(self):
        #self.new_window=Toplevel(self.root)
        self.obj=attendance.Attendance(self.root)
        
    def help_data(self):
        #self.new_window=Toplevel(self.root)
        self.obj=help.Help(self.root)
        
    def developer_data(self):
        #self.new_window=Toplevel(self.root)
        self.obj=developer.Developer(self.root)
        
            
    """def user_details(self):
        self.new_window=Toplevel(self.root)
        self.app=User(self.root)"""
    """
    def user_details(self):
        self.new_window=Toplevel(self.root)
        self.app=DetectFace(self.root)
        
    def user_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.root)
        
    def user_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.root)on_button_click
    def user_details(self):
        self.new_window=Toplevel(self.root)
        self.app=TrainFace(self.root)
        
    def user_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.root)
        
    def user_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Exit(self.root)
    """    
if __name__=="__main__":
    root=Tk()
    obj=FaceRecognition(root)
    root.mainloop()
    