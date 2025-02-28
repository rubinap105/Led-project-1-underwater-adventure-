#Imported Necessary Modules
from tkinter import *
import sqlite3
from tkinter import ttk


# Bubble Sort Function which arrange number according to ascending order
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            value1 = nums[i]
            value2 = nums[i + 1]
            if value1[1] < value2[1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

def data_not_found():
    '''Store title for toplevel in title and message to be displayed at message and calls show_error function providing title and message'''
    title = "Username Not Found"
    message = "Input Username was\n not Found"
    from errors import error as show_error
    show_error(title, message)

#Created a Function Named leaderboard Which Stores all the Codes of leaderboard Page
# so it can be called later from another program
def leaderboard():
    '''Created a Tkinter Window named WIN_leaderboard and placed logo_image as icon photo.
    Similarly,Adding Title to the window and Providing Geometry to the window.'''
    WIN_leaderboard = Tk()
    logo_image = PhotoImage(file="images/fish2.png")
    WIN_leaderboard.iconphoto(False, logo_image)
    WIN_leaderboard.title('Underwater Adventure')
    WIN_leaderboard.geometry('360x640')

    # Placed backround_top.png image as Background to a Tkinter Window
    background = PhotoImage(file="images/background_top.png")
    label_background = Label(WIN_leaderboard, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    #Created a Canvas with width and height of 240 and 400 respectively.
    w = Canvas(WIN_leaderboard, width=240, height=400, borderwidth=0, highlightthickness=0)
    #Created a Rectangle in a Canvas with width and height of 240 and 400
    w.create_rectangle(0, 0, 240, 400, fill="#77DC28", outline='#77DC28')
    w.pack(padx=(50,50), pady=(135,80))



    #List contaning properties of font
    tfont_tup = ("Comic Sans MS", 12)

    #Created a TreeView To show Scores Data
    tv = ttk.Treeview(WIN_leaderboard, show='tree', height=13)
    #Set theme of TreeView as Default
    ttk.Style().theme_use("default")
    #Configured Properties of Tree View
    ttk.Style().configure("Treeview", background="#77DC28",foreground="black",fieldbackground="#77DC28", rowheight=28,font = tfont_tup, highlightthickness=0, bd=0,padding=10)
    ttk.Style().map("Treeview",background=[('selected','#77DC28')],foreground=[('selected','black')])
    #Added Name to columns
    tv['columns']=('Name', 'Score')
    #Added teext to column
    tv.column('#0', width=0, stretch=NO)
    tv.column('Name', anchor=W, width=130)
    tv.column('Score', anchor=E, width=88)


    #Connect player_details databse and store all data of profile into record_data
    conn = sqlite3.connect('player_details.db')
    c1 = conn.cursor()
    c1.execute("SELECT *,oid FROM profile")
    records_data = c1.fetchall()
    conn.commit()
    conn.close()

    #Created scoreboard as blank list
    scoreboard = []
    #for loop to go in every value of records_data
    for record in records_data:
        #create a list with username and score and named as scores
        scores = (record[2],record[4])
        #append it into scoreboard
        scoreboard.append(scores)

    bubble_sort(scoreboard)
    #duplicates scoreboard list into orginal_scoreboard
    orginal_scoreboard = scoreboard.copy()
    #Calculated length of list
    orginal_length = len(scoreboard)
    #Check if Statement is Correct or not
    if orginal_length > 7:
        #stores new length as how much orginal_length is more than 7
        new_length = orginal_length - 7
        #Calls for loop to pop all items after index 7
        for i in range(new_length):
            scoreboard.pop()

    a = 0
    #insert Data from a list of Scoreboard
    for score_data in scoreboard:
        tv.insert(parent='', index=a, iid=a, text='', values=score_data)
        a = a+1
    tv.place(x=60,y=170)

    #list contaning proerties for font
    tfont_tup = ("Comic Sans MS", 15)

    #Created Rectangle with width of 240 and height of 35
    w.create_rectangle(0, 0, 240, 35,outline="#fb0",fill="#E9FA2A")
    #Created a text named Leaderboard
    leaderboard_label = Label(WIN_leaderboard, text="Leaderboard", font=tfont_tup, justify="center", background="#E9FA2A")
    leaderboard_label.place(x=115,y=135)

    #function named Search
    def search():
        try:
            #for loop which runs till there is a value in orginal_scoreboard list
            for value in orginal_scoreboard:
                #looks if user entered username is there in list
                if username_search.get() == value[0]:
                    #deletes all data shown in leaderboard
                    for item in tv.get_children():
                        tv.delete(item)
                    #show Data of Found User Only
                    tv.insert(parent='', index=1, iid=1, text='', values=value)
                    #breaks the loop
                    break
                #if enterd username is not matched with value and is blank then this executes
                elif username_search.get() == "":
                    #Deletes All Data of Scoreboard
                    for item in tv.get_children():
                        tv.delete(item)
                    b = 1
                    #Again Insert all values into leaderboard acording to descending order of scores
                    for score_data in scoreboard:
                        tv.insert(parent='', index=b, iid=b, text='', values=score_data)
                        b = b + 1
                    #breaks loop
                    break
            #if value is not found in orginal_scoreboard list
            else:
                #raises a Errror
                raise ValueError('Value Not found')
        #runs this part of code if error occured
        except:
            #Calls data_not_foound
            data_not_found()

    #function named reback which destroys Tkinter window and calls p function .i.e. profile_view from profile page
    def reback():
        WIN_leaderboard.destroy()
        from user_profile import profile_view as p
        p()

    #Place to Enter Username to search for
    username_search = Entry(WIN_leaderboard, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    username_search.place(x=87, y=395)
    #Text Displayed in Entry bar so User Know What to look for
    username_search.insert(1,"Enter User Name")
    #Search button which when pressed calls search
    search_button = Button(WIN_leaderboard, text="Search", padx=10, borderwidth=0, font=tfont_tup, background='green3', foreground='black', command=search)
    search_button.place(x = 135,y = 438)
    #return button which when pressed calls reback
    return_button = Button(WIN_leaderboard, text="Return", padx=10, borderwidth=0, font=tfont_tup, background='green3', foreground='black', command=reback)
    return_button.place(x = 140,y = 493)

    #Places all GUI of Tkinter Window into it.
    WIN_leaderboard.mainloop()

#Calls Leaderboard Function
leaderboard()