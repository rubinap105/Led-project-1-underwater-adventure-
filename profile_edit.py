#Imported Necessary Modules
from tkinter import *
import sqlite3
import re
import sqlite3
from tkinter import messagebox

def update_user_profile(username, email, phone_number):
    """ Updates the user profile in the database after validation. """
    try:
        conn = sqlite3.connect('player_details.db')
        c = conn.cursor()

        # Assuming there's a 'profile' table with columns: username, email, phone_number, etc.
        c.execute("""
            UPDATE profile
            SET email = ?, phone_number = ?
            WHERE username = ?
        """, (email, phone_number, username))

        conn.commit()
        conn.close()

        # Inform the user that the profile has been successfully updated
        messagebox.showinfo("Success", "Your profile has been updated successfully.")
    
    except Exception as e:
        messagebox.showerror("Database Error", f"An error occurred while updating the profile: {e}")




# Created Function named error_data_profile
def error_age_profile():
    '''Store title for toplevel in title and message to be displayed at message and calls show_error function providing title and message'''
    title = "Value Error"
    message = "Recheck Your Values\n Before Entering"
    from errors import error as show_error
    show_error(title,message)

# Created Function named error_data_profile
def error_data_profile():
    '''Store title for toplevel in title and message to be displayed at message and calls show_error function providing title and message'''
    title = "Value Error"
    message = "Please Recheck Your \n Input Data"
    from errors import error as show_error
    show_error(title,message)

#Function named register_page-Validation
def register_page_validation(name,age,username,password):
    #try.....except to check code
    try:
        #look whether Age Entry is Integer or not
        int(age)
    #Runs except if error occur on try block
    except:
        #Calls for error_age_register
        error_age_profile()
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
                error_data_similar_profile()
                break
        else:
            #Returns True if Entered Username is not empty and nothing is written
            return len(name) != 0 and name != "Full Name" and len(age) != 0 and age != "Age" and len(username) != 0 and username != "User Name" and len(password) != 0 and password != "Password"


# Created Function named error_data_similar_profile
def error_data_similar_profile():
    '''Store title for toplevel in title and message to be displayed at message and calls show_error function providing title and message'''
    title = "Value Error"
    message = "Input Username Already Exist"
    from errors import error as show_error
    show_error(title,message)

# Created Function named database_error
def database_error():
    '''Store title for toplevel in title and message to be displayed at message and calls show_error function providing title and message'''
    title = "Database Error"
    message = "Unknown Error Occured\n on Database"
    from errors import error as show_error
    show_error(title,message)


#Function named update_data
def update_data(WIN_edit,value_name,value_age,value_username,value_password,id_record):
    #if then Statement and calls profile_page_validation which either returns True or False
    if register_page_validation(value_name,value_age,value_username,value_password):
        #Suspected Code in try block
        try:

            #Connected with current_user database and stores all data of user_data
            #table into records as a list
            conn = sqlite3.connect('current_user.db')
            c = conn.cursor()
            c.execute("SELECT *,oid FROM user_data")
            records_user = c.fetchall()
            conn.commit()
            conn.close()

            #Connected with player_details database and stores all data of profile
            #table into records_data as a list
            conn = sqlite3.connect('player_details.db')
            c1 = conn.cursor()
            c1.execute("SELECT *,oid FROM profile")
            records_profile = c1.fetchall()
            conn.commit()
            conn.close()

            #Checks Which username of current_user matches with username in player_details and updates information into it.
            for record_user in records_user:
                for record_profile in records_profile:
                    if str(record_user[0]) == str(record_profile[2]):
                        conn = sqlite3.connect('player_details.db')
                        c = conn.cursor()
                        data_to_be_updated = '''UPDATE profile
                                                SET full_name = ?,
                                                    age = ?,
                                                    user_name = ?,
                                                    password = ?
                                                WHERE oid = ?'''
                        data = (value_name,value_age,value_username,value_password,id_record)
                        c.execute(data_to_be_updated,data)
                        conn.commit()
                        conn.close()
        #if error occured on suspected code
        except:
            #calls database_error
            database_error()
        #Runs if suspected code runs well
        else:
            # function named start_page which Destroys Current Tkinter Window and calls
            # view_profile i.e. profile_view function from profile page
            WIN_edit.destroy()
            from user_profile import profile_view as view_profile
            view_profile()
    #if validation is not met
    else:
        #calls error_data_register
        error_data_profile()

#Created a Function Named profile_data Which Stores all the Codes of profile_data Page
# so it can be called later from another program
def profile_edit():
    '''Created a Tkinter Window named WIN_edit and placed logo_image as icon photo.
    Similarly,Adding Title to the window and Providing Geometry to the window.'''
    WIN_edit = Tk()
    logo_image = PhotoImage(file="images/fish2.png")
    WIN_edit.iconphoto(False, logo_image)
    WIN_edit.title('Underwater Adventure')
    WIN_edit.geometry('360x640')

    # Made a list Contaning properties of font so can be called many times in program.
    tfont_tup = ("Comic Sans MS", 15)


    #Connect with database player_details and stores all values of profile table into records_profile
    conn = sqlite3.connect('player_details.db')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM profile")
    records_profile = c.fetchall()
    conn.commit()
    conn.close()

    #Connect with database currrent_user and stores all values of user_data table into records_user
    conn = sqlite3.connect('current_user.db')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM user_data")
    records_user = c.fetchall()
    conn.commit()
    conn.close()

    # looks whether data of list record_user matches with data of list records_profile
    # and stores all values record_profile into name_value,age_value,username_value,password_value,record_id respectively
    for record_user in records_user:
        for record_profile in records_profile:
            if str(record_user[0]) == str(record_profile[2]):
                name_value = record_profile[0]
                age_value = record_profile[1]
                username_value = record_profile[2]
                password_value = record_profile[3]
                record_id = record_profile[5]

    # Placed backround_top.png image as Background to a TKinter Window
    background = PhotoImage(file="images/background_top.png")
    label_background = Label(WIN_edit, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    #Created a Canvas with width and height of 240 and 320 respectively.
    w = Canvas(WIN_edit, width=240, height=320, borderwidth=0, highlightthickness=0)
    #Created a Rectangle in a Canvas with width and height of 240 and 320
    w.create_rectangle(0, 0, 240, 320, fill="#77DC28", outline='#77DC28')
    w.pack(padx=50, pady=145)

    #Entry to take name entry to be updated
    name_entry = Entry(WIN_edit, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    name_entry.place(x=87, y=180)
    #Entry to take age entry to be updated
    age_entry = Entry(WIN_edit, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    age_entry.place(x=87, y=230)
    #Entry to take username entry to be updated
    username_entry = Entry(WIN_edit, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    username_entry.place(x=87, y=280)
    #Entry to take password entry to be updated
    password_entry = Entry(WIN_edit, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    password_entry.place(x=87, y=330)

    #Inserted name_value,age_value,username_value,password_value taken from database into name_age
    #,age_entry,username_entry,password_entry respectively
    name_entry.insert(1,name_value)
    age_entry.insert(1,age_value)
    username_entry.insert(1,username_value)
    password_entry.insert(1,password_value)

    #Update Button which when calls update_data
    update_button = Button(WIN_edit, font=tfont_tup, justify="center", width=10, borderwidth=0, text="Update", bg="#DD3939",
                           command=lambda : update_data(WIN_edit,name_entry.get(),age_entry.get(),username_entry.get(),password_entry.get(),record_id))
    update_button.place(x=110, y=395)

    #Places all GUI of TKinter Window in it
    WIN_edit.mainloop()

#calls profile_edit
profile_edit()