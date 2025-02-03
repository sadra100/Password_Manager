from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from cryptography.fernet import Fernet
import login
import menu


# ________________________ALL GUI______________________________________________________

def SignUp():
    window_signnup = Tk()
    window_signnup.title("PASSAM(sign up)")
    window_signnup.geometry("800x500")
    window_signnup.config(bg="#000066")
    window_signnup.resizable(False, False)
    window_signnup.iconbitmap("D:\Projects\PassWordManger\icon2.ico")
    # __________________________________________________________________________________________
    # image app icon
    passam_Image_Icon = Image.open("logo.png")
    passam_Image_Icon = passam_Image_Icon.resize((320, 210))
    Tk_passam_Image = ImageTk.PhotoImage(passam_Image_Icon)
    Passam_Image_Lable = Label(window_signnup, image=Tk_passam_Image)
    Passam_Image_Lable.place(x=50, y=140)
    # _______________________________________________________________________________________________
    # welcome text in app header
    Text_Welcom = Label(window_signnup, text='Welcome', bg="#000066", fg='white', width=10)
    Text_Welcom.pack()
    Text_Welcom_Style = ("Caveat", 50, "bold")
    Text_Welcom.configure(font=Text_Welcom_Style)
    # ____________________________________________________________________________________________________
    # text enter password
    Text_Enter_Password = Label(window_signnup, text="Enter Password for Sign up", bg="#000066", fg="white")
    Text_Enter_Password.pack()
    Text_Enter_Password.place(x=440, y=150)
    Text_Enter_Password_Style = ("Comic Sans Ms", 15, "bold")
    Text_Enter_Password.configure(font=Text_Enter_Password_Style)
    # ________________________________________________________________________________________________________
    # edit text enter password
    Password_Entry = Entry(window_signnup, width=30)
    Password_Entry.pack()
    Password_Entry.place(x=395, y=220)
    Password_Entry_Style = ("Arial")
    Password_Entry.configure(font=Password_Entry_Style)

    # ___________________________________________________________________________________________________________
    # function click button
    def signUP_password_input():
        valueEditText = Password_Entry.get()
        if valueEditText == '':
            messagebox.showerror('Error', 'Please enter password')
        else:
            messagebox.showinfo('Success', 'Sign up successfully')
            Write_value_checkuser()

            App_Password_Encrypt = fernet.encrypt(valueEditText.encode()).decode()
            File_App_Password = open("App_Password", "a")
            File_App_Password.write(App_Password_Encrypt)
            File_App_Password.close()

            window_signnup.destroy()
            login.Login()

    # ____________________________________________________________________________________________________________
    # button sign up
    Button_SignUp = Button(window_signnup, text='Sign Up', width=15, fg='white', bg='green',
                           command=signUP_password_input)
    Button_SignUp.pack()
    Button_SignUp.place(x=445, y=280)
    Button_SignUp_Style = ("Centaur", 17, "bold")
    Button_SignUp.configure(font=Button_SignUp_Style)

    window_signnup.mainloop()


File_Check_User = open('Check_New_User.txt', 'a')
File_Check_User = open('Check_New_User.txt', 'r')


def Write_value_checkuser():
    File_Check_User = open('Check_New_User.txt', 'w')
    File_Check_User.write('1')
    File_Check_User.close()


# ____________________________________________________________________________________

def write_key_file():
    if File_Check_User.read() == "":
        key = Fernet.generate_key()
        key_file = open("key.key", "wb")
        key_file.write(key)


# _____________________________________________________________________________________________
def Load_Key_File():
    global fernet
    key_file = open("key.key", "rb")
    key = key_file.read()
    key_file.close()
    fernet = Fernet(key)


# _____________________________________________________________________________________________________
def check_App_Password():
    global App_Password_Decrypt

    File_App_Password=open('App_Password','r')
    File_App_Password=File_App_Password.read()

    Load_Key_File()

    App_Password_Decrypt=fernet.decrypt(File_App_Password.encode()).decode()


if File_Check_User.read() == "":
    write_key_file()
    Load_Key_File()
    SignUp()
else:
    login.Login()
