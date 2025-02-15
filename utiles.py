from cryptography.fernet import Fernet

File_Check_User = open('Check_New_User.txt', 'a')
File_Check_User = open('Check_New_User.txt', 'r')


def Write_value_checkuser():
    File_Check_User = open('Check_New_User.txt', 'w')
    File_Check_User.write('1')
    File_Check_User.close()



def write_key_file():
    if File_Check_User.read()=='':
     key = Fernet.generate_key()
     with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key_file():
    global fernet
    with open("key.key", "rb") as key_file:
        key = key_file.read()
        key_file.close()
        fernet=Fernet(key)

def check_new_user():
    with open('Check_New_User.txt', 'r') as file:
        return file.read().strip() == ""

def check_App_Password():
    global App_Password_Decrypt

    File_App_Password=open('App_Password','r')
    File_App_Password=File_App_Password.read()

    load_key_file()
    App_Password_Decrypt=fernet.decrypt(File_App_Password.encode()).decode()

