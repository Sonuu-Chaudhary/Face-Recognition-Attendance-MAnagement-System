from tkinter import*
from PIL import Image, ImageTk






class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x780+0+0")
        self.root.title("Face Recognition Attendance System")

        img1 = Image.open(r"D:\Attendance System Project\Downloaded Image\Developer1.jpg")
        img1 = img1.resize((700,200), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img1)
        f_lable = Label(self.root,image=self.photoimage)
        f_lable.place(x=0, y=0, width=700, height=200)

# 2nd Image 

        img2 = Image.open(r"D:\Attendance System Project\Downloaded Image\Developer2.jpeg")
        img2 = img2.resize((700,200), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        f_lable = Label(self.root,image=self.photoimage2)
        f_lable.place(x=700, y=0, width=700, height=200)

        BgImage = Image.open(r"D:\Attendance System Project\Downloaded Image\DevBg.jpg")
        BgImage = BgImage.resize((1370,550), Image.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(BgImage)
        bg_lable = Label(self.root,image=self.photoimage4)
        bg_lable.place(x=0, y=200, width=1370, height=550)

        titleLable = Label(bg_lable, text="Developer", font=("times new roman", 25, "bold"), bg="white", fg="blue")
        titleLable.place(x=0, y=0, width=1370, height=40)
        ##Back
        backBtn = Button(titleLable,command=self.HomePage, text="Home" , cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="red", activebackground="blue")
        backBtn.place(x=0, y=0, width=110, height=50)



        ## DevFrame
        mainFrame = Frame(bg_lable, bd=2, bg="goldenrod1")
        mainFrame.place(x=670, y=45, width=660, height=440)

        AttIdLable = Label(mainFrame, text="MENTOR",font=("times new roman", 12, "bold"), bg="goldenrod1" )
        AttIdLable.grid(row=0, column=1, padx=5,pady=10, sticky=W)
        nameLable = Label(mainFrame, text="Dr. Jaspreeti Singh",font=("times new roman", 12, "bold"), bg="goldenrod1" )
        nameLable.grid(row=1, column=1, padx=5,pady=10, sticky=W)
        desigLable = Label(mainFrame, text="(Assistant Professor)",font=("times new roman", 12, "bold"), bg="goldenrod1" )
        desigLable.grid(row=2, column=1, padx=5,pady=10, sticky=W)


        AtIdLable = Label(mainFrame, text="                                        MENTEE",font=("times new roman", 12, "bold"), bg="goldenrod1" )
        AtIdLable.grid(row=0, column=6, padx=25,pady=10, sticky=W)
        namLable = Label(mainFrame, text="                                        Sonu Chaudhary",font=("times new roman", 12, "bold"), bg="goldenrod1" )
        namLable.grid(row=1, column=6, padx=25,pady=10, sticky=W)
        desiLable = Label(mainFrame, text="                                        MCA(SE) (2022-2024)",font=("times new roman", 12, "bold"), bg="goldenrod1" )
        desiLable.grid(row=2, column=6, padx=25,pady=10, sticky=W)
        desLable = Label(mainFrame, text="                                        Enrol. No. 04516404522",font=("times new roman", 12, "bold"), bg="goldenrod1" )
        desLable.grid(row=3, column=6, padx=25,pady=10, sticky=W)
    

    def HomePage(self):
        from main import FaceRecognitionSystem
        self.new_Window=Toplevel(self.root)
        self.app=FaceRecognitionSystem(self.new_Window)






if __name__ == "__main__" :
    root = Tk()
    obj = Developer(root)
    root.mainloop()