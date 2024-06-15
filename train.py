
#import UserDetailsButton
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # Import ttk separately
from PIL import Image, ImageTk
import cv2
import main
import importlib
import os
import numpy as np

class TrainButton:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data ")
        
        #Bg Image
        imgbg=Image.open("Christine1.jpg")
        imgbg=imgbg.resize((1530,780))
        self.photoimg=ImageTk.PhotoImage(imgbg)
        
        bgnd_img=Label(self.root,image=self.photoimg)
        bgnd_img.place(x=0,y=0,relwidth=1,height=790)
        
        
        top_frame = LabelFrame(self.root, bd=2, bg="purple",fg="gray", relief=RIDGE, text="Train Data", font=("times new roman", 10, "bold"))
        top_frame.place(x=0, y=10, relwidth=1, height=90)
        
        top_lbl=Label(top_frame,text="\t \t Train Data Page \t \t  ", font=("times new roman",25,"bold"), \
                    bg="grey",fg="gold")
        top_lbl.place(x=0,y=0)
        
        
        
        back_btn=Button(top_frame, text="Back", command=self.back_button,font=("times new roman", 10, "bold"), cursor="hand2",width=10,bg="red", fg="white")
        back_btn.place(x=1000,y=10)
        
        train_btn=Button(top_frame, text="TRAIN DATA", command=self.train_classifier,font=("tahoma", 15, "bold"), cursor="hand2",width=10,bg="gold", fg="black")
        train_btn.place(x=1100,y=10)
        
    def back_button(self):
        #self.facerecog_window=Toplevel(self.root)
        #importlib.reload(FaceRecog)
        self.obj=main.FaceRecognition(self.root)
        
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces_=[]
        ids_=[]
        
        for image in path:
            img=Image.open(image).convert("L") #GrayScaleImage
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces_.append(imageNp)
            ids_.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids_=np.array(ids_)
        
        
        #==================== Train the Classsifier ==================================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces_,ids_)
        clf.write("classifier.xml")
        cv2.destroyAllWindows
        
        messagebox.showinfo("Result","Training Data Completed :-D")
        
        
        
        """                        """
        """                        """
        """                        """

#def back_button(self)""  D:\Documents\Apps\FacialRecognition\data\user.7.1.jpg
 
    
    
    
if __name__=="__main__":
        
    root=Tk()
    obj=TrainButton(root)
    root.mainloop()

