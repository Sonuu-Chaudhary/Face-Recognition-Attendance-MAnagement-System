from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os 
import csv
from tkinter import filedialog


myData=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x780+0+0")
        self.root.title("Face Recognition Attendance System")

        #Variables

        self.varID=StringVar()
        self.varRoll=StringVar()
        self.varName=StringVar()
        self.varDep=StringVar()
        self.varTime=StringVar()
        self.varDate=StringVar()
        self.varAtt=StringVar()


# 1st Img =========
        img1 = Image.open(r"D:\Attendance System Project\Downloaded Image\ClassStudent.jpg")
        img1 = img1.resize((700,200), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img1)
        f_lable = Label(self.root,image=self.photoimage)
        f_lable.place(x=0, y=0, width=700, height=200)

# 2nd Image 

        img2 = Image.open(r"D:\Attendance System Project\Downloaded Image\StudentinClass2.jpg")
        img2 = img2.resize((700,200), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        f_lable = Label(self.root,image=self.photoimage2)
        f_lable.place(x=700, y=0, width=700, height=200)

        # BG img========

        BgImage = Image.open(r"D:\Attendance System Project\Downloaded Image\BgImage.jpg")
        BgImage = BgImage.resize((1370,550), Image.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(BgImage)
        bg_lable = Label(self.root,image=self.photoimage4)
        bg_lable.place(x=0, y=200, width=1370, height=550)


        titleLable = Label(bg_lable, text="Attendance Management System", font=("times new roman", 25, "bold"), bg="white", fg="blue")
        titleLable.place(x=0, y=0, width=1370, height=40)
        ##BACK

        backBtn = Button(titleLable,command=self.HomePage, text="Home" , cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="red", activebackground="blue")
        backBtn.place(x=0, y=0, width=110, height=50)

        mainFrame = Frame(bg_lable, bd=2)
        mainFrame.place(x=10, y=45, width=1340, height=440)
        ##Left======

        LeftFrame = LabelFrame(mainFrame, bd=4, relief=RIDGE, text="Attendance Management", font=("times new roman", 15, "bold"))
        LeftFrame.place(x=5, y=5, width=660, height=420)

        LeftInsideFrame = Frame(LeftFrame, bd=2, relief=RIDGE, bg="light goldenrod yellow")
        LeftInsideFrame.place(x=15, y=15, width=620, height=370)
         # Attendance id
        AttIdLable = Label(LeftInsideFrame, text="Attendance ID",font=("times new roman", 12, "bold"), bg="white" )
        AttIdLable.grid(row=0, column=0, padx=5,pady=10, sticky=W)

        AttIdEntry = ttk.Entry(LeftInsideFrame,  width=20,textvariable=self.varID, font=("times new roman", 12, "bold"))
        AttIdEntry.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        # Roll=====
        RollLable = Label(LeftInsideFrame, text="Roll",font=("times new roman", 12, "bold"), bg="white" )
        RollLable.grid(row=0, column=2, padx=5,pady=10, sticky=W)

        RollEntry = ttk.Entry(LeftInsideFrame,  width=20,textvariable=self.varRoll,  font=("times new roman", 12, "bold"))
        RollEntry.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        # Name ======

        NameLable = Label(LeftInsideFrame, text="Name",font=("times new roman", 12, "bold"), bg="white" )
        NameLable.grid(row=1, column=0, padx=5,pady=10, sticky=W)

        NameEntry = ttk.Entry(LeftInsideFrame,  width=20,textvariable=self.varName,  font=("times new roman", 12, "bold"))
        NameEntry.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        #Department
        DepLable = Label(LeftInsideFrame, text="Department",font=("times new roman", 12, "bold"), bg="white" )
        DepLable.grid(row=1, column=2, padx=5,pady=10, sticky=W)

        DepEntry = ttk.Entry(LeftInsideFrame,  width=20,textvariable=self.varDep,  font=("times new roman", 12, "bold"))
        DepEntry.grid(row=1, column=3, padx=5, pady=10, sticky=W)

        #Time
        TimeLable = Label(LeftInsideFrame, text="Time",font=("times new roman", 12, "bold"), bg="white" )
        TimeLable.grid(row=3, column=0, padx=5,pady=10, sticky=W)

        TimeEntry = ttk.Entry(LeftInsideFrame,  width=20,textvariable=self.varTime,  font=("times new roman", 12, "bold"))
        TimeEntry.grid(row=3, column=1, padx=5, pady=10, sticky=W)

        #Date
        DateLable = Label(LeftInsideFrame, text="Date",font=("times new roman", 12, "bold"), bg="white" )
        DateLable.grid(row=3, column=2, padx=5,pady=10, sticky=W)

        DateEntry = ttk.Entry(LeftInsideFrame,  width=20,textvariable=self.varDate,  font=("times new roman", 12, "bold"))
        DateEntry.grid(row=3, column=3, padx=5, pady=10, sticky=W)
        
        #Attendance====
        AttLable = Label(LeftInsideFrame, text="Attendance Status",font=("times new roman", 12, "bold"), bg="white" )
        AttLable.grid(row=4, column=0, padx=5,pady=10, sticky=W)

        AttCombo = ttk.Combobox(LeftInsideFrame, width=18,textvariable=self.varAtt,  font=("times new roman", 11, "bold"), state="readonly")
        AttCombo["values"] = ("Status","Present", "Absent")
        AttCombo.current(0)
        AttCombo.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Buttons =======##########

        saveButon = Button(LeftInsideFrame, text="Import",command=self.importCSV, width=10, font=("times new roman", 12, "bold"), bg="green", fg="white")
        saveButon.grid(row=6, column=0, padx=10, pady=10)

        # updateButon = Button(LeftInsideFrame, text="Update",width=10, font=("times new roman", 12, "bold"), bg="yellow", fg="blue")
        # updateButon.grid(row=6, column=2, padx=10, pady=10)

        deleteButton = Button(LeftInsideFrame, text="Export",command=self.exportCSV,width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        deleteButton.grid(row=8, column=0, padx=10, pady=10)

        resetButon = Button(LeftInsideFrame, text="Reset",width=10,command=self.resetData, font=("times new roman", 12, "bold"), bg="white", fg="blue")
        resetButon.grid(row=8, column=2, padx=10, pady=10)






        # Right======
        RightFrame = LabelFrame(mainFrame, bd=4, relief=RIDGE, text="Attendance Details", font=("times new roman", 15, "bold"))
        RightFrame.place(x=670, y=5, width=660, height=420)

        RightInsideFrame = Frame(RightFrame, bd=2, relief=RIDGE, bg="light goldenrod yellow")
        RightInsideFrame.place(x=10, y=10, width=640, height=370)

        #Scroll / Table
        scrollX=ttk.Scrollbar(RightInsideFrame, orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(RightInsideFrame, orient=VERTICAL)
        self.ReportTable = ttk.Treeview(RightInsideFrame, column=("id", "roll","name", "dep", "time", "date", "attendance"),xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)

        scrollX.config(command=self.ReportTable.xview)
        scrollY.config(command=self.ReportTable.yview)

        self.ReportTable.heading("id",text="Attendance ID")
        self.ReportTable.heading("roll",text="Roll")
        self.ReportTable.heading("name",text="Name")
        self.ReportTable.heading("dep",text="Department")
        self.ReportTable.heading("time",text="Time")
        self.ReportTable.heading("date",text="Date")
        self.ReportTable.heading("attendance",text="Attendance")

        self.ReportTable["show"]="headings"
        self.ReportTable.column("id", width=100)
        self.ReportTable.column("roll", width=100)
        self.ReportTable.column("name", width=100)
        self.ReportTable.column("dep", width=100)
        self.ReportTable.column("time", width=100)
        self.ReportTable.column("date", width=100)
        self.ReportTable.column("attendance", width=100)


        self.ReportTable.pack(fill=BOTH, expand=1)
        self.ReportTable.bind("<ButtonRelease>", self.getCursor)

        ## FetchData   =======

    def fetchData(self, rows):
        self.ReportTable.delete(*self.ReportTable.get_children())
        for i in rows:
            self.ReportTable.insert("", END, values=i)

    def importCSV(self):
        global myData
        myData.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwdb(),title="Open CSV", filetypes=[("CSV File", "*csv"), ("All File", "*.*")], parent=self.root)
        with open(fln) as myFile:
            csvread=csv.reader(myFile, delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)

            # Export CSV


    def exportCSV(self):
        try:
            if len(myData)<1:
                messagebox.showerror("Error", "No data found to export", parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwdb(),title="Open CSV", filetypes=[("CSV File", "*csv"), ("All File", "*.*")], parent=self.root)
            with open(fln,mode="w", newline="") as myfile:
                expWrite=csv.writer(myfile, delimiter=",")
                for i in myData:
                    expWrite.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to"+os.path.basename(fln)+"successfully")

        except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)




    def getCursor(self, event=""):
        cursorRow=self.ReportTable.focus()
        content=self.ReportTable.item(cursorRow)
        rows=content['values']
        self.varID.set(rows[0])
        self.varRoll.set(rows[1])
        self.varName.set(rows[2])
        self.varDep.set(rows[3])
        self.varTime.set(rows[4])
        self.varDate.set(rows[5])
        self.varAtt.set(rows[6])
    def resetData(self):
        self.varID.set("")
        self.varRoll.set("")
        self.varName.set("")
        self.varDep.set("")
        self.varTime.set("")
        self.varDate.set("")
        self.varAtt.set("")
    

    def HomePage(self):
        from main import FaceRecognitionSystem
        self.new_Window=Toplevel(self.root)
        self.app=FaceRecognitionSystem(self.new_Window)










if __name__ == "__main__" :
    root = Tk()
    obj = Attendance(root)
    root.mainloop()