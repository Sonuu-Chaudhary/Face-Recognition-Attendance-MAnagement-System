from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x780+0+0")
        self.root.title("Face Recognition Attendance System")

        #Variables

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_photo = StringVar()


        # 1st Image
        img1 = Image.open(r"D:\Attendance System Project\Downloaded Image\Student1.jpg")
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

        img3 = Image.open(r"D:\Attendance System Project\Downloaded Image\Students.jpg")
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


        titleLable = Label(bg_lable, text="Student Management System", font=("times new roman", 25, "bold"), bg="white", fg="blue")
        titleLable.place(x=0, y=0, width=1370, height=40)

        ## BACK   
        backBtn = Button(titleLable,command=self.HomePage, text="Home" , cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="red", activebackground="blue")
        backBtn.place(x=0, y=0, width=110, height=50)

        # Frame
        mainFrame = Frame(bg_lable, bd=2)
        mainFrame.place(x=10, y=45, width=1470, height=600)

        # Left Lable

        LeftFrame = LabelFrame(mainFrame, bd=4, relief=RIDGE, text="Student Details", font=("times new roman", 15, "bold"))
        LeftFrame.place(x=10, y=10, width=720, height=580)

        # imgLeft = Image.open(r"D:\Attendance System Project\Downloaded Image\Students.jpg")
        # imgLeft = img3.resize((700,130), Image.LANCZOS)
        # self.photoimageLeft = ImageTk.PhotoImage(imgLeft)

        # f_lable = Label(LeftFrame,image=self.photoimageLeft)
        # f_lable.place(x=5, y=0, width=700, height=130)

        # Current Course
        CurrentFrame = LabelFrame(LeftFrame, bd=4, relief=RIDGE, text="Current Course", font=("times new roman", 13, "bold"))
        CurrentFrame.place(x=5, y=20, width=700, height=115)
        # Department
        deptLable = Label(CurrentFrame, text="Department",font=("times new roman", 12, "bold"), bg="white" )
        deptLable.grid(row=0, column=0, padx=10, sticky=W)

        deptCombo = ttk.Combobox(CurrentFrame, textvariable=self.var_dep ,font=("times new roman", 11, "bold"), state="readonly")
        deptCombo["values"] = ("Select Department", "CS", "IT", "SE", "Civil", "Mechanical")
        deptCombo.current(0)
        deptCombo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        courseLable = Label(CurrentFrame, text="Course",font=("times new roman", 12, "bold"), bg="white" )
        courseLable.grid(row=0, column=2, padx=10, sticky=W)

        courseCombo = ttk.Combobox(CurrentFrame, textvariable=self.var_course , font=("times new roman", 11, "bold"), state="readonly")
        courseCombo["values"] = ("Select Course", "MCA", "B. tech", "MBA", "BALLB", "MA")
        courseCombo.current(0)
        courseCombo.grid(row=0, column=3, padx=3, pady=10, sticky=W)

        # Year
        YearLable = Label(CurrentFrame, text="Year",font=("times new roman", 12, "bold"), bg="white" )
        YearLable.grid(row=1, column=0, padx=10, sticky=W)

        YearCombo = ttk.Combobox(CurrentFrame, textvariable=self.var_year , font=("times new roman", 11, "bold"), state="readonly")
        YearCombo["values"] = ("Select Year", "2021-2022", "2022-2023", "2023-2024", "2024-2025")
        YearCombo.current(0)
        YearCombo.grid(row=1, column=1, padx=1, pady=10, sticky=W)


        # Semester
        SemesterLable = Label(CurrentFrame, text="Semester",font=("times new roman", 12, "bold"), bg="white" )
        SemesterLable.grid(row=1, column=2, padx=10, sticky=W)

        SemesterCombo = ttk.Combobox(CurrentFrame, textvariable=self.var_sem , font=("times new roman", 11, "bold"), state="readonly")
        SemesterCombo["values"] = ("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        SemesterCombo.current(0)
        SemesterCombo.grid(row=1, column=3, padx=3, pady=10, sticky=W)

        # Student Information
        StudentFrame = LabelFrame(LeftFrame, bd=4, relief=RIDGE, text="Student Information", font=("times new roman", 13, "bold"))
        StudentFrame.place(x=5, y=135, width=700, height=250)
        # Student ID
        StudentIdLable = Label(StudentFrame, text="ID",font=("times new roman", 12, "bold"), bg="white" )
        StudentIdLable.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        StudentIdEntry = ttk.Entry(StudentFrame, textvariable=self.var_id , width=20, font=("times new roman", 12, "bold"))
        StudentIdEntry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        StudentNameLable = Label(StudentFrame, text="Name",font=("times new roman", 12, "bold"), bg="white" )
        StudentNameLable.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        StudentNameEntry = ttk.Entry(StudentFrame, textvariable=self.var_name , width=20, font=("times new roman", 12, "bold"))
        StudentNameEntry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

       # Student Division
        StudentDivLable = Label(StudentFrame, text="Division",font=("times new roman", 12, "bold"), bg="white" )
        StudentDivLable.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        
        divCombo = ttk.Combobox(StudentFrame, textvariable=self.var_div , width=18, font=("times new roman", 11, "bold"), state="readonly")
        divCombo["values"] = ("1st", "2nd", "3rd")
        divCombo.current(0)
        divCombo.grid(row=1, column=1, padx=10, pady=5, sticky=W)


        # Student Roll No
        StudentRollLable = Label(StudentFrame, text="Roll No.",font=("times new roman", 12, "bold"), bg="white" )
        StudentRollLable.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        StudentRollEntry = ttk.Entry(StudentFrame, textvariable=self.var_roll , width=20, font=("times new roman", 12, "bold"))
        StudentRollEntry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        
        # Student Gender
        StudentGenLable = Label(StudentFrame, text="Gender",font=("times new roman", 12, "bold"), bg="white" )
        StudentGenLable.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        
        genderCombo = ttk.Combobox(StudentFrame, textvariable=self.var_gender , width=18, font=("times new roman", 11, "bold"), state="readonly")
        genderCombo["values"] = ("Male", "Female", "Other")
        genderCombo.current(0)
        genderCombo.grid(row=2, column=1, padx=10, pady=5, sticky=W)


        # Student DOB
        StudentDobLable = Label(StudentFrame, text="DOB",font=("times new roman", 12, "bold"), bg="white" )
        StudentDobLable.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        StudentDobEntry = ttk.Entry(StudentFrame, textvariable=self.var_dob , width=20, font=("times new roman", 12, "bold"))
        StudentDobEntry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        
       # Student Email
        EmailLable = Label(StudentFrame, text="Email",font=("times new roman", 12, "bold"), bg="white" )
        EmailLable.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        EmailEntry = ttk.Entry(StudentFrame, textvariable=self.var_email , width=20, font=("times new roman", 12, "bold"))
        EmailEntry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        # Student Phone no
        PhoneLable = Label(StudentFrame, text="Mobile No.",font=("times new roman", 12, "bold"), bg="white" )
        PhoneLable.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        PhoneEntry = ttk.Entry(StudentFrame, textvariable=self.var_phone , width=20, font=("times new roman", 12, "bold"))
        PhoneEntry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        
        # Student Address
        AddressLable = Label(StudentFrame, text="Address",font=("times new roman", 12, "bold"), bg="white" )
        AddressLable.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        AddressEntry = ttk.Entry(StudentFrame, textvariable=self.var_address , width=20, font=("times new roman", 12, "bold"))
        AddressEntry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        
        # Teacher Name
        TeacherLable = Label(StudentFrame, text="Teacher Name",font=("times new roman", 12, "bold"), bg="white" )
        TeacherLable.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        TeacherEntry = ttk.Entry(StudentFrame, textvariable=self.var_teacher , width=20, font=("times new roman", 12, "bold"))
        TeacherEntry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
        
        # Radio Button
        self.var_radio1 = StringVar()

        radio1 = ttk.Radiobutton(StudentFrame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radio1.grid(row=8, column=0, padx=10, pady=10)

        

        radio2 = ttk.Radiobutton(StudentFrame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radio2.grid(row=8, column=1, padx=10, pady=10)

        # Button

        ButtonFrame = LabelFrame(LeftFrame, bd=4, relief=RIDGE, text="", font=("times new roman", 13, "bold"))
        ButtonFrame.place(x=0, y=390, width=700, height=150)

        saveButon = Button(ButtonFrame, command=self.addData, text="Save",width=10, font=("times new roman", 12, "bold"), bg="green", fg="white")
        saveButon.grid(row=0, column=0)

        updateButon = Button(ButtonFrame, command=self.updateData, text="Update",width=10, font=("times new roman", 12, "bold"), bg="yellow", fg="blue")
        updateButon.grid(row=0, column=1)

        deleteButton = Button(ButtonFrame,command=self.deleteData, text="Delete",width=10, font=("times new roman", 12, "bold"), bg="red", fg="white")
        deleteButton.grid(row=0, column=2)

        resetButon = Button(ButtonFrame, command=self.resetData, text="Reset",width=10, font=("times new roman", 12, "bold"), bg="white", fg="blue")
        resetButon.grid(row=0, column=3)



        takePhotoButon = Button(ButtonFrame,command=self.generateDataset, text="Take Photo",width=25, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        takePhotoButon.grid(row=1, column=0, pady=5)

        UpdatePhotoButon = Button(ButtonFrame, text="Update Photo",width=25, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        UpdatePhotoButon.grid(row=1, column=2, pady=5)

        # Right Lable

        RightFrame = LabelFrame(mainFrame, bd=4, relief=RIDGE, text="Student Details", font=("times new roman", 15, "bold"))
        RightFrame.place(x=740, y=10, width=600, height=580)

        imgRight = Image.open(r"D:\Attendance System Project\Downloaded Image\Student3.jpg")
        imgRight = imgRight.resize((700,130), Image.LANCZOS)
        self.photoimageRight = ImageTk.PhotoImage(imgRight)

        r_lable = Label(RightFrame,image=self.photoimageRight)
        r_lable.place(x=5, y=0, width=700, height=130)

        # Search System

        SearchFrame = LabelFrame(RightFrame, bd=4, relief=RIDGE, text="Search System", font=("times new roman", 13, "bold"))
        SearchFrame.place(x=5, y=135, width=700, height=70)

        PhoneLable = Label(SearchFrame, text="Search By",font=("times new roman", 12, "bold"), bg="red", fg="white" )
        PhoneLable.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        SearchCombo = ttk.Combobox(SearchFrame, font=("times new roman", 11, "bold"), width=15, state="readonly")
        SearchCombo["values"] = ("Select", "Roll No", "Phone No")
        SearchCombo.current(0)
        SearchCombo.grid(row=0, column=1, padx=3, pady=10, sticky=W)

        SearchEntry = ttk.Entry(SearchFrame, width=15, font=("times new roman", 12, "bold"))
        SearchEntry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        

        SearchButon = Button(SearchFrame, text="Search",width=10, font=("times new roman", 12, "bold"), bg="green", fg="white")
        SearchButon.grid(row=0, column=3, padx=4)

        ShowButton = Button(SearchFrame, text="Show All",width=10, font=("times new roman", 12, "bold"), bg="green", fg="white")
        ShowButton.grid(row=0, column=4, padx=4)

        # Table View

        TableFrame = Frame(RightFrame, bd=4, relief=RIDGE)
        TableFrame.place(x=5, y=210, width=600, height=250)

        scrollX = ttk.Scrollbar(TableFrame, orient=HORIZONTAL)
        scrollY = ttk.Scrollbar(TableFrame, orient=VERTICAL)

        self.StudentTable = ttk.Treeview(TableFrame, column=("dep", "course", "year", "sem", "id", "name", "division", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)

        scrollX.config(command=self.StudentTable.xview)
        scrollY.config(command=self.StudentTable.yview)


        self.StudentTable.heading("dep", text="Department")
        self.StudentTable.heading("course", text="Course")
        self.StudentTable.heading("year", text="Year")
        self.StudentTable.heading("sem", text="Semester")
        self.StudentTable.heading("id", text="ID")
        self.StudentTable.heading("name", text="Name")
        self.StudentTable.heading("division", text="Division")
        self.StudentTable.heading("roll", text="Roll No.")
        self.StudentTable.heading("gender", text="Gender")
        self.StudentTable.heading("dob", text="DOB")
        self.StudentTable.heading("email", text="Email")
        self.StudentTable.heading("phone", text="Mobile No.")
        self.StudentTable.heading("address", text="Address")
        self.StudentTable.heading("teacher", text="Teacher")
        self.StudentTable.heading("photo", text="Photo")
        self.StudentTable["show"] = "headings"

        self.StudentTable.column("dep", width=100)
        self.StudentTable.column("course", width=100)
        self.StudentTable.column("year", width=100)
        self.StudentTable.column("sem", width=100)
        self.StudentTable.column("id", width=100)
        self.StudentTable.column("name", width=100)
        self.StudentTable.column("division", width=100)
        self.StudentTable.column("roll", width=100)
        self.StudentTable.column("gender", width=100)
        self.StudentTable.column("dob", width=100)
        self.StudentTable.column("email", width=100)
        self.StudentTable.column("phone", width=100)
        self.StudentTable.column("address", width=100)
        self.StudentTable.column("teacher", width=100)
        self.StudentTable.column("photo", width=150)

        self.StudentTable.pack(fill=BOTH, expand=1)
        self.StudentTable.bind("<ButtonRelease>", self.getCursor)

        self.fetchData()

    # Function Declration

    def addData(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)  
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "Sonu$121099sql", database = "face_recognition")
                myCursor = conn.cursor()
                myCursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                    ))
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("Sucsecc", "Student Details has been added successfully", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)

 

        ##     Fetch Data   =======
                
    def fetchData(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "Sonu$121099sql", database = "face_recognition")
        myCursor = conn.cursor()
        myCursor.execute("select * from student")
        data = myCursor.fetchall()

        if len(data)!=0:
            self.StudentTable.delete(*self.StudentTable.get_children())
            for i in data:
                self.StudentTable.insert("", END, values=i)
            conn.commit()
        conn.close()

        # Get Cursor=========#

    def getCursor(self, event=""):
        cursorFocus = self.StudentTable.focus()
        content = self.StudentTable.item(cursorFocus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    ##  Update Function  ####################3
             
    def updateData(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)  
        else:
            try:
                update = messagebox.askyesno("update", "Do you want to update this student detail", parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host = "localhost", username = "root", password = "Sonu$121099sql", database = "face_recognition")
                    myCursor = conn.cursor()
                    myCursor.execute("""update student set dep=%s, course=%s, year=%s, sem=%s, name=%s, division=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photo=%s where id=%s""",(
                       
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetchData()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to{str(es)}", parent=self.root)

  #     DELETE FUNCTION ========####

    def deleteData(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student delete page", "Do you want to delete this student", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host = "localhost", username = "root", password = "Sonu$121099sql", database = "face_recognition")
                    myCursor = conn.cursor()
                    sql = "delete from student where id=%s"
                    val= (self.var_id.get(),)
                    myCursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student detail", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to{str(es)}", parent=self.root)

    #    RESET FUNCTION ======######

    def resetData(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("1st")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


   

    def generateDataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)  
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Sonu$121099sql", database="face_recognition")
                myCursor = conn.cursor()
                myCursor.execute("SELECT * FROM student")
                myResult = myCursor.fetchall()
                id = len(myResult)  # Incrementing ID
                
                myCursor.execute("""UPDATE student SET dep=%s, course=%s, year=%s, sem=%s, name=%s, division=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photo=%s WHERE id=%s""",
                                (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_sem.get(),
                                self.var_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(),
                                self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(),
                                self.var_teacher.get(), self.var_radio1.get(), id))
                conn.commit()
                self.fetchData()
                self.resetData()
                conn.close()

                faceClassifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def faceCroped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = faceClassifier.detectMultiScale(gray, 1.3, 5)
                    cropped_faces = []
                    for (x, y, w, h) in faces:
                        cropped_face = img[y:y+h, x:x+w]
                        cropped_faces.append(cropped_face)
                    return cropped_faces
                
                cap = cv2.VideoCapture(0)
                imgId = 0

                while True:
                    ret, Myframe = cap.read()
                    if ret:
                        faces = faceCroped(Myframe)
                        for face in faces:
                            imgId += 1
                            face_resized = cv2.resize(face, (450, 450))
                            face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
                            fileName = f"data/user.{id}.{imgId}.jpg"
                            cv2.imwrite(fileName, face_gray)
                            cv2.putText(face_resized, str(imgId), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face_resized)
                        if cv2.waitKey(1) == 13 or imgId == 100:
                            break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed")

            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    def HomePage(self):
        from main import FaceRecognitionSystem
        self.new_Window=Toplevel(self.root)
        self.app=FaceRecognitionSystem(self.new_Window)




    

    


   

   


    







if __name__ == "__main__" :
    root = Tk()
    obj = Student(root)
    root.mainloop()