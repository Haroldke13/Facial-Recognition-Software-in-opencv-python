import train
#import UserDetailsButton
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # Import ttk separately
from PIL import Image, ImageTk
import mysql.connector
import cv2
import main
import importlib
import os
import numpy as np
import pymysql
from time import strftime
from datetime import datetime

class Facial_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Data ")
        
        top_frame = LabelFrame(self.root, bd=2, bg="purple",fg="gray", relief=RIDGE, text="Recognize Face", font=("times new roman", 10, "bold"))
        top_frame.place(x=0, y=0, relwidth=1, height=90)
        
        top_lbl=Label(top_frame,text="Recognize Face", font=("times new roman",20,"bold"), \
                    bg="grey",fg="gold")
        top_lbl.place(x=0,y=0, relwidth=1)
        
        
        lower_frame = LabelFrame(self.root, bd=2, relief=SUNKEN,bg="lightgray", text="Recognize Face Buttons", font=("times new roman", 10, "bold"))
        lower_frame.place(x=0, y=90,relwidth=1,height=700)
        
        
        lower_lbl=Label(lower_frame,text="Recognize Face", font=("times new roman",13,"bold"), \
                    bg="grey",fg="gold")
        lower_lbl.place(x=0,y=0, relwidth=1)
        
        img_=Image.open("Christine1.jpg")
        img_=img_.resize((200,800))
        self.photoimg=ImageTk.PhotoImage(img_)
        
        lf_img=Label(lower_frame,image=self.photoimg)
        lf_img.place(x=0,y=0,width=200,relheight=1)
        
        img2=Image.open("Christine1.jpg")
        img2=img2.resize((200,800))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lf_img2=Label(lower_frame,image=self.photoimg2)
        lf_img2.place(x=1350,y=0,width=200,relheight=1)
        
        
        back_btn=Button(top_frame, text="Back", command=self.back_button,font=("times new roman", 10, "bold"), cursor="hand2",width=10,bg="red", fg="white")
        back_btn.place(x=1300,y=10)
        
        
        recogface_btn=Button(lower_frame, text="RECOGNIZE FACE", command=self.face_recog,font=("times new roman", 15, "bold"), cursor="hand2",bg="purple", fg="gold")
        recogface_btn.place(x=500,y=500)
        
        
    def back_button(self):
        #self.facerecog_window=Toplevel(self.root)
        #importlib.reload(FaceRecog)
        self.obj=main.FaceRecognition(self.root)
        
    #Attendance=================================================    
        
    def mark_attendance(self,i,n,d):
        with open("harold.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if ((i not in name_list ) and (d not in name_list ) and (n not in name_list ) 
                ):
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n {i},{n},{d},{dtString},{d1},Preset")
    
    
    #Recognize face=================================================    
        


    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="programmer1.",
                    database="facialrecognition",
                    auth_plugin='mysql_native_password'
                )
                cursor_conn = conn.cursor()

                cursor_conn.execute("SELECT name FROM userdetails WHERE id=%s", (id,))
                n = cursor_conn.fetchone()
                n = '+'.join(n) if n else "Unknown"

                

                cursor_conn.execute("SELECT dep FROM userdetails WHERE id=%s", (id,))
                d = cursor_conn.fetchone()
                d = '+'.join(d) if d else "Unknown"

                cursor_conn.execute("SELECT id FROM userdetails WHERE id=%s", (id,))
                i = cursor_conn.fetchone()
                i = '+'.join(i) if i else "Unknown"

                if confidence > 86:
                    
                    cv2.putText(img, f"Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep: {d}", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"ID: {i}", (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(n,d,i)
                else:
                    cv2.putText(img, "Unknown Face", (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 0), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(r"D:\Documents\Apps\FacialRecognition\haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key to break
                break

        video_cap.release()
        cv2.destroyAllWindows()

               
    
if __name__=="__main__":
        
    root=Tk()
    obj=Facial_Recognition(root)
    root.mainloop()


