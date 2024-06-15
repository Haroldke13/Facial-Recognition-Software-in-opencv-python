import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # Import ttk separately
from PIL import Image, ImageTk

import cv2
import main
import train
import importlib
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog
import os

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Attendance Management System")
        
        #=============Variables===================
        self.var_empID=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_status=StringVar()
        
        #Bg Image
        img = Image.open("Maureen.jpg")
        img = img.resize((1530, 1200))
        self.photoimg = ImageTk.PhotoImage(img)
            
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=50, width=1530, height=1000)
            
        bg_img.place(x=0, y=50, width=1530, height=1000)
                    
        title_lbl = Label(bg_img, text=" Attendance Management System ", font=("times new roman", 25, "bold"), bg="Yellow", fg="Green")
        title_lbl.place(x=0, y=0, width=1530, height=40)
        main_frame = Frame(bg_img, bd=2, bg="grey")
        main_frame.place(x=10, y=55, width=1500, height=720)

        ####################### Left label frame()
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text=" Attendance Information", font=("times new roman", 10, "bold"))
        Left_frame.place(x=10, y=10, width=725, height=580)

        imgLeft = Image.open("Christine1.jpg")
        imgLeft = imgLeft.resize((720, 100))
        self.photoimgLeft = ImageTk.PhotoImage(imgLeft)

        frameLabelLeft = Label(Left_frame, image=self.photoimgLeft)
        frameLabelLeft.place(x=5, y=0, width=710, height=70)

        # #########################  Current course
        studentFrame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=("times new roman", 10, "bold"))
        studentFrame.place(x=5, y=65, width=710, height=530)
        
        
        
        empIdLabel = Label(studentFrame, text="Student Number: ", font=("times new roman", 10, "bold"))
        empIdLabel.grid(row=0, column=0,pady=3,sticky=W)
        empIdEntry=Entry(studentFrame,width=20, font=("times new roman", 10, "bold"),textvariable=self.var_empID)           
        empIdEntry.grid(row=0, column=1,pady=3,sticky=W) 
          
        
        
        nameLabel = Label(studentFrame, text="Name : ", font=("times new roman", 10, "bold"))
        nameLabel.grid(row=1, column=0,pady=3,sticky=W)
        nameEntry=Entry(studentFrame,width=20, font=("times new roman", 10, "bold"),textvariable=self.var_name)           
        nameEntry.grid(row=1, column=1,pady=3,sticky=W) 
          
        
        depLabel = Label(studentFrame, text="Deparment : ", font=("times new roman", 10, "bold"))
        depLabel.grid(row=1, column=2,pady=3,sticky=W)
        depLabelEntry=Entry(studentFrame,width=20, font=("times new roman", 10, "bold"),textvariable=self.var_dep)           
        depLabelEntry.grid(row=1, column=3,pady=3,sticky=W)  
        
        
        timeLabel = Label(studentFrame, text="Time: ", font=("times new roman", 10, "bold"))
        timeLabel.grid(row=2, column=0,pady=3,sticky=W)
        timeEntry=Entry(studentFrame,width=20, font=("times new roman", 10, "bold"),textvariable=self.var_time)           
        timeEntry.grid(row=2, column=1,pady=3,sticky=W) 
          
        
        dateLabel = Label(studentFrame, text="Date : ", font=("times new roman", 10, "bold"))
        dateLabel.grid(row=2, column=2,pady=3,sticky=W)
        
        dateLabelEntry=Entry(studentFrame,width=20, font=("times new roman", 10, "bold"),textvariable=self.var_date)           
        dateLabelEntry.grid(row=2, column=3,pady=3,sticky=W)  
        
        
        
                    
        #Years DropDown===============================
        statusLabel = Label(studentFrame, text="Attendance Status", font=("times new roman", 10, "bold"))
        statusLabel.grid(row=3, column=0,pady=3, sticky=W)
        self.statusCombo = ttk.Combobox(studentFrame,font=("times new roman", 10, "bold"), state="readonly",textvariable=self.var_status)
        self.statusCombo["values"] = ("Status ", "Attended","Absconded")
        self.statusCombo.current(0)
        self.statusCombo.grid(row=3, column=1, pady=3, sticky=W)   
        
        
        
        #===================================Buttons===============================================status
        
        buttonFrame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Buttons", font=("times new roman", 10, "bold"))
        buttonFrame.place(x=5, y=500, width=710, height=50)
        
        
                
        importCsv=Button(buttonFrame,text="Import csv",font=("times new roman", 10, "bold"),width=20,command=self.import_csv, cursor="hand2",bg="violet",fg="white")
        importCsv.grid(row=0,column=0,padx=14)
        
        exportCsv=Button(buttonFrame, text="Export csv",command=self.exportCsv ,cursor="hand2",width=20, font=("times new roman", 10, "bold"),bg="blue", fg="white")
        exportCsv.grid(row=0,column=1,padx=14)
        
        updateBtn=Button(buttonFrame,text="Update", cursor="hand2",width=20,font=("times new roman", 10, "bold"),bg="indigo",fg="white")
        updateBtn.grid(row=0,column=2,padx=14)
        
        resetBtn=Button(buttonFrame, text="Reset", cursor="hand2",width=20, command=self.reset_fields,font=("times new roman", 10, "bold"),bg="blue", fg="white")
        resetBtn.grid(row=0,column=3,padx=14)
        
        
        
        
        
        
        #########333# Right label frame()======================================================
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details Table", font=("times new roman", 12, "bold"))
        right_frame.place(x=740, y=10, width=720, height=600)
        
        imgRight = Image.open("Maureen.jpg")
        imgRight = imgRight.resize((720, 100))
        self.photoimgRight = ImageTk.PhotoImage(imgRight)
        
        frameLabelRight = Label(right_frame, image=self.photoimgRight)
        frameLabelRight.place(x=5, y=0, width=710, height=70)
        
        
        # #########################  Table Frame Creation #######3Usually lacks ,text=" "===================================
        
        tableFrame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        tableFrame.place(x=5, y=160, width=710, height=350)
        #Scroll Bar\
        scroll_x=ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableFrame,orient=VERTICAL)
        self.attendanceReport=ttk.Treeview(tableFrame,column=("empID","name","dep","time","date","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        
        #too move the scroll bar===============================
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)
        
        #Table heading=========================================================
        self.attendanceReport.heading("empID",text="Attendance ID")
        self.attendanceReport.heading("name",text="Name")
        self.attendanceReport.heading("dep",text="Department")
        self.attendanceReport.heading("time",text="Time")
        self.attendanceReport.heading("date",text="Date")
        self.attendanceReport.heading("status",text="Attendance Status")
        self.attendanceReport["show"]="headings"

        #Table columns==========================================================================
        self.attendanceReport.column("empID", width=100)
        self.attendanceReport.column("name", width=100)
        self.attendanceReport.column("dep",width=100)
        self.attendanceReport.column("time",width=100)
        self.attendanceReport.column("date",width=100)
        self.attendanceReport.column("status",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor)#========Gets  data for showing on the right window
        #self.fetchData()  #===================================
        
        
        #delete_btn=Button(right_frame,text="Delete", cursor="hand2",command=self.delete_data,font=("times new roman", 10, "bold"),width=10,bg="red",fg="white")
        #delete_btn.place(x=250,y=520)
        
        back_btn=Button(right_frame, text="Back", command=self.back_button,font=("times new roman", 10, "bold"), cursor="hand2",width=10,bg="red", fg="white")
        back_btn.place(x=390,y=520)
        
        
        
        
        
        
        #===============================Fetch data=================================   
        pass
    
    def fetchData(self,rows):
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:  
            self.attendanceReport.insert("",END,values=i)
            
            pass
        pass
    def import_csv(self):
         global mydata
         mydata.clear()
         flnm=filedialog.askopenfilename(initialdir=os.getcwd(),title="Save Csv",filetypes=(("All Files","*.*"),("CSV Files",'*.csv')),parent=self.root)
         with open(flnm) as myfile:
             csvread=csv.reader(myfile,delimiter=",")
             for i in csvread:
                 mydata.append(i)
             self.fetchData(mydata)
             
             pass
         pass
    def exportCsv(self):
         
         try:
             if len(mydata)<1:
                 messagebox.showerror("No Data","Data Absent for Export",parent=self.root)
                 return False
             flnm=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV Files",'*.csv'),("All Files","*.*")),parent=self.root)
         
             with open(flnm,mode="w",newline="") as myfile:
                 exp_write=csv.writer(myfile,delimiter=",")
                 for i in mydata:
                     exp_write.writerow(i)
                     
                 messagebox.showinfo("Success","Exported Csv Data to "+os.path.basename(flnm)+" Successfully")
         except Exception as h:
             messagebox.showerror("Error",f"Due to : {str(h)}",parent=self.root)
            
     #================get cursor=========================  
    def get_cursor(self,event=""):
        cursor_focus=self.attendanceReport.focus()
        content=self.attendanceReport.item(cursor_focus)
        data=content["values"]
        
        
        self.var_empID.set(data[0])
        self.var_name.set(data[1])
        self.var_dep.set(data[2])
        self.var_time.set(data[3])
        self.var_date.set(data[4])
        self.var_status.set(data[5]) 
        
    def back_button(self):
        #self.facerecog_window=Toplevel(self.root)
        #importlib.reload(FaceRecog)
        self.obj=main.FaceRecognition(self.root)  
        
        pass
    def reset_fields(self):
        # Clear all entry fields and set comboboxes to default values
        self.var_empID.set("")                       
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("Status")
        
        
        pass
        
    
if __name__ == "__main__":
    
    root = Tk()
    obj = Attendance(root)
    root.mainloop()