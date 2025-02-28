from tkinter import *
import tkinter.font as tfont

#Created a Function Named profile_view Which Stores all the Codes of profile Page
# so it can be called later from another program
def profile_view():
   '''Created a Tkinter Window named WIN and placed logo_image as icon photo.
   Similarly,Adding Title to the window and Providing Geaometry to the window.'''
   WIN = Tk()
   logo_image = PhotoImage(file="images/fish2.png")
   WIN.iconphoto(False, logo_image)
   WIN.title('Underwater Adventure')
   WIN.geometry('360x640')

   # Placed backround.png image as Background to a TKinter Window
   background = PhotoImage(file="images/background.png")
   label_background = Label(WIN,image=background,borderwidth=0)
   label_background.place(x=0,y=0)

   #function named game_play which Destroys Current Tkinter Window and calls
   # run_game i.e. game function from main page
   def game_play():
      WIN.destroy()
      from main import game as run_game
      run_game()

   # function named leader which Destroys Current Tkinter Window and calls
   # show_score i.e. leaderboard from leaderboard page
   def leader():
      WIN.destroy()
      from leaderboard import leaderboard as show_score
      show_score()

   # function named data_profile which Destroys Current Tkinter Window and calls
   # open_data i.e. profile_data function from profile_data page
   def data_profile():
      WIN.destroy()
      from profile_data import profile_data as open_data
      open_data()

   #Created a Button with Image profile_image and calls data_profile when clicked
   profile_image = PhotoImage(file="images/profileimg.png")
   profile_button = Button(WIN,image=profile_image,borderwidth=0,highlightthickness=0,bd=0,background='#085895',command=data_profile)
   profile_button.place(x=260,y=17)

   # Made a list Contaning properties of font so can be called many times in program.
   tfont_tup = ("Comic Sans MS", 13)

   # Created a Function named on_enter_play with 'e' as one parameter
   def on_enter_play(e):
      '''Changed Background and Foreground of play Button named play_button
      to #ABBC41 and white respectively when function is called.'''
      play_button.config(background='#ABBC41',foreground= "white")

    # Created a Function named on_leave_register with 'e' as one parameter
   def on_leave_play(e):
      '''Changed Background and Foreground of Play Button named play_button to
      green3 and black respectively when function is called.'''
      play_button.config(background= 'green3', foreground= 'black')

   #Button which when press calls game_play
   play_button = Button(WIN,text="Play",padx=10,borderwidth=0,font=tfont_tup,background= 'green3', foreground= 'black',command=game_play)
   play_button.place(x = 153,y = 350)
   #Created a Bind i.e. When Entered inside a Play button calls on_enter_play function
   #and when leaves the Play button calls on_leave_play function
   play_button.bind('<Enter>',on_enter_play)
   play_button.bind('<Leave>',on_leave_play)

   # Created a Function named on_enter_leaderboard with 'e' as one parameter
   def on_enter_leaderboard(e):
      '''Changed Background and Foreground of leaderboard Button named leaderboard_button
      to #ABBC41 and white respectively when function is called.'''
      leaderboard_button.config(background='#ABBC41',foreground= "white")

    # Created a Function named on_leave_leaderboard with 'e' as one parameter
   def on_leave_leaderboard(e):
      '''Changed Background and Foreground of Leaderboard Button named leaderboard_button to
      green3 and black respectively when function is called.'''
      leaderboard_button.config(background= 'green3', foreground= 'black')
   #Leaderboard Button which when pressed calls leader
   leaderboard_button = Button(WIN,text="Leaderboard",padx=10,borderwidth=0,font=tfont_tup,background= 'green3', foreground= 'black',command=leader)
   leaderboard_button.place(x=115,y=425)
   #Created a Bind i.e. When Entered inside a Leaderboard button calls on_enter_leaderboard function
   #and when leaves the Leaderboard button calls on_leave_leaderboard function
   leaderboard_button.bind('<Enter>',on_enter_leaderboard)
   leaderboard_button.bind('<Leave>',on_leave_leaderboard)

   WIN.mainloop()

profile_view()