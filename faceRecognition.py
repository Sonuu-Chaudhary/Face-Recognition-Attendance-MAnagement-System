from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import cv2
from datetime import datetime



class FaceDetection:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x780+0+0")
        self.root.title("Face Recognition Attendance System")

        titleLable = Label(self.root, text="Face Recognition", font=("times new roman", 25, "bold"), bg="white", fg="blue")
        titleLable.place(x=0, y=0, width=1370, height=40)

        imgTop = Image.open(r"D:\Attendance System Project\Downloaded Image\Training.jpg")
        imgTop = imgTop.resize((650,600), Image.LANCZOS)
        self.photoimageTop = ImageTk.PhotoImage(imgTop)

        f_lable = Label(self.root,image=self.photoimageTop)
        f_lable.place(x=0, y=55, width=650, height=600)

        #####
        
        imgBottom = Image.open(r"D:\Attendance System Project\Downloaded Image\change.jpg")
        imgBottom = imgBottom.resize((850,600), Image.LANCZOS)
        self.photoimageBottom = ImageTk.PhotoImage(imgBottom)

        f_lable = Label(self.root,image=self.photoimageBottom)
        f_lable.place(x=650, y=55, width=850, height=600)

####button
        buttn1Title = Button(f_lable, text="Face Recognition" , cursor="hand2",command=self.faceRecognition, font=("times new roman", 15, "bold"), bg="red", fg="white")
        buttn1Title.place(x=330, y=530, width=200, height=30)
        ##BACK

        backBtn = Button(titleLable,command=self.HomePage, text="Home" , cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="red", activebackground="blue")
        backBtn.place(x=0, y=0, width=110, height=50)

        
    ##   Attendance=======####

    def markAttendance(self, i, r, n, d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList=f.readlines()
            nameList=[]
            for line in myDataList:
                entry=line.split((","))
                nameList.append(entry[0])
            if((i not in nameList) and (r not in nameList) and (n not in nameList) and (d not in nameList)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {d}, {dtstring}, {d1}, Present")




  



    def faceRecognition(self):
        def drawBoundary(img, classifier, scale, minNeighbors, color, text, recognizer, cursor):
            grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(grayImage, scale, minNeighbors)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = recognizer.predict(grayImage[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                print(f"Detected ID: {id}, Confidence: {confidence}")

                try:
                    cursor.execute("SELECT name FROM student WHERE id=%s", (id,))
                    n = cursor.fetchone()
                    if n:
                        n = "+".join(n)
                    else:
                        n = "Unknown"

                    cursor.execute("SELECT roll FROM student WHERE id=%s", (id,))
                    r = cursor.fetchone()
                    if r:
                        r = "+".join(r)
                    else:
                        r = "Unknown"

                    cursor.execute("SELECT dep FROM student WHERE id=%s", (id,))
                    d = cursor.fetchone()
                    if d:
                        d = "+".join(d)
                    else:
                        d = "Unknown"

                    cursor.execute("SELECT id FROM student WHERE id=%s", (id,))
                    i = cursor.fetchone()
                    if i:
                        i = "+".join(i)
                    else:
                        i = "Unknown"    

                except Exception as e:
                    print(f"Database error: {e}")
                    n, r, d, i = "Unknown", "Unknown", "Unknown"

                if confidence > 80:
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.markAttendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, recognizer, faceCascade, cursor):
            coord = drawBoundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", recognizer, cursor)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("classifier.xml")

        # Database connection
        conn = mysql.connector.connect(host="localhost", username="root", password="Sonu$121099sql", database="face_recognition")
        cursor = conn.cursor()

        videoCap = cv2.VideoCapture(0)
        while True:
            ret, img = videoCap.read()
            if not ret:
                break
            img = recognize(img, recognizer, faceCascade, cursor)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key to break
                break

        # Clean up
        videoCap.release()
        cv2.destroyAllWindows()
        cursor.close()
        conn.close()

    def HomePage(self):
        from main import FaceRecognitionSystem
        self.new_Window=Toplevel(self.root)
        self.app=FaceRecognitionSystem(self.new_Window)








if __name__ == "__main__" :
    root = Tk()
    obj = FaceDetection(root)
    root.mainloop()
