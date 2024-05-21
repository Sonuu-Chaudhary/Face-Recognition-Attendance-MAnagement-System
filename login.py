
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from main import FaceRecognitionSystem

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x780+0+0")
        self.root.title("Login")
        
        # Load the image
        self.bg_image = Image.open("D:\\Attendance System Project\\Downloaded Image\\LoginBackg.jpg")
        self.bg_image=self.bg_image.resize((1320,620), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg_image)
        
        # Display the image
        lblBg = Label(self.root, image=self.bg)
        lblBg.place(x=0, y=0, relwidth=1, relheight=1)
        frame=Frame(self.root, bg="black")

        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"D:\\Attendance System Project\\Downloaded Image\\LoginLogo.jpg")
        img1=img1.resize((150,100), Image.LANCZOS)

        self.photoimage1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimage1, bg="black", borderwidth=0)

        lblimg1.place(x=730,y=175, width=100, height=100)

        get_str=Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95,y=100)

        #Label1   ===========

        username=lbl=Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame, font=("times new roman", 15, "bold"))

        self.txtpass.place(x=40,y=250,width=270)

        #########Icon Image=========

        img2=Image.open(r"D:\\Attendance System Project\\Downloaded Image\\LoginLogo.jpg")
        img2=img2.resize((25,25), Image.LANCZOS)

        self.photoimage2=ImageTk.PhotoImage(img2)

        lblimg1=Label(image=self.photoimage2, bg="black", borderwidth=0)

        lblimg1.place(x=650,y=323, width=25, height=25)



        img3=Image.open(r"D:\\Attendance System Project\\Downloaded Image\\LoginLogo.jpg")
        img3=img3.resize((25,25), Image.LANCZOS)

        self.photoimage3=ImageTk.PhotoImage(img3)

        lblimg1=Label(image=self.photoimage3, bg="black", borderwidth=0)

        lblimg1.place(x=650,y=393,width=25,height=25)

        ##LoginButton==========

        loginBtn = Button(frame,command=self.login, text="Login", font=("times new roman", 15, "bold"),borderwidth=0, fg="blue", bg="lightblue", activeforeground="red", activebackground="red")
        loginBtn.place(x=0, y=350, width=350, height=35)

        #Registration Btn

        # RegBtn = Button(frame, text="New Registration",borderwidth=0, font=("times new roman", 10, "bold"), fg="blue", bg="lightblue", activeforeground="red", activebackground="blue")
        # RegBtn.place(x=5, y=350, width=160)


# Forgot p

        # forgotBtn = Button(frame, text="Forgot Password?", font=("times new roman", 10, "bold"),borderwidth=0, fg="blue", bg="lightblue", activeforeground="white", activebackground="blue")
        # forgotBtn.place(x=5, y=380, width=160,)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get()=="sonu" and self.txtpass.get()=="1234":
            messagebox.showinfo("Success", "Welcome to Face Recognition Attendance Management System")
            self.login_Data()
        else:
            messagebox.showerror("Error", "Invalid username or password")
    




    def login_Data(self):
        self.new_Window=Toplevel(self.root)
        self.app=FaceRecognitionSystem(self.new_Window)
        
        






        





if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()
