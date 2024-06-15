"""from kivy.uix.filechooser import string_types
from kivy.uix.screenmanager import NoTransition
from kivy.uix.actionbar import DropDown"""
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



class User:
     def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("User Details")
        
        #=============Variables===================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_title=StringVar()
        self.var_gender=StringVar()
        self.var_class=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_dob=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
        #Bg Image
        img = Image.open("Maureen.jpg")
        img = img.resize((1530, 1200))
        self.photoimg = ImageTk.PhotoImage(img)
            
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=50, width=1530, height=1000)
            
                    
        title_lbl = Label(bg_img, text="User Details System", font=("times new roman", 25, "bold"), bg="Yellow", fg="Green")
        title_lbl.place(x=0, y=0, width=1530, height=40)
        
        main_frame = Frame(bg_img, bd=2, bg="grey")
        main_frame.place(x=10, y=55, width=1500, height=720)

        ####################### Left label frame()
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="User Details", font=("times new roman", 10, "bold"))
        Left_frame.place(x=10, y=10, width=725, height=580)

        imgLeft = Image.open("Christine1.jpg")
        imgLeft = imgLeft.resize((720, 100))
        self.photoimgLeft = ImageTk.PhotoImage(imgLeft)

        frameLabelLeft = Label(Left_frame, image=self.photoimgLeft)
        frameLabelLeft.place(x=5, y=0, width=710, height=70)

        # #########################  Current course
        current_courseFrame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 10, "bold"))
        current_courseFrame.place(x=5, y=65, width=710, height=130)
        
        #Create a DEPARTMENT  dropdown ======================================= 

        departmentLabel = Label(current_courseFrame, text="Department", font=("times new roman", 10, "bold"))
        departmentLabel.grid(row=0, column=0,pady=3,sticky=W)
            
        #departmentCombo()
        self.departmentCombo = ttk.Combobox(current_courseFrame,textvariable=self.var_dep ,font=("times new roman", 10, "bold"), state="readonly")
        self.departmentCombo["values"] = ("Select Department", "Data", "IT", "Civil", "Mechanical")
        self.departmentCombo.current(0)
        self.departmentCombo.grid(row=0, column=1,pady=3, sticky=W)

        ###############3Create a COURSES  dropdown  ===============================

        courseLabel = Label(current_courseFrame, text="Course", font=("times new roman", 10, "bold"))
        courseLabel.grid(row=0, column=2, pady=3, sticky=W)
                
        #itemsC=["Select Course", "FE", "AST", "TE", "BE"]
        #selected_itemC=tk.StringVar()
        #courseCombo=ttk.Combobox(root,textvariable=selected_itemC,values=itemsC)
        #courseCombo.pack()

        #def on_select(event):
        #    print(selected_itemC.get())
                        
        #courseCombo.bind("<<ComboboxSelected>>",on_select)

        self.courseCombo = ttk.Combobox(current_courseFrame,textvariable=self.var_course ,font=("times new roman", 10, "bold"), state="readonly")
        self.courseCombo["values"] = ("Select Course", "DS", "IT", "CE", "ME")
        self.courseCombo.current(0)
        self.courseCombo.grid(row=0, column=3, pady=3, sticky=W)

        ##Combo creation complete
                    
        #Years DropDown===============================
        yearLabel = Label(current_courseFrame, text="Year", font=("times new roman", 10, "bold"))
        yearLabel.grid(row=1, column=0,pady=3, sticky=W)
        
        self.yearCombo = ttk.Combobox(current_courseFrame,textvariable=self.var_year ,font=("times new roman", 10, "bold"), state="readonly")
        self.yearCombo["values"] = ("Select Year ", "One","Two","Three","Four")
        self.yearCombo.current(0)
        self.yearCombo.grid(row=1, column=1, pady=3, sticky=W)   
         
        #Semester========================================
        semesterLabel = Label(current_courseFrame, text="Semester", font=("times new roman", 10, "bold"))
        semesterLabel.grid(row=1, column=2, pady=3,sticky=W)
        
        self.semesterCombo = ttk.Combobox(current_courseFrame, textvariable=self.var_sem,font=("times new roman", 10, "bold"), state="readonly")
        self.semesterCombo["values"] = ("Select Semester", "One","Two","Three","Four")
        self.semesterCombo.current(0)
        self.semesterCombo.grid(row=1, column=3, pady=3, sticky=W)    
        
        
        # #########################  Class Student Information/Frame====================
        
        studentInfoFrame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student Details Information", font=("times new roman", 10, "bold"))
        studentInfoFrame.place(x=5, y=200, width=710, height=400)
        
        #Student ID=======================
        idLabel = Label(studentInfoFrame, text="Student ID: ", font=("times new roman", 10, "bold"))
        idLabel.grid(row=0, column=0,pady=3,sticky=W)
        idEntry=Entry(studentInfoFrame,width=20, textvariable=self.var_id,font=("times new roman", 10, "bold"))           
        idEntry.grid(row=0, column=1,pady=3,sticky=W) 
        
        #Student Name===========================
        nameLabel = Label(studentInfoFrame, text="Student Name: ", font=("times new roman", 10, "bold"))
        nameLabel.grid(row=0, column=2,pady=3,sticky=W)
        nameEntry=Entry(studentInfoFrame,width=20,textvariable=self.var_name, font=("times new roman", 10, "bold"))           
        nameEntry.grid(row=0, column=3,pady=3,sticky=W)   
        
        
        
        #Gender====================================
        genderLabel = Label(studentInfoFrame, text="Gender", font=("times new roman", 10, "bold"))
        genderLabel.grid(row=1, column=0,pady=3,sticky=W)
        self.genderCombo = ttk.Combobox(studentInfoFrame, textvariable=self.var_gender,font=("times new roman", 10, "bold"), state="readonly")
        self.genderCombo["values"] = ("Select Gender", "Male","Female")
        self.genderCombo.current(0)
        self.genderCombo.grid(row=1, column=1, pady=3, sticky=W)  
        
        
        
        
        #DOB=========================================================
        dobLabel = Label(studentInfoFrame, text="Date of Birth: ", font=("times new roman", 10, "bold"))
        dobLabel.grid(row=1, column=2,pady=3,sticky=W)
        dobEntry=Entry(studentInfoFrame,width=20,textvariable=self.var_dob, font=("times new roman", 10, "bold"))           
        dobEntry.grid(row=1, column=3,pady=3,sticky=W)  
        
        #Email========================================================
        emailLabel = Label(studentInfoFrame, text="Email Address: ", font=("times new roman", 10, "bold"))
        emailLabel.grid(row=2, column=0,pady=3,sticky=W)
        emailLabelEntry=Entry(studentInfoFrame,width=20, textvariable=self.var_email,font=("times new roman", 10, "bold"))           
        emailLabelEntry.grid(row=2, column=1,pady=3,sticky=W)   
        
        #Phone Number=======================================================
        phoneLabel = Label(studentInfoFrame, text="Phone Number: ", font=("times new roman", 10, "bold"))
        phoneLabel.grid(row=2, column=2,pady=3,sticky=W)
        phoneEntry=Entry(studentInfoFrame,width=20, font=("times new roman", 10, "bold"),textvariable=self.var_phone)           
        phoneEntry.grid(row=2, column=3,pady=3,sticky=W) 
          
        #Address=====================================================
        addressLabel = Label(studentInfoFrame, text="Address : ", font=("times new roman", 10, "bold"))
        addressLabel.grid(row=3, column=0,pady=3,sticky=W)
        addressLabelEntry=Entry(studentInfoFrame,width=20, font=("times new roman", 10, "bold"),textvariable=self.var_address)           
        addressLabelEntry.grid(row=3, column=1,pady=3,sticky=W)  
        
        
        #Teacher Name==================================================
        trLabel = Label(studentInfoFrame, text="Teacher Name: ", font=("times new roman", 10, "bold"))
        trLabel.grid(row=3, column=2,pady=3,sticky=W)
        trLabelEntry=Entry(studentInfoFrame,width=20, font=("times new roman", 10, "bold"),textvariable=self.var_teacher)           
        trLabelEntry.grid(row=3, column=3,pady=3,sticky=W)  
         
        #====================RADIO BUTTONS ############33==============================
        
        
        self.var_radio1=StringVar()
        
        radiobtn1=ttk.Radiobutton(studentInfoFrame,text="Take Photo Sample",value="Yes",variable=self.var_radio1)
        radiobtn1.grid(row=4,column=0)
        
        
        radiobtn2=ttk.Radiobutton(studentInfoFrame, text="No Photo Sample",value="No",variable=self.var_radio1)
        radiobtn2.grid(row=4,column=1)
        
        
        #######################3Buttons Frame=================================
        
        
        btn_frame=Frame(studentInfoFrame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=720,height=35)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data, cursor="hand2", font=("times new roman", 10, "bold"),width=15,bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=4)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data, cursor="hand2",font=("times new roman", 10, "bold"),width=15,bg="green",fg="white")
        update_btn.grid(row=0,column=1,padx=4)
        
        delete_btn=Button(btn_frame,text="Delete", cursor="hand2",command=self.delete_data,font=("times new roman", 10, "bold"),width=15,bg="red",fg="white")
        delete_btn.grid(row=0,column=2,padx=4)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_fields, cursor="hand2",font=("times new roman", 10, "bold"),width=15,bg="grey",fg="white")
        reset_btn.grid(row=0,column=3,padx=4)
        
        ###########
        btn_frame1=Frame(studentInfoFrame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=280,width=720,height=35)
        
        takePhoto_btn=Button(btn_frame1,text="Take Photo Sample",font=("times new roman", 10, "bold"), 
                             cursor="hand2",width=30,bg="violet",fg="white", command=self.take_photo_sample)
        takePhoto_btn.grid(row=0,column=0,padx=4)
        
        updatePhoto_btn=Button(btn_frame1,text="Update Photo Sample", cursor="hand2",command=self.update_photo_sample,
                               font=("times new roman", 10, "bold"),width=30,bg="indigo",fg="white")
        updatePhoto_btn.grid(row=0,column=1,padx=4)
        
        #=======
        
        
        #########333# Right label frame()======================================================
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="User Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=740, y=10, width=720, height=600)
        
        imgRight = Image.open("Maureen.jpg")
        imgRight = imgRight.resize((720, 100))
        self.photoimgRight = ImageTk.PhotoImage(imgRight)
        
        frameLabelRight = Label(right_frame, image=self.photoimgRight)
        frameLabelRight.place(x=5, y=0, width=710, height=70)
        
        
        #=========Search System===============================================================
        # #########################  Search  Student Information
        searchInfoFrame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 10, "bold"))
        searchInfoFrame.place(x=5, y=80, width=710, height=70)
        
        searchLabel = Label(searchInfoFrame, text="Search By: ", font=("times new roman", 10, "bold"),bg="red",fg="white")
        searchLabel.grid(row=0, column=0,padx=4, pady=3,sticky=W)
        
        self.searchCombo = ttk.Combobox(searchInfoFrame, font=("times new roman", 10, "bold"), state="readonly")
        self.searchCombo["values"] = ("Select","Phone_No","Student_ID")
        self.searchCombo.current(0)
        self.searchCombo.grid(row=0, column=1,padx=4, pady=3,sticky=W)
        
        
        self.searchLabel=StringVar()
        
        searchLabelEntry=Entry(searchInfoFrame,width=20,textvariable=self.searchLabel ,font=("times new roman", 10, "bold"))           
        searchLabelEntry.grid(row=0, column=2,pady=3,sticky=W)
        
        search_btn=Button(searchInfoFrame,text="Search",command=self.search_data,font=("times new roman", 10, "bold"),width=9,bg="red",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showall_btn=Button(searchInfoFrame,text="Show All",command=self.show_all_data,font=("times new roman", 10, "bold"),width=9,bg="grey",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)
        
        back_btn=Button(right_frame, text="Return", cursor="hand2", command=self.back_button,font=("times new roman", 10, "bold"), width=10,bg="blue", fg="white")
        back_btn.place(x=400,y=550)
        
        
        
        
        # #########################  Table Frame Creation ######
        # Usually lacks ,text=" "===================================
        
        tableFrame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        tableFrame.place(x=5, y=160, width=710, height=320)
        
        
        
        
        #Scroll Bar\
        scroll_x=ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableFrame,orient=VERTICAL)
        self.userTable=ttk.Treeview(tableFrame,column=("dep","course","year","sem","id","name","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        
        
        
        
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        
        #too move the scroll bar===============================
        scroll_x.config(command=self.userTable.xview)
        scroll_y.config(command=self.userTable.yview)
        
        #Table heading=========================================================
        self.userTable.heading("dep",text="Department")
        self.userTable.heading("course",text="Course")
        self.userTable.heading("year",text="Year")
        self.userTable.heading("sem",text="Semester")
        self.userTable.heading("id",text="ID")
        self.userTable.heading("name",text="Name")
        self.userTable.heading("gender",text="Gender")
        self.userTable.heading("dob",text="DOB")
        self.userTable.heading("email",text="Email")
        self.userTable.heading("phone",text="Phone")
        self.userTable.heading("address",text="Address")
        self.userTable.heading("teacher",text="Teacher")
        self.userTable.heading("photo",text="PhotoSampleStatus")
        self.userTable["show"]="headings"
        
        #Table columns==========================================================================
        self.userTable.column("dep", width=100)
        self.userTable.column("course", width=100)
        self.userTable.column("year", width=100)
        self.userTable.column("sem",width=100)
        self.userTable.column("id",width=100)
        self.userTable.column("name",width=100)
        self.userTable.column("gender",width=100)
        self.userTable.column("dob",width=100)
        self.userTable.column("email",width=100)
        self.userTable.column("phone",width=100)
        self.userTable.column("address",width=100)
        self.userTable.column("teacher",width=100)
        self.userTable.column("photo",width=150)
        
        self.userTable.pack(fill=BOTH,expand=1)
        self.userTable.bind("<ButtonRelease>",self.get_cursor)#========Gets  data for showing on the right window
        self.fetch_data()  #===========================================This holds the sql statement to achieve a similar objective as the above code
        
        
        
        
     #========================Function Declaration===================
     
     def add_data(self):
             
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
             messagebox.showerror("Error","Fill all fields",parent=self.root)
        else:
            try: 
                conn=mysql.connector.connect(host="localhost", user="root", passwd="programmer1.", database="facialrecognition",auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute('''CREATE TABLE IF NOT EXISTS userdetails (
                                    id INTEGER PRIMARY KEY,
                                    dep TEXT,
                                    course TEXT,
                                    year TEXT,
                                    sem TEXT,
                                    id TEXT,
                                    name TEXT,
                                    gender TEXT,
                                    dob TEXT,
                                    email TEXT,
                                    phone TEXT,
                                    address TEXT,
                                    teacher TEXT,
                                    photo TEXT
                                )''')
                conn.commit()
                my_cursor.execute("INSERT INTO userdetails VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (
                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_id.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get()   ))
                
                
                conn.commit()
                self.fetch_data()
                conn.close()
                
                messagebox.showinfo("Success","Welcome, Code with Onyango Joel Harold",parent=self.root)
                
            except Exception as e:
                messagebox.showerror("Error", f"Due To : {str(e)}",parent=self.root)
                
            
     #===============================Fetch data=================================   
     

     

     def connect_to_database(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="programmer1.",
                database="facialrecognition",
                auth_plugin='mysql_native_password'  # Specify the authentication plugin
            )
            if conn.is_connected():
                print("Successfully connected to the database")
                return conn
            else:
                print("Failed to connect to the database")
        except Exception as err:
            print(f"Error: {err}")
            messagebox.showerror("Error", f"Database connection failed: {err}")

     # Usage example
     def fetch_data(self):
        conn = self.connect_to_database()
        if conn:
            try:
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM userdetails")
                data = my_cursor.fetchall()
                if data:
                    self.userTable.delete(*self.userTable.get_children())
                    for row in data:
                        self.userTable.insert("", END, values=row)
                conn.close()
            except Exception as err:
                print(f"Error: {err}")
                messagebox.showerror("Error", f"Error fetching data: {err}")


        
     def get_cursor(self, event=""):
        cursor_focus = self.userTable.focus()
        content = self.userTable.item(cursor_focus)
        data = content["values"]

        # Ensure data is not empty and has the expected number of elements
        if not data or len(data) < 13:
            print("Data is empty or does not have the expected structure.")
            return

        # Set variables if data contains sufficient elements
        try:
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_sem.set(data[3])
            self.var_id.set(data[4])
            self.var_name.set(data[5])
            self.var_gender.set(data[6])
            self.var_dob.set(data[7])
            self.var_email.set(data[8])
            self.var_phone.set(data[9])
            self.var_address.set(data[10])
            self.var_teacher.set(data[11])
            self.var_radio1.set(data[12]) 
        except IndexError as e:
            print(f"IndexError: {e}")

        
    
    #========================================update function============
     def update_data(self):
        
            try:
                Uupdate = messagebox.askyesno("Update", "Do you want to update user details?", parent=self.root)
                if Uupdate:
                    conn = mysql.connector.connect(host="localhost", user="root", passwd="programmer1.", database="facialrecognition", auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()

                    # Corrected the SQL query to include the WHERE clause
                    my_cursor.execute("""
                        UPDATE userdetails SET
                            dep = %s,
                            course = %s,
                            year = %s,
                            sem = %s,
                            id=%s,
                            name = %s,
                            gender = %s,
                            dob = %s,
                            email = %s,
                            phone = %s,
                            address = %s,
                            teacher = %s,
                            photo = %s
                        WHERE id = %s
                    """  , (
                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_id.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get(),
                                                                                            self.var_id.get() ))

                    conn.commit()
                    messagebox.showinfo("Success", "User details updated successfully", parent=self.root)
                    self.fetch_data()
                else:
                    return
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)
            finally:
                if conn.is_connected():
                    conn.close()

    # Function to delete data
     def delete_data(self):
        try:
            # Get the ID of the selected user
            selected_id = self.var_id.get()
            if selected_id == "":
                messagebox.showerror("Error", "Select a user to delete", parent=self.root)
                return

            # Confirmation message
            confirmation = messagebox.askyesno("Delete", "Are you sure you want to delete this user?", parent=self.root)
            if confirmation:
                # Connect to the database
                conn = mysql.connector.connect(host="localhost", user="root", passwd="programmer1.", database="facialrecognition",auth_plugin='mysql_native_password' )
                my_cursor = conn.cursor()

                # Delete the user from the database
                my_cursor.execute("DELETE FROM userdetails WHERE id=%s", (selected_id,))
                conn.commit()

                # Display success message and update the table
                messagebox.showinfo("Success", "User deleted successfully", parent=self.root)
                self.fetch_data()

                # Close the connection
                conn.close()
                self.fetch_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting user: {str(e)}", parent=self.root)

    # Function to reset fields
     def reset_fields(self):
         
         
        # Clear all entry fields and set comboboxes to default values
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_gender.set("Select Gender")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_dob.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")





    
     def take_photo_sample(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "Fill all fields", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="programmer1.",
                    database="facialrecognition",
                    auth_plugin='mysql_native_password'
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM userdetails WHERE id=%s", (self.var_id.get(),))
                myresult = my_cursor.fetchall()

                if not myresult:
                    messagebox.showerror("Error", "User not found in the database", parent=self.root)
                    return

                user_id = self.var_id.get()

                # Update the user's details
                my_cursor.execute("""
                    UPDATE userdetails SET
                        dep = %s,
                        course = %s,
                        year = %s,
                        sem = %s,
                        name = %s,
                        gender = %s,
                        dob = %s,
                        email = %s,
                        phone = %s,
                        address = %s,
                        teacher = %s,
                        photo = %s
                    WHERE id = %s
                """, (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    user_id
                ))

                conn.commit()
                self.fetch_data()
                self.reset_fields()
                conn.close()

                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(
                        gray,
                        scaleFactor=1.1,
                        minNeighbors=10,
                        minSize=(60, 60)
                    )
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                    return None

                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, myframe = cap.read()
                    if not ret:
                        messagebox.showerror("Error", "Failed to capture image from camera", parent=self.root)
                        break

                    cropped_face = face_cropped(myframe)
                    if cropped_face is not None:
                        img_id += 1
                        face_ = cv2.resize(cropped_face, (400, 400))
                        face_ = cv2.cvtColor(face_, cv2.COLOR_BGR2GRAY)

                        file_path = r"D:\Documents\Apps\FacialRecognition\data\user." + str(user_id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_path, face_)
                        cv2.putText(face_, f"user.{user_id}.{img_id}", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face_)

                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generated data sets compiled", parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", f"Error capturing photo sample: {str(e)}")


     def update_photo_sample(self):
            try:
                # Similar to capturing, open the webcam
                cap = cv2.VideoCapture(0)

                if not cap.isOpened():
                    raise Exception("Unable to access the webcam.")

                ret, frame = cap.read()

                if ret:
                    cv2.imshow("Update Photo Sample", frame)
                    file_path = "updated_photo_sample.jpg"
                    cv2.imwrite(file_path, frame)
                    cap.release()
                    cv2.destroyAllWindows()

                    # Update the photo sample status variable or field in your GUI
                    self.var_radio1.set("Yes")
                    messagebox.showinfo("Success", "Photo sample updated successfully.")
                else:
                    messagebox.showerror("Error", "Failed to update photo sample.")

            except Exception as e:
                messagebox.showerror("Error", f"Error updating photo sample: {str(e)}")
                
     def search_data(self):
            try:
                search_by = self.searchCombo.get()
                search_value = self.searchLabel.get()

                if search_by == "Select" or search_value == "":
                    messagebox.showerror("Error", "Select search criteria and enter search value.")
                else:
                    conn = mysql.connector.connect(host="localhost", user="root", passwd="programmer1.", database="facialrecognition",auth_plugin='mysql_native_password' )
                    my_cursor = conn.cursor()

                    # Constructing the SQL query based on search criteria ie, ID, Roll No or  Phone Number
                    
                    if search_by == "Phone_No":
                        query = f"SELECT * FROM userdetails WHERE Phone LIKE '%{search_value}%'"
                    elif search_by == "Student_ID":
                        query = f"SELECT * FROM userdetails WHERE ID LIKE '%{search_value}%'"

                    my_cursor.execute(query)
                    data = my_cursor.fetchall()

                    if data:
                        self.userTable.delete(*self.userTable.get_children())
                        for record in data:
                            self.userTable.insert("", END, values=record)
                    else:
                        messagebox.showinfo("No Results", "No matching records found.")

                    conn.close()

            except Exception as e:
                messagebox.showerror("Error", f"Error searching data: {str(e)}")



     def back_button(self):
            #self.new_window=Toplevel(self.root)
            self.obj=main.FaceRecognition(self.root)
            
     def show_all_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", passwd="programmer1.", database="facialrecognition",auth_plugin='mysql_native_password' )
            my_cursor = conn.cursor()

            my_cursor.execute("SELECT * FROM userdetails")
            data = my_cursor.fetchall()

            if data:
                self.userTable.delete(*self.userTable.get_children())
                for record in data:
                    self.userTable.insert("", END, values=record)
            else:
                messagebox.showinfo("No Data", "No records found in the database.")

            conn.close()

        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {str(e)}")

              
            
                     

if __name__ == "__main__":
    
    root = Tk()
    obj = User(root)
    root.mainloop()
    
