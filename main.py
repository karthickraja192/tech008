
# install opencv-contrib-python
# uninstall opencv-python
import datetime
from tkinter.filedialog import askopenfilename
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
import pandas as pd
import csv
import os
import shutil
import time
from tkinter import Tk, messagebox, ttk
from tkinter import *
from tkinter.ttk import Treeview
import csv
import numpy as np
from PIL import Image, ImageTk
import cv2
from PIL import Image, ImageTk

from PIL import ImageTk
import ar_master_csv



class tk_master:
    id = ''
    user = ''
    fname=''
    camera=''
    def __init__(self):
        self.master = 'ar_master'
        self.title = 'Smart Missing Child'
        self.titlec = 'Smart Missing Child'
        self.backround_color = '#2F4F4F'
        self.text_color = '#FFF'
        self.backround_image = 'images/background_hd1.jpg'
    def get_title(self):
        return self.title
    def get_titlec(self):
        return self.titlec
    def get_backround_color(self):
        return self.backround_color
    def get_text_color(self):
        return self.text_color
    def get_backround_image(self):
        return self.backround_image
    def set_window_design(self):
        root = Tk()
        w = 780
        h = 500
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        root.title(self.title)
        root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=self.backround_image)
        canvas = Canvas(root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(390, 20, text=self.title, font=("Times New Roman", 24), fill=self.text_color)
        def clickHandler(event):
            tt = tk_master
            tt.admin_home(event)
        image = Image.open('images/admin.png')
        img = image.resize((125, 125))
        my_img = ImageTk.PhotoImage(img)
        image_id = canvas.create_image(270, 150, image=my_img)
        canvas.tag_bind(image_id, "<1>", clickHandler)
        def clickHandler1(event):
            tt = tk_master
            tt.select_camera(event)
        image1 = Image.open('images/user.png')
        img1 = image1.resize((125, 125))
        my_img1 = ImageTk.PhotoImage(img1)
        image_id1 = canvas.create_image(270, 320, image=my_img1)
        canvas.tag_bind(image_id1, "<1>", clickHandler1)
        admin_id = canvas.create_text(470, 150, text="Training", font=("Times New Roman", 28), fill=self.text_color)
        canvas.tag_bind(admin_id, "<1>", clickHandler)
        admin_id1 = canvas.create_text(470, 320, text="Testing", font=("Times New Roman", 28), fill=self.text_color)
        canvas.tag_bind(admin_id1, "<1>", clickHandler1)
        root.mainloop()
    def select_camera(self):
        user_home_root = Toplevel()
        user_home_root.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 780
        h = 500
        ws = user_home_root.winfo_screenwidth()
        hs = user_home_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_home_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        user_home_root.resizable(False, False)
        canvas1 = Canvas(user_home_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),
                            fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="SELECT CAMERA", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        def upload_files(event):
            tk_master.camera="Arasur"
            user_home_root.destroy()
            tt = tk_master
            tt.user_login(event)
        admin_id1 = canvas1.create_text(350, 170, text="Arasur", font=("Times New Roman", 28), fill=get_data.get_text_color())
        canvas1.tag_bind(admin_id1, "<1>", upload_files)

        def upload_files1(event):
            tk_master.camera="Junction"
            user_home_root.destroy()
            tt = tk_master
            tt.user_login(event)
        admin_id2 = canvas1.create_text(350, 230, text="Junction", font=("Times New Roman", 28), fill=get_data.get_text_color())
        canvas1.tag_bind(admin_id2, "<1>", upload_files1)

        def upload_files2(event):
            tk_master.camera="Maruthur"
            user_home_root.destroy()
            tt = tk_master
            tt.user_login(event)
        admin_id3 = canvas1.create_text(350, 290, text="Maruthur", font=("Times New Roman", 28), fill=get_data.get_text_color())
        canvas1.tag_bind(admin_id3, "<1>", upload_files2)


        user_home_root.mainloop()
    def user_login(self):
        sts=0
        name=''
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("TrainingImageLabel\Trainer.yml")
        harcascadePath = "data\haarcascades\haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)
        df = pd.read_csv("UserDetails//UserDetails.csv")
        cam = cv2.VideoCapture(0)
        # cam = cv2.VideoCapture('http://192.168.1.7:8080/video')
        font = cv2.FONT_HERSHEY_SIMPLEX

        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                r = max(w, h) / 2
                centerx = x + w / 2
                centery = y + h / 2
                nx = int(centerx - r)
                ny = int(centery - r)
                nr = int(r * 2)
                faceimg = im[ny:ny + nr, nx:nx + nr]
                font = cv2.FONT_HERSHEY_SIMPLEX

                str1 = 'tt.jpg'
                # kk=kk+1

                lastimg = cv2.resize(faceimg, (100, 100))

                cv2.imwrite(str1, lastimg)

                if (conf < 40):
                    aa = df.loc[df['Id'] == Id]['Name'].values
                    print(aa)
                    name=aa[0]
                    tt = str(Id) + "-" + aa
                    sts=sts+1
                    tk_master.id=str(Id)
                else:
                    sts=0
                    Id = 'Unknown'
                    tt = str(Id)
                if (conf > 75):
                    noOfFile = len(os.listdir("ImagesUnknown")) + 1
                    cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
                cv2.putText(im, str(tt), (x, y + h),font, 1, (255, 255, 255), 2)
            cv2.imshow('Image', im)
            if sts>15:
                print(Id,name,conf)
                tk_master.id=Id
                tk_master.user=name
                f = open("email/" + str(name) + ".txt", "r")
                to_mail = (f.read())
                # print(email)
                msg = MIMEMultipart()
                password = "mlkdrcrjnoimnclw"
                msg['From'] = "serverkey2018@gmail.com"
                msg['To'] = to_mail
                msg['Subject'] = "Child Face Detected on  Camera : " + str(tk_master.camera)+""+ str(name)
                file = str1
                fp = open(file, 'rb')
                img = MIMEImage(fp.read())
                fp.close()
                msg.attach(img)
                server = smtplib.SMTP('smtp.gmail.com: 587')
                server.starttls()
                server.login(msg['From'], password)
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                server.quit()
                break

            if (cv2.waitKey(1) == ord('q')):
                break
        cam.release()
        cv2.destroyAllWindows()
        if sts>10:
            sts=0
            print("yes")
            tt = tk_master()
            tt.user_login()
        else:
            print("no")

    def admin_login(self):
        admin_login_root = Toplevel()
        admin_login_root.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 780
        h = 500
        ws = admin_login_root.winfo_screenwidth()
        hs = admin_login_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        admin_login_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        admin_login_root.resizable(False, False)
        canvas1 = Canvas(admin_login_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),
                            fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="ADMIN LOGIN", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 200, text="Username", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 300, text="Password", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        e1 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(470, 200, window=e1)
        e2 = Entry(canvas1, font=('times', 15, ' bold '), show="*")
        canvas1.create_window(470, 300, window=e2)

        def exit_program():
            a = e1.get()
            b = e2.get()
            if (a == ""):
                messagebox.showinfo(title="Alert", message="Enter Username", parent=admin_login_root)
            elif (b == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=admin_login_root)
            elif ((a == "admin") and (b == "admin")):
                messagebox.showinfo("Result", "Login Success", parent=admin_login_root)
                admin_login_root.destroy()
                tt = tk_master()
                tt.admin_home()
            else:
                messagebox.showinfo("Result", "Login Failed", parent=admin_login_root)

        b1 = Button(canvas1, text="Login", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 400, window=b1)
        admin_login_root.mainloop()
    def admin_home(self):
        admin_home_root = Toplevel()

        admin_home_root.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 780
        h = 500
        ws = admin_home_root.winfo_screenwidth()
        hs = admin_home_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        admin_home_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        admin_home_root.resizable(False, False)
        canvas1 = Canvas(admin_home_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),
                            fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="CHILD FACE TRAINING HOME", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())

        def add_user():
            add_user_root = Toplevel()
            add_user_root.attributes('-topmost', 'true')
            get_data = tk_master()
            w = 780
            h = 500
            ws = add_user_root.winfo_screenwidth()
            hs = add_user_root.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            add_user_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
            image = Image.open('images/background_hd1.jpg')
            img = image.resize((w, h))
            my_img = ImageTk.PhotoImage(img)
            add_user_root.resizable(False, False)
            canvas1 = Canvas(add_user_root, width=200, height=300)
            canvas1.create_image(0, 0, image=my_img, anchor=NW)
            canvas1.pack(fill="both", expand=True)
            # canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),
            #                     fill=get_data.get_text_color())
            ##
            admin_id2 = canvas1.create_text(390, 20, text="ADD USER DETAILS", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 170, text="Name", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 270, text="Email", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())


            e1 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(480, 170, window=e1)
            e2 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(480, 270, window=e2)


            def exit_program():
                name = e1.get()
                email = e2.get()

                if (name == ""):
                    messagebox.showinfo(title="Alert", message="Enter Name", parent=add_user_root)
                elif (email == ""):
                    messagebox.showinfo(title="Alert", message="Enter Email", parent=add_user_root)
                else:
                    if 1==3:
                        dd=0
                    else:
                        DIR = 'training'
                        maxin=len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
                        maxin=maxin+1
                        tk_master.id=maxin
                        tk_master.user=name
                        print(tk_master.id,tk_master.user)
                        add_user_root.destroy()
                        def getImagesAndLabels(path):
                            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
                            faces = []
                            Ids = []
                            for imagePath in imagePaths:
                                pilImage = Image.open(imagePath).convert('L')
                                imageNp = np.array(pilImage, 'uint8')
                                Id = int(os.path.split(imagePath)[-1].split(".")[1])
                                faces.append(imageNp)
                                Ids.append(Id)
                            return faces, Ids
                        def face_register():
                            Id = int(tk_master.id)
                            name = str(tk_master.user)
                            print(Id,name)
                            # cam = cv2.VideoCapture('http://192.168.1.7:8080/video')
                            cam = cv2.VideoCapture(0)
                            harcascadePath = "data\haarcascades\haarcascade_frontalface_default.xml"
                            detector = cv2.CascadeClassifier(harcascadePath)
                            sampleNum = 0
                            while (True):
                                ret, img = cam.read()
                                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                                faces = detector.detectMultiScale(gray, 1.3, 5)
                                for (x, y, w, h) in faces:
                                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                                    sampleNum = sampleNum + 1
                                    cv2.imwrite("TrainingImage\ " + str(name) + "." + str(Id) + '.' + str(sampleNum) + ".jpg",gray[y:y + h, x:x + w])
                                    cropped = img[y:y + h, x:x + w]
                                    gg = str(name) + ".jpg"
                                    cv2.imwrite("training/" + gg, cropped)
                                cv2.imshow('frame', img)
                                if cv2.waitKey(100) & 0xFF == ord('q'):
                                    break
                                elif sampleNum > 60:

                                    break
                            cam.release()
                            cv2.destroyAllWindows()
                            res = "Images Saved for ID : " + str(Id) + " Name : " + str(name)
                            row = [Id, name]
                            with open('UserDetails/UserDetails.csv', 'a+') as csvFile:
                                writer = csv.writer(csvFile)
                                writer.writerow(row)
                                f = open("email/"+str(name)+".txt", "w")
                                f.write(str(email))
                                f.close()

                            csvFile.close()
                            print(res)
                            time.sleep(2)
                            ############################################################
                            recognizer = cv2.face.LBPHFaceRecognizer_create()
                            harcascadePath = "data\haarcascades\haarcascade_frontalface_default.xml"
                            detector = cv2.CascadeClassifier(harcascadePath)
                            faces, Id = getImagesAndLabels("TrainingImage")
                            recognizer.train(faces, np.array(Id))
                            recognizer.save("TrainingImageLabel\Trainer.yml")
                            res = "Image Trained"
                            print(res)
                            messagebox.showinfo(title="Result", message=str(res))
                        face_register()
            b1 = Button(canvas1, text="Register", command=exit_program, font=('times', 15, ' bold '))
            canvas1.create_window(470, 430, window=b1)
            add_user_root.mainloop()

        b1 = Button(canvas1, text="FACE REGISTER", command=add_user, font=('times', 15, ' bold '), width=20)
        canvas1.create_window(390,200, window=b1)

        def logout():
            admin_home_root.destroy()
        b3 = Button(canvas1, text="Logout", command=logout, font=('times', 15, ' bold '), width=20)
        canvas1.create_window(390, 350, window=b3)
        admin_home_root.mainloop()
ar = tk_master()
root = ar.set_window_design()
