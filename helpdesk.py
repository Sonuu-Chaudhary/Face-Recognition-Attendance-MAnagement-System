from tkinter import*
from PIL import Image, ImageTk


class HelpDesk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x780+0+0")
        self.root.title("Face Recognition Attendance System")

        titleLable = Label(self.root, text="HelpDesk", font=("times new roman", 25, "bold"), bg="white", fg="blue")
        titleLable.place(x=0, y=0, width=1370, height=40)

        ## BACK
        backBtn = Button(titleLable,command=self.HomePage, text="Home" , cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="red", activebackground="blue")
        backBtn.place(x=0, y=0, width=110, height=50)

        imgTop = Image.open(r"D:\Attendance System Project\Downloaded Image\Help.jpg")
        imgTop = imgTop.resize((1350,600), Image.LANCZOS)
        self.photoimageTop = ImageTk.PhotoImage(imgTop)

        f_lable = Label(self.root,image=self.photoimageTop)
        f_lable.place(x=0, y=55, width=1350, height=600)

        devLabel=Label(f_lable, text="Email: sonuchy95@gmail.com", font=("times new roman", 25, "bold"), fg="salmon3")
        devLabel.place(x=500, y=500)

    def HomePage(self):
        from main import FaceRecognitionSystem
        self.new_Window=Toplevel(self.root)
        self.app=FaceRecognitionSystem(self.new_Window)







if __name__ == "__main__" :
    root = Tk()
    obj = HelpDesk(root)
    root.mainloop()