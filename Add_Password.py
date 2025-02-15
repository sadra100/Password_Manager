from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import menu
import utiles


def Add():
    window_add=Tk()
    window_add.title('Passam(Add_Password)')
    window_add.geometry('800x500')
    window_add.configure(bg='#000066')
    window_add.resizable(False,False)
    window_add.iconbitmap('icon_kcl_icon.ico')
#___________________________________________________________________________________________
    Add_Image_Icon=Image.open('logo2.png')
    Add_Image_Icon=Add_Image_Icon.resize((310,210))
    Tk_Add_Image=ImageTk.PhotoImage(Add_Image_Icon)
    Add_image_Lable=Label(window_add,image=Tk_Add_Image)
    Add_image_Lable.place(x=30,y=160)
#____________________________________________________________________________________________________
    text_add_password=Label(window_add,text='Add Password',bg='#000066',fg='white',width=15)
    text_add_password.pack()
    text_add_password.place()
    text_add_password_style=('Caveat',50,'bold')
    text_add_password.configure(font=text_add_password_style)
#_________________________________________________________________________________________________________
    back_image_icon=Image.open('back.png')
    back_image_icon=back_image_icon.resize((25,25))
    back_image_icon=ImageTk.PhotoImage(back_image_icon)

    def button_back_clicked():
        window_add.destroy()
        menu.Menu()

    button_back=Button(window_add,image=back_image_icon,command=button_back_clicked)
    button_back.pack()
    button_back.place(x=40,y=30)
# _________________________________________________________________________________________________________
    frame=Frame(window_add,bg='#0000CC',width=400,height=350)
    frame.pack()
    frame.place(x=370,y=120)
# _________________________________________________________________________________________________________
    text_platform_name=Label(frame,text='Enter Platform Name',bg='#0000CC',fg='white')
    text_platform_name.pack()
    text_platform_name.place(x=100,y=20)
    text_platform_name_style=('Arial')
    text_platform_name.configure(font=text_platform_name_style)

    entry1=Entry(frame,width=45)
    entry1.pack()
    entry1.place(x=65,y=50)
# _________________________________________________________________________________________________________
    text_account_username=Label(frame,text='Enter Account Username',bg='#0000CC',fg='white')
    text_account_username.pack()
    text_account_username.place(x=90,y=100)
    text_account_username_style=('Arial')
    text_account_username.configure(font=text_account_username_style)

    enry2=Entry(frame,width=45)
    enry2.pack()
    enry2.place(x=65,y=130)

# _________________________________________________________________________________________________________
    text_account_password=Label(frame,text='Enter Account Password',bg='#0000CC',fg='white')
    text_account_password.pack()
    text_account_password.place(x=90,y=180)
    text_account_password_style=('Arial')
    text_account_password.configure(font=text_account_password_style)

    entry3=Entry(frame,width=45)
    entry3.pack()
    entry3.place(x=65,y=210)
#__________________________________________________________________________________________________________
    def button_save_clicked():
        value_platform_entry=entry1.get()
        value_account_entry=enry2.get()
        value_password_entry=entry3.get()

        if value_platform_entry and value_account_entry and value_password_entry !="":
            result=value_platform_entry + ' ' + ':' + ' ' + value_account_entry + ' ' + '=' + ' ' + value_password_entry
            All_Password_Encrypt=utiles.fernet.encrypt(result.encode()).decode()

            File_All_Password=open('All_Password','a')
            File_All_Password.write(All_Password_Encrypt+'\n')
            File_All_Password.close()
            result=''

            messagebox.showinfo('Success','Save info successfully')
        else:
            messagebox.showerror('Error','Please fill field')

    button_save=Button(frame,text='Save',width=17,bg='green',fg='white',command=button_save_clicked)
    button_save.pack()
    button_save.place(x=85,y=260)
    button_save_style=('Centaur',17,'bold')
    button_save.configure(font=button_save_style)

    window_add.mainloop()


# Add()'