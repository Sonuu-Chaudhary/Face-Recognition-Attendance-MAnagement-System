from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox

import cv2
import os
import numpy as np



class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x780+0+0")
        self.root.title("Face Recognition Attendance System")

        titleLable = Label(self.root, text="Train Data Set", font=("times new roman", 25, "bold"), bg="white", fg="blue")
        titleLable.place(x=0, y=0, width=1370, height=40)

        ##BACK    

        backBtn = Button(self.root,command=self.HomePage, text="Home" , cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="red", activebackground="blue")
        backBtn.place(x=0, y=0, width=110, height=50)

        imgTop = Image.open(r"D:\Attendance System Project\Downloaded Image\temp2.jpg")
        imgTop = imgTop.resize((1350,280), Image.LANCZOS)
        self.photoimageTop = ImageTk.PhotoImage(imgTop)

        f_lable = Label(self.root,image=self.photoimageTop)
        f_lable.place(x=0, y=55, width=1350, height=280)
        ##Button

        buttn1Title = Button(self.root, text="Train Data" , command=self.trainClassifier, cursor="hand2", font=("times new roman", 25, "bold"), bg="darkblue", fg="white")
        buttn1Title.place(x=0, y=340, width=1350, height=50) 
 

        imgBottom = Image.open(r"D:\Attendance System Project\Downloaded Image\Photos.jpg")
        imgBottom = imgBottom.resize((1350,280), Image.LANCZOS)
        self.photoimageBottom = ImageTk.PhotoImage(imgBottom)

        f_lable = Label(self.root,image=self.photoimageBottom)
        f_lable.place(x=0, y=400, width=1350, height=280)

    def trainClassifier(self):
        dataDir=("data")
        path=[os.path.join(dataDir, file) for file in os.listdir(dataDir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        ## Train Classifier=======

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces,ids)
        recognizer.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset complete")

    def HomePage(self):
        from main import FaceRecognitionSystem
        self.new_Window=Toplevel(self.root)
        self.app=FaceRecognitionSystem(self.new_Window)









       





if __name__ == "__main__" :
    root = Tk()
    obj = Train(root)
    root.mainloop()
