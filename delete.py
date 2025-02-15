import os.path
from tkinter import *
from PIL import Image,ImageTk
import utiles
import menu

def delete():
    window_delete=Tk()
    window_delete.title('Passam(Delete)')
    window_delete.geometry('800x500')
    window_delete.resizable(False,False)
    window_delete.configure(bg='#000066')
    window_delete.iconbitmap('icon_kcl_icon.ico')
#________________________________________________________________
    delete_text=Label(window_delete,text='Choose to delete an option',bg='#000066',fg='white',width=25)
    delete_text.pack()
    delete_text_style=('Caveat',35,'bold')
    delete_text.configure(font=delete_text_style)
#__________________________________________________________________________
    passwords_list=Listbox(window_delete,height=12,width=35,bg='white',fg='#04757c')
    passwords_list.pack()
    passwords_list.place(x=150,y=60)
    passwords_list_style=('Arial',17,'bold')
    passwords_list.configure(font=passwords_list_style)


    scrollbar_vertical=Scrollbar(window_delete)
    scrollbar_vertical.place(in_=passwords_list,relx=1,rely=0,relheight=1,anchor='ne')

    scrollbar_horizontal=Scrollbar(window_delete,orient=HORIZONTAL)
    scrollbar_horizontal.place(in_=passwords_list,relx=0,rely=1,relwidth=1,anchor='sw')



    File_All_Password = open('All_Password', 'r')
    File_All_Password = File_All_Password.readlines()
    utiles.load_key_file()
    List_of_Password=File_All_Password


    for item in List_of_Password:
        Password_Decrypt = utiles.fernet.decrypt(item.encode()).decode()
        result = str(List_of_Password.index(item)+1) + '-' + ' ' + Password_Decrypt


        passwords_list.insert(END,result)

    passwords_list.config(yscrollcommand=scrollbar_vertical.set,xscrollcommand=scrollbar_horizontal.set)

    scrollbar_vertical.config(command=passwords_list.yview)
    scrollbar_horizontal.config(command=passwords_list.xview)
#____________________________________________________________________________________________________________
    def delete_button_clicked():
        selected_item=passwords_list.curselection()
        for selected_item in selected_item[::-1]:
            passwords_list.delete(selected_item)


            print(Password_Decrypt[selected_item])
            with open('All_Password','r') as my_file:
                File_All_Password=my_file.readlines()

            File_All_Password.pop(selected_item)

            with open('All_Password','w') as my_file:
                my_file.writelines(File_All_Password)
                my_file.close()

    delete_button=Button(window_delete,text='Delete',bg='red',fg='white',width=17,command=delete_button_clicked)
    delete_button.pack()
    delete_button.place(x=250,y=450)
    delete_button_style=('Centaur',17,'bold')
    delete_button.configure(font=delete_button_style)
#______________________________________________________________________________________________
    back_image_icon = Image.open(os.path.join(os.path.dirname(__file__),'back.png'))
    back_image_icon = back_image_icon.resize((25, 25))
    back_image_icon = ImageTk.PhotoImage(back_image_icon)
    window_delete.back_image_icon=back_image_icon

    def button_back_clicked():
        window_delete.destroy()
        menu.Menu()

    button_back = Button(window_delete,image=back_image_icon, command=button_back_clicked)
    button_back.pack()
    button_back.place(x=40, y=30)


    window_delete.mainloop()


# delete()

