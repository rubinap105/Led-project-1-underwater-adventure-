#Imported Necessary Modules
from tkinter import *
import sqlite3

# Function Named error_age_register
def error_age_register():
    '''Store title for toplevel in title and message to be displayed at message and calls show_error function providing title and message'''
    title = "Value Error"
    message = "Recheck Your Values\n Before Entering"
    from errors import error as show_error
    show_error(title,message)

#Created Function named error_data_register
def error_data_register():
    '''Store title for toplevel in title and message to be displayed at message and calls show_error function providing title and message'''
    title = "Data Error"
    message = "Please Recheck Your \n Input Data!"
    from errors import error as show_error
    show_error(title, message)

#Created Function named error_data_similar_register
def error_data_similar_register():
    '''Store title for toplevel in title and message to be displayed at message and calls show_error function providing title and message'''
    title = "User Name Found"
    message = "Input Username Already Exist!"
    from errors import error as show_error
    show_error(title, message)

#Function named register_page-Validation
def register_page_validation(name,age,username,password):
    #try.....except to check code
    try:
        #look whether Age Entry is Integer or not
        int(age)
    #Runs except if error occur on try block
    except:
        #Raises an Error
        raise ValueError("Integer Error")
        #Calls for error_age_register
        error_age_register()
    #runs else if try runs properly without error
    else:
        #Connect with database player_details and look for entered username
        #in profile table and if found then call error_data_similar_register
        conn = sqlite3.connect('player_details.db')
        c = conn.cursor()
        c.execute("SELECT *,oid FROM profile")
        records = c.fetchall()
        for record in records:
            if str(username) == str(record[2]):
                error_data_similar_register()
                break
        else:
            #Returns True if Entered Username is not empty and nothing is written
            return len(name) != 0 and name != "Full Name" and len(age) != 0 and age != "Age" and len(username) != 0 and username != "User Name" and len(password) != 0 and password != "Password"

#Function named register_data
def register_data(WIN,name_value,age_value,username_value,password_value):
    #calls register_page_validation and looks whether it return True or False
    if  register_page_validation(name_value,age_value,username_value,password_value):
        #Connect with player_details database and insert all Entered
        #Data into profile table
        conn = sqlite3.connect('player_details.db')
        c = conn.cursor()
        c.execute("INSERT INTO profile VALUES (:full_name, :age, :user_name, :password, :score)",
                  {
                      'full_name': name_value,
                      'age': age_value,
                      'user_name': username_value,
                      'password': password_value,
                      'score':0
                  })
        conn.commit()
        conn.close()

        #Connect with current_user database and insert username in it and store in user_data Table
        conn = sqlite3.connect('current_user.db')
        c = conn.cursor()
        c.execute("INSERT INTO user_data VALUES (:user_name_value)",
                  {
                      'user_name_value': username_value
                  })
        conn.commit()
        conn.close()
        #Calls for start_page
        WIN.destroy()
        from user_profile import profile_view as open_profile
        open_profile()
    #if register_page_validation returns False then
    else:
        #Call for error_data_register
         error_data_register()

#Created a Function Named register Which Stores all the Codes of register Page
# so it can be called later from another program
def register():
    '''Created a Tkinter Window named WIN and placed logo_image as icon photo.
    Similarly,Adding Title to the window and Providing Geaometry to the window.'''
    WIN = Tk()
    logo_image = PhotoImage(file="images/fish2.png")
    WIN.iconphoto(False, logo_image)
    WIN.title('Underwater Adventure')
    WIN.geometry('360x640')

    #Made a list Contaning properties of font so can be called many times in program.
    tfont_tup = ("Comic Sans MS", 15)

    # Placed backround_top.png image as Background to a TKinter Window
    background = PhotoImage(file="images/background_top.png")
    label_background = Label(WIN, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    #Created a Canvas with width and height of 240 and 340 respectively.
    w = Canvas(WIN, width=240, height=340, borderwidth=0, highlightthickness=0)
    #Created a Rectangle in a Canvas with width and height of 240 and 340
    w.create_rectangle(0, 0, 240, 340, fill="#77DC28", outline='#77DC28')
    w.pack(padx=50, pady=145)

    #Function named temp_name with one parameter i.e. 'e'
    def temp_name(e):
        '''Clears name_entry to take user input'''
        name_entry.delete(0, "end")

    #Entry Box to take name Input from user
    name_entry = Entry(WIN, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    name_entry.insert(0, "Full Name")
    #Bind Entry so that when Clicked for Input it calls temp_name
    name_entry.bind("<FocusIn>",temp_name)
    name_entry.place(x=87, y=180)

    #Function named temp_age with one parameter i.e. 'e'
    def temp_age(e):
        '''Clears age_entry to take user input'''
        age_entry.delete(0, "end")

    #Entry Box to take age Input from user
    age_entry = Entry(WIN, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    age_entry.insert(1, "Age")
    #Bind Entry so that when Clicked for Input it calls temp_nge
    age_entry.bind("<FocusIn>",temp_age)
    age_entry.place(x=87, y=230)

    #Function named temp_username with one parameter i.e. 'e'
    def temp_username(e):
        '''Clears username_entry to take user input'''
        username_entry.delete(0, "end")

    #Entry Box to take username Input from user
    username_entry = Entry(WIN, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    username_entry.insert(2, "User Name")
    #Bind Entry so that when Clicked for Input it calls temp_username
    username_entry.bind("<FocusIn>",temp_username)
    username_entry.place(x=87, y=280)

    #Function named temp_password with one parameter i.e. 'e'
    def temp_password(e):
        '''Clears password_entry to take user input and configured it to show * when anything is enterd'''
        password_entry.config(show="*")
        password_entry.delete(0, "end")

    #Entry Box to take password Input from user
    password_entry = Entry(WIN, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    password_entry.insert(0, "Password")
    #Bind Entry so that when Clicked for Input it calls temp_password
    password_entry.bind("<FocusIn>",temp_password)
    password_entry.place(x=87,y=330)

    #Button which when pressed calls register_data
    register_button = Button(WIN, font=tfont_tup, justify="center", width=10, borderwidth=0, text="Register",bg="#DD3939",command=lambda: register_data(WIN,name_entry.get(),age_entry.get(),username_entry.get(),password_entry.get()))
    register_button.place(x=110, y=395)

    #places all GUI into Tkinter Window
    WIN.mainloop()

#calls register function to execute
register()