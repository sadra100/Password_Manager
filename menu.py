from tkinter import *
from PIL import ImageTk,Image
import Add_Password
import passwords
import delete

#___________________________________Menu___________________________________
def Menu():
    window_menu=Tk()
    window_menu.title("Passam(Menu)")
    window_menu.geometry('800x500')
    window_menu.configure(bg="#000066")
    window_menu.resizable(False,False)
    window_menu.iconbitmap("icon_kcl_icon.ico")
#______________________________________________________________________________
    Text_Menu=Label(window_menu,text='Passam',bg='#000066',fg='white',width=10)
    Text_Menu.pack()
    Text_Menu_Style=('Caveat',50,'bold')
    Text_Menu.configure(font=Text_Menu_Style)
#__________________________________________________________________________________
    Frame_Add=Frame(window_menu,bg='#CCFFFF',width=150,height=150)
    Frame_Add.pack()
    Frame_Add.place(x=150,y=120)

    Add_Image=Image.open('images (1).png')
    Add_Image=Add_Image.resize((100,100))
    Add_Image=ImageTk.PhotoImage(Add_Image)

    def Button_Add_Clicked():
        window_menu.destroy()
        Add_Password.Add()


    Button_add=Button(Frame_Add,image=Add_Image,command=Button_Add_Clicked)
    Button_add.pack()
    Button_add.place(x=23,y=23)

#___________________________________________________________________________________
    Frame_Del=Frame(window_menu,bg='#CCFFFF',width=150,height=150)
    Frame_Del.pack()
    Frame_Del.place(x=500,y=120)

    Del_Image=Image.open('del2.jpg')
    Del_Image=Del_Image.resize((100,100))
    Del_Image=ImageTk.PhotoImage(Del_Image)

    def Button_Delete_Clicked():
        window_menu.destroy()
        delete.delete()

    Button_Del=Button(Frame_Del,image=Del_Image,command=Button_Delete_Clicked)
    Button_Del.pack()
    Button_Del.place(x=23,y=23)
#_________________________________________________________________________________________________
    Frame_View=Frame(window_menu,bg='#CCFFFF',width=150,height=150)
    Frame_View.pack()
    Frame_View.place(x=325,y=300)

    View_Image=Image.open('view.jpg')
    View_Image=View_Image.resize((100,100))
    View_Image=ImageTk.PhotoImage(View_Image)

    def Button_View_Clicked():
        window_menu.destroy()
        passwords.passwords()

    Button_View=Button(Frame_View,image=View_Image,command=Button_View_Clicked)
    Button_View.pack()
    Button_View.place(x=23,y=23)

    window_menu.mainloop()


# Menu()