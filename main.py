from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import tkinter as tk
import os
from faceRecognition import FaceDetection
from train import Train
from attendance import Attendance
from developer import Developer
from helpdesk import HelpDesk
from tkinter import messagebox
from time import strftime
from datetime import datetime
from tkinter import Label


class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x780+0+0")
        self.root.title("Face Recognition Attendance System")




# 1st Image
        img1 = Image.open(r"D:\Attendance System Project\Downloaded Image\temp1.jpg")
        img1 = img1.resize((500,130), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img1)
        f_lable = Label(self.root,image=self.photoimage)
        f_lable.place(x=0, y=0, width=500, height=130)

# 2nd Image 

        img2 = Image.open(r"D:\Attendance System Project\Downloaded Image\temp2.jpg")
        img2 = img2.resize((500,130), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        f_lable = Label(self.root,image=self.photoimage2)
        f_lable.place(x=450, y=0, width=500, height=130)

# 3rd image 

        img3 = Image.open(r"D:\Attendance System Project\Downloaded Image\temp3.jpg")
        img3 = img3.resize((500,130), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        f_lable = Label(self.root,image=self.photoimage3)
        f_lable.place(x=900, y=0, width=500, height=130)

# Background Image
        
        BgImage = Image.open(r"D:\Attendance System Project\Downloaded Image\BgImage.jpg")
        BgImage = BgImage.resize((1370,580), Image.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(BgImage)
        bg_lable = Label(self.root,image=self.photoimage4)
        bg_lable.place(x=0, y=130, width=1370, height=580)


        titleLable = Label(bg_lable, text="Face Recognition Attendance System", font=("times new roman", 25, "bold"), bg="black", fg="red")
        titleLable.place(x=0, y=0, width=1370, height=40)

        def time():
            string =strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        lbl = Label(titleLable, font=('times new roman', 14, 'bold'), background='white', foreground='red')
        lbl.place(x=0, y=0, width=110, height=50)
        time()


#1 1 1 1 1 1 1 1 1

        img5 = Image.open(r"D:\Attendance System Project\Downloaded Image\Students.jpg")
        img5 = img5.resize((200,200), Image.LANCZOS)
        self.photoimage5 = ImageTk.PhotoImage(img5)
        buttn1 = Button(bg_lable, image=self.photoimage5,command=self.open_student_page, cursor="hand2")
        buttn1.place(x=50, y=50, width=200, height=150)

        buttn1Title = Button(bg_lable, text="Student Details" , command=self.open_student_page, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        buttn1Title.place(x=50, y=200, width=200, height=50)   
        
        #2 2 2 2 2
        img6 = Image.open(r"D:\Attendance System Project\Downloaded Image\FaceDetector.jpg")
        img6 = img6.resize((200, 200), Image.LANCZOS)
        self.photoimage6 = ImageTk.PhotoImage(img6)
        buttn2 = Button(bg_lable, image=self.photoimage6, cursor="hand2", command=self.face_Data)
        buttn2.place(x=400, y=50, width=200, height=150)

        buttn1Title2 = Button(bg_lable, text="Face Detector", cursor="hand2", command=self.face_Data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        buttn1Title2.place(x=400, y=200, width=200, height=50)

        #3 3 3 3 

        img7 = Image.open(r"D:\Attendance System Project\Downloaded Image\Attendance.jpg")
        img7 = img7.resize((200, 200), Image.LANCZOS)
        self.photoimage7 = ImageTk.PhotoImage(img7)
        buttn3 = Button(bg_lable, image=self.photoimage7, cursor="hand2", command=self.attendance_Data)
        buttn3.place(x=750, y=50, width=200, height=150)

        buttn1Title3 = Button(bg_lable, text="Attendance", cursor="hand2",command=self.attendance_Data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        buttn1Title3.place(x=750, y=200, width=200, height=50)

        #4 4 4 4 4 4 4 4 4
        img8 = Image.open(r"D:\Attendance System Project\Downloaded Image\HelpDesk.png")
        img8 = img8.resize((200, 200), Image.LANCZOS)
        self.photoimage8 = ImageTk.PhotoImage(img8)
        buttn4 = Button(bg_lable, image=self.photoimage8, cursor="hand2", command=self.help_Data)
        buttn4.place(x=1100, y=50, width=200, height=150)

        buttn1Title4 = Button(bg_lable, text="Help Desk", cursor="hand2",command=self.help_Data,  font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        buttn1Title4.place(x=1100, y=200, width=200, height=50)
        
        #5 5 5 5 5 5 5 5 5 5 5 5 5 5 
        img9 = Image.open(r"D:\Attendance System Project\Downloaded Image\Training.jpg")
        img9 = img9.resize((200, 200), Image.LANCZOS)
        self.photoimage9 = ImageTk.PhotoImage(img5)
        buttn5 = Button(bg_lable, image=self.photoimage9, cursor="hand2", command=self.train_Data)
        buttn5.place(x=50, y=325, width=200, height=150)

        buttn1Title5 = Button(bg_lable, text="Train Data", cursor="hand2",command=self.train_Data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        buttn1Title5.place(x=50, y=475, width=200, height=50)
        
        #6 6 6 6 6 6 6 6 6 6

        img10 = Image.open(r"D:\Attendance System Project\Downloaded Image\Photos.jpg")
        img10 = img10.resize((200,200), Image.LANCZOS)
        self.photoimage10 = ImageTk.PhotoImage(img10)
        buttn6 = Button(bg_lable, image=self.photoimage10, cursor="hand2", command=self.openImage)
        buttn6.place(x=400, y=325, width=200, height=150)

        buttn1Title6 = Button(bg_lable, text="Photos", cursor="hand2",command=self.openImage, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        buttn1Title6.place(x=400, y=475, width=200, height=50)

        # 7 7 7 7 7 7 7 7 7 7 7 7 7

        img11 = Image.open(r"D:\Attendance System Project\Downloaded Image\SoftwareDev.jpg")
        img11 = img11.resize((200, 200), Image.LANCZOS)
        self.photoimage11 = ImageTk.PhotoImage(img11)
        buttn7 = Button(bg_lable, image=self.photoimage11, cursor="hand2", command=self.dev_Data)
        buttn7.place(x=750, y=325, width=200, height=150)

        buttn1Title7 = Button(bg_lable, text="Developer", cursor="hand2",command=self.dev_Data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        buttn1Title7.place(x=750, y=475, width=200, height=50)

        # 8 8 8 8 8 8 8 8 8 8 8 8

        img12 = Image.open(r"D:\Attendance System Project\Downloaded Image\Exit.jpg")
        img12 = img12.resize((200, 200), Image.LANCZOS)
        self.photoimage12 = ImageTk.PhotoImage(img12)
        buttn8 = Button(bg_lable, image=self.photoimage12, cursor="hand2", command=self.iExit)
        buttn8.place(x=1100, y=325, width=200, height=150)

        buttn1Title8 = Button(bg_lable, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        buttn1Title8.place(x=1100, y=475, width=200, height=50)


        
    def openImage(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition", "Are you sure exit this project", parent=self.root)
        if self.iExit>0:
           self.root.destroy()
        else:
            return




    def open_student_page(self):
        # Function to open the Student page
        self.new_Window = Toplevel(self.root)
        self.app = Student(self.new_Window)

    def train_Data(self):
        self.new_Window=Toplevel(self.root)
        self.app=Train(self.new_Window)


    def face_Data(self):
        self.new_Window=Toplevel(self.root)
        self.app=FaceDetection(self.new_Window)

    def attendance_Data(self):
        self.new_Window=Toplevel(self.root)
        self.app=Attendance(self.new_Window)

    def dev_Data(self):
        self.new_Window=Toplevel(self.root)
        self.app=Developer(self.new_Window)

    def help_Data(self):
        self.new_Window=Toplevel(self.root)
        self.app=HelpDesk(self.new_Window)


    



   
   


















if __name__ == "__main__" :
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
      
    # Function Button

    
    

