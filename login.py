from tkinter import *
from tkinter import messagebox
import utiles
import menu

#_____________________________Login__________________________________
def Login():
    window_login=Tk()
    window_login.title("Passam(Log in)")
    window_login.geometry('800x500')
    window_login.configure(bg='#000066')
    window_login.resizable(False,False)
    window_login.iconbitmap('icon_kcl_icon.ico')
    #_____________________________________________________________________
    # text login
    Text_Login=Label(window_login,text='Login',bg='#000066',fg='white',width=10)
    Text_Login.pack()
    Text_Login_Style=("Caveat",50,"bold")
    Text_Login.configure(font=Text_Login_Style)
    #_________________________________________________________________________
    #frame box
    frame=Frame(window_login,bg='#0000CC',height=350,width=400)
    frame.pack()
    frame.place(x=200,y=120)
    #____________________________________________________________________________
    #text enter password
    Text_Enter_Password=Label(frame,text='Enter Password for Login',bg='#0000CC',fg='white')
    Text_Enter_Password.pack()
    Text_Enter_Password.place(x=70,y=50)
    Text_Enter_Password_Style=("Comic Sans Ms",15,'bold')
    Text_Enter_Password.configure(font=Text_Enter_Password_Style)
    #__________________________________________________________________________________
    #edit text enter password
    Password_Entry=Entry(frame,width=30)
    Password_Entry.pack()
    Password_Entry.place(x=30,y=110)
    Password_Entry_Style=('Arial')
    Password_Entry.configure(font=Password_Entry_Style)
    #_______________________________________________________________________________________
    def get_login_enter_password():
        valueEditText =Password_Entry.get()
        if valueEditText=='':
            messagebox.showerror('Error','Please enter your password!')
        else:
            utiles.check_App_Password()
            if valueEditText==utiles.App_Password_Decrypt:
                messagebox.showinfo('Success','Your password is correct')
                window_login.destroy()
                menu.Menu()

            else:
                messagebox.showerror('Error','Password is wrong')


    #button login
    Button_Login=Button(frame,text="Login",bg='green',fg='white',width=15,command=get_login_enter_password)
    Button_Login.pack()
    Button_Login.place(x=95,y=180)
    Button_Login_Style=('Centaur',17,'bold')
    Button_Login.configure(font=Button_Login_Style)



    window_login.mainloop()


