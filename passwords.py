from tkinter import *
from PIL import Image, ImageTk
import menu
import utiles


def passwords():
    window_passwords = Tk()
    window_passwords.title('Passam(Passwords List)')
    window_passwords.geometry('800x500')
    window_passwords.iconbitmap('icon_kcl_icon.ico')
    window_passwords.configure(bg='#000066')
    window_passwords.resizable(False, False)
    # ________________________________________________________________________
    passwords_list_text = Label(window_passwords, text='Passwords List', bg='#000066', fg='white', width=15)
    passwords_list_text.pack()
    passwords_list_text_style = ('Caveat', 40, 'bold')
    passwords_list_text.configure(font=passwords_list_text_style)
    # _____________________________________________________________________________
    passwords_list_image = Image.open('passwords_list.png')
    passwords_list_image = passwords_list_image.resize((310, 300))
    tk_passwords_list_image = ImageTk.PhotoImage(passwords_list_image)
    passwords_list_image_label = Label(window_passwords, image=tk_passwords_list_image)
    passwords_list_image_label.place(x=30, y=120)
    # __________________________________________________________________________________
    back_button_image = Image.open('back.png')
    back_button_image = back_button_image.resize((25, 25))
    back_button_image = ImageTk.PhotoImage(back_button_image)

    def back_button_clicked():
        window_passwords.destroy()
        menu.Menu()

    back_button = Button(window_passwords, image=back_button_image, command=back_button_clicked)
    back_button.pack()
    back_button.place(x=40, y=30)

    def View_All_Password():
        global File_All_Password
        File_All_Password = open('All_Password', 'r')
        File_All_Password=File_All_Password.readlines()
        utiles.load_key_file()

    View_All_Password()
    List_of_Password = File_All_Password

    List_Password = Listbox(window_passwords, height=13, width=32, bg='white', fg='#04757c')
    List_Password.pack()
    List_Password.place(x=360,y=115)
    List_Password_Style=('Arial',17,'bold')
    List_Password.configure(font=List_Password_Style)

    scrollbar_vertical=Scrollbar(List_Password)
    scrollbar_vertical.place(in_=List_Password,relx=1,rely=0,relheight=1,anchor='ne')

    scrollbar_horizontal=Scrollbar(List_Password,orient=HORIZONTAL)
    scrollbar_horizontal.place(in_=List_Password,relx=0,rely=1,relwidth=1,anchor='sw')

    for item in List_of_Password:
        Password_Decrypt = utiles.fernet.decrypt(item.encode()).decode()
        result = str(List_of_Password.index(item)+1) + '-' + ' ' + Password_Decrypt
        List_Password.insert(END,result)

    List_Password.config(yscrollcommand=scrollbar_vertical.set,xscrollcommand=scrollbar_horizontal.set)

    scrollbar_vertical.config(command=List_Password.yview)
    scrollbar_horizontal.config(command=List_Password.xview)

    window_passwords.mainloop()

# passwords()
