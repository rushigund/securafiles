from tkinter import *
from pymysql import connect

# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global repass
    global username_entry
    global password_entry


    username = StringVar()
    password = StringVar()
    repass   = StringVar()


    password_1 = password.get()  # Retrieve password from entry field
    password_2 = repass.get()  # Same but for re-entered password
    print(password_1 == password_2)

    Label(register_screen, text="Please enter details below", bg="green").pack()
    Label(register_screen, text="").pack()

    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()

    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()

    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    password_lable = Label(register_screen, text="Re-enter Password * ")
    password_lable.pack()

    repassword_entry = Entry(register_screen, textvariable=repass, show='*')
    repassword_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="green", command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()



# Implementing event on register button

def register_user():
     username_info = username.get()
     password_info = password.get()


     connection = connect(host = "localhost", user = "root", password = "root", db ="mylogin")
     cur       = connection.cursor()
     query      = "insert into accounts(username,mypassword)  VALUES(%s, %s)"
     cur.execute(query,(username_info,password_info,))
     connection.commit()
     connection.close()
     Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()



# Implementing event on login button

def login_verify():

    connection = connect(host = "localhost", user = "root", password = "root", db ="mylogin")
    cury       = connection.cursor()

    while True:
        username1 = username_verify.get()
        password1 = password_verify.get()
        query_1   = "select * from accounts where username = %s and mypassword = %s"
        cury.execute(query_1,(username1,password1))
        check     = cury.fetchall()
        connection.commit()
        connection.close()

        if check:
            Label(login_screen, text="Login Success", fg="green", font=("calibri", 11)).pack()

            break


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="orange", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()

