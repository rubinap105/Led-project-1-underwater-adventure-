#imported necessary modules
from tkinter import *

#Created a Function Named game_finish Which Stores all the Codes of game_over Page
# so it can be called later from another program
def game_finish():
    '''Created a Tkinter Window named WIN_ and placed logo_image as icon photo.
        Similarly,Adding Title to the window and Providing Geometry to the window.'''
    WIN = Tk()
    logo_image = PhotoImage(file="images/fish2.png")
    WIN.iconphoto(False, logo_image)
    WIN.title('Underwater Adventure')
    WIN.geometry('360x640')

    # Placed gameover.png image as Background to a TKinter Window
    background = PhotoImage(file="images/gameover.png")
    label_background = Label(WIN,image=background,borderwidth=0)
    label_background.place(x=0,y=0)

    #List with properties of font
    tfont_tup = ("Comic Sans MS", 13)

    #function named home which destroys current Tkinter Window and calls start_game i.e. profile_view from profile page
    def home():
        WIN.destroy()
        from profile import profile_view as start_game
        start_game()

    #function named exitpage which quit program on execution
    def exitpage():
        quit()

    #homepage button which calls home function on pressing
    homepage = Button(WIN,text="Profile",padx=10,borderwidth=0,font=tfont_tup,background= 'red', foreground= 'black',command=home)
    homepage.place(x = 133,y = 350)
    #quit button which calls exitpage on pressing
    quit_button = Button(WIN,text="Quit",padx=10,borderwidth=0,font=tfont_tup,background= 'green3', foreground= 'black',command=exitpage)
    quit_button.place(x=140,y=425)

    #places all GUI of Tkinter window into it.
    WIN.mainloop()

#calls game_finish
game_finish()