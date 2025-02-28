from tkinter import *

# Created a Function named login_error
def error(title,message):
    # Created a Top Level Named WIN_TOP
    WIN_TOP = Toplevel(bg='#E0D9EF')
    # Set Geometry of Top level WIndow
    WIN_TOP.geometry('300x150')
    # Gave Title to Toplevel Window
    WIN_TOP.title(title)

    # Created destroy_toplevel_login function
    def destroy_toplevel_login():
        '''Destroys Top level when Function is Called'''
        WIN_TOP.destroy()

    #Made a list Contaning properties of font so can be called many times in program.
    tfont_tup = ("Comic Sans MS", 15)

    # Message To Be Displayed at Top Level
    error_message = Label(WIN_TOP, bg='#E0D9EF', text=message, font=tfont_tup,
                          justify="center", foreground="#000000")
    error_message.pack()

    # Cancel Button in Toplevel which calls destroy_toplevel_login when pressed
    error_button_cancel = Button(WIN_TOP, bg='#FFFFFF', text="Cancel", font=("Comic Sans MS", 12),
                                 command=destroy_toplevel_login)
    error_button_cancel.place(x=120, y=80)
    # Update all code into Toplevel window
    WIN_TOP.mainloop()