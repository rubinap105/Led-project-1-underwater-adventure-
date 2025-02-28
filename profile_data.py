#Imported Necessary Modules
from tkinter import *
import sqlite3


#Function named delete_profile
def delete_profile(WIN,record_id):
    '''Created TopLevel as WIN_top,providing its geometry and title.'''
    WIN_top = Toplevel(bg='#E0D9EF')
    WIN_top.title('Delete Profile')
    WIN_top.geometry('300x150')

    #Made a list Contaning properties of font so can be called many times in program.
    tfont_tup = ("Comic Sans MS", 15)

    #function named yes
    def yes(WIN,record_id):
        '''Connect with database player_details and Deletes every record
        of the player when function is called'''
        conn = sqlite3.connect('player_details.db')
        c = conn.cursor()
        c.execute("DELETE from profile where oid = ?", str(record_id))
        conn.commit()
        conn.close()

        #Destroys Toplevel Window
        WIN_top.destroy()

        # Destroys Current Tkinter Window and calls
        # run_game i.e. game function from main page
        WIN.destroy()
        from game import game as run_game
        run_game()

    #function named no which when called destroys Toplevel
    def no():
        WIN_top.destroy()

    #Message to be Displayed at Toplevel
    message = Label(WIN_top, bg='#E0D9EF', text="Are you sure you \n want to delete?", font=tfont_tup, justify="center",
                        foreground="#000000")
    message.pack()

    #Yes Button of Toplevel which when pressed calls yes function
    yes_button = Button(WIN_top, bg='#FFFFFF', text=" Yes ", font=("Comic Sans MS", 12), command=lambda : yes(WIN,record_id))
    yes_button.place(x=40, y=80)

    #No Button which when pressed calls no function
    no_button = Button(WIN_top, bg='#FFFFFF', text=" No ", font=("Comic Sans MS", 12), command=no)
    no_button.place(x=200, y=80)

    #Places all GUI of Toplevel into it
    WIN_top.mainloop()

#Created a Function Named profile_data Which Stores all the Codes of profile_data Page
# so it can be called later from another program
def profile_data():
    '''Created a Tkinter Window named WIN and placed logo_image as icon photo.
    Similarly,Adding Title to the window and Providing Geometry to the window.'''
    WIN = Tk()
    logo_image = PhotoImage(file="images/fish2.png")
    WIN.iconphoto(False, logo_image)
    WIN.title('Underwater Adventure')
    WIN.geometry('360x640')

    # Made a list Contaning properties of font so can be called many times in program.
    tfont_tup = ("Comic Sans MS", 15)

    #Connected with current_user database and stores all data of user_data
    #table into records as a list
    conn = sqlite3.connect('current_user.db')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM user_data")
    record = c.fetchall()
    conn.commit()
    conn.close()

    #Connected with player_details database and stores all data of profile
    #table into records_data as a list
    conn = sqlite3.connect('player_details.db')
    c1 = conn.cursor()
    c1.execute("SELECT *,oid FROM profile")
    records_data = c1.fetchall()
    conn.commit()
    conn.close()

    #For loop to go in every data of list named record
    for record_user in record:
        #For loop to go in every data of list records_data
        for record_profile in records_data:
            #looks whether data of list record matches with data of list records_data
            # and stores all values in profile table of player_details database into name_value
            #age_value,username_value,password_value,record_id respectively
            if str(record_user[0]) == str(record_profile[2]):
                name_value = record_profile[0]
                age_value = record_profile[1]
                username_value = record_profile[2]
                password_value = record_profile[3]
                record_id = record_profile[5]

    # Placed backround_top.png image as Background to a Tkinter Window
    background = PhotoImage(file="images/background_top.png")
    label_background = Label(WIN, image=background, borderwidth=0)
    label_background.place(x=0, y=0)

    #Created a Canvas with width and height of 240 and 320 respectively.
    w = Canvas(WIN, width=240, height=320, borderwidth=0, highlightthickness=0)
    #Created a Rectangle in a Canvas with width and height of 240 and 320
    w.create_rectangle(0, 0, 240, 320, fill="#77DC28", outline='#77DC28')
    w.pack(padx=50, pady=145)

    #Entry Box to take name Input from user
    name_entry = Entry(WIN, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    name_entry.insert(1,name_value)
    #configured Entry Box as Disabled to not let user to provide input
    name_entry.config(state="disabled")
    name_entry.place(x=87, y=180)
    #Entry Box to take age Input from user
    age_entry = Entry(WIN, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    age_entry.insert(1,age_value)
    #configured Entry Box as Disabled to not let user to provide input
    age_entry.config(state="disabled")
    age_entry.place(x=87, y=230)
    #Entry Box to take username Input from user
    username_entry = Entry(WIN, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    username_entry.insert(1,username_value)
    #configured Entry Box as Disabled to not let user to provide input
    username_entry.config(state="disabled")
    username_entry.place(x=87, y=280)
    #Entry Box to take password Input from user
    password_entry = Entry(WIN, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    password_entry.insert(1,password_value)
    #configured Entry Box as Disabled to not let user to provide input
    password_entry.config(state="disabled")
    password_entry.place(x=87, y=330)

    # function named edit_profile which Destroys Current Tkinter Window and calls
    # edit i.e. profile_edit function from profile_edit page
    def edit_profile():
        WIN.destroy()
        from profile_edit import profile_edit as edit
        edit()

    #Button with edit as a image which when press calls edit_profile
    edit = PhotoImage(file="images/edit.png")
    edit_button = Button(WIN,image=edit,borderwidth=0,highlightthickness=0,bd=0,background='#085895',command=edit_profile)
    edit_button.place(x=100,y=400)

    #Button with delete as a image which when press calls delete_profile
    delete = PhotoImage(file="images/delete.png")
    delete_button = Button(WIN,image=delete,borderwidth=0,highlightthickness=0,bd=0,background='#085895',command=lambda : delete_profile(WIN,record_id))
    delete_button.place(x=230,y=400)

    #Places all GUI of Tkinter Window Into it
    WIN.mainloop()

#calls for profile_data
profile_data()