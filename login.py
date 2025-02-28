#Imported Necessary Modules
from tkinter import *
import sqlite3

# Created a function named login_validation
def login_validation(username, password):
    '''Checks Whether Username and Password Entry is Entered or not
    and Returns True if Username and Password is entered or Flase if not.'''
    return len(username) != 0 and username != "User Name" and len(password) != 0 and password != "Password"

#Created Function namedlogin_error
def login_data_error():
    '''Store title for toplevel in title and message to be displayed at message and calls show_error function providing title and message'''
    title = "Error"
    message = "Recheck Your Input\n Values"
    from errors import error as show_error
    show_error(title,message)


# Create a Function named login_validate
def login_validate(WIN,username_value, password_value):
    '''Calls for login_validation an dif returns True then connect with player_details Database and store all data from
    profile table into records and insert record of username into user_data Table of current_user databse if Username and password matches
    in profile'''
    if login_validation(username_value, password_value):
        conn = sqlite3.connect('player_details.db')
        c = conn.cursor()
        c.execute("SELECT *,oid FROM profile")
        records = c.fetchall()
        conn.commit()
        conn.close()
        conn = sqlite3.connect('current_user.db')
        c = conn.cursor()
        try:
            for record in records:
                if str(username_value) == str(record[2]) and str(password_value) == str(record[3]):
                    c.execute("INSERT INTO user_data VALUES (:user_name_value)",
                              {
                                  'user_name_value': username_value
                              })
                    conn.commit()
                    conn.close()
                    #Destroys the tkinter window and call open_profile function i.e. profile_view function from a profile page
                    WIN.destroy()
                    from user_profile import profile_view as open_profile
                    open_profile()
                    #breaks for loop
                    break
            else:
                raise ValueError('Value Not Found')
        except:
            login_error()
    else:
        login_data_error()


#Created a Function Named login Which Stores all the Codes of Login Page
# so it can be called later from another program
def login():
    # Created a Tkinter Window named WIN
    WIN = Tk()
    # Placed Image as Iconphoto on Window
    logo_image = PhotoImage(file="images/fish2.png")
    WIN.iconphoto(False, logo_image)
    #Named Tkinter Window
    WIN.title('Underwater Adventure')
    #Set size of Tkinter Window
    WIN.geometry('360x640')

    # Created register_page function
    def register_page():
        '''Destroys Tkinter Window named WIN and calls page_register
        from register program'''
        WIN.destroy()
        from register import register as page_register
        page_register()

    #Made a list Contaning properties of font so can be called many times in program.
    tfont_tup = ("Comic Sans MS", 15)
    # Placed backround.png image as BAckground to a TKinter Window
    background = PhotoImage(file="images/background_top.png")
    label_background = Label(WIN, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    #Created a Canvas with width and height of 350 and 300 respectively.
    w = Canvas(WIN, width=350, height=300, borderwidth=0, highlightthickness=0)
    #Created a Rectangle in a Canvas with width and height of 350 and 300
    w.create_rectangle(0, 0, 350, 300, fill="#77DC28", outline='#77DC28')
    w.pack(padx=50, pady=160)

    #Function named temp_username with one parameter i.e. 'e'
    def temp_username(e):
        '''Clears username_entry to take user input'''
        username_entry.delete(0, "end")

    #Entry Box to  take Username Input from user
    username_entry = Entry(WIN, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    username_entry.insert(2, "User Name")
    #Bind Entry so that when Clicked for Input it calls temp_username
    username_entry.bind("<FocusIn>", temp_username)
    username_entry.place(x=85, y=190)

    #Function named temp_password with one parameter i.e. 'e'
    def temp_password(e):
        '''Clears password_entry to take user input and configured password entry to show * when password is entered.'''
        password_entry.config(show="*")
        password_entry.delete(0, "end")
    #Entry Box to take Password Input from user
    password_entry = Entry(WIN, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    password_entry.insert(0, "Password")
    #Bind Entry so that when Clicked for Input it calls temp_password
    password_entry.bind("<FocusIn>", temp_password)
    password_entry.place(x=85, y=260)
    #Log in Which when pressed calls login_validate by providing userentry as arguments
    login_button = Button(WIN, font=tfont_tup, justify="center", width=10, borderwidth=0, text="Log In", bg="#DD3939",command=lambda : login_validate(WIN,username_entry.get(),password_entry.get()))
    login_button.place(x=110, y=330)
    # Register in Which when pressed calls register
    register_button = Button(WIN, font=tfont_tup, justify="center", width=10, borderwidth=0, text="New User ?", bg="#DD3939",
                          command=register_page)
    register_button.place(x=110, y=400)

    #Updates GUI Into TKinter Window
    WIN.mainloop()

#calls Login function
login()