from tkinter import *
import os
from pygame import mixer
import tkinter.messagebox
from tkinter import filedialog

# Create window
root = Tk()

# Create Menu_bar
menu_bar = Menu(root)
root.config(menu=menu_bar)


# Functions


# Function for setting volume
def set_volume_scale(val):
    value = int(val) / 100  # val will be automatically assigned as per the value from scale
    mixer.music.set_volume(value)  # set_volume takes value from 0-1


# Function for browsing file
def browse_file():
    global filename
    filename = filedialog.askopenfilename()


# print(file)


# Function for playing music
def play_music():
    # print("Button clicked")
    try:
        paused  # Checked whether paused variable initialized or not
    except:
        try:
            mixer.music.load(filename)
            # statusbar['text'] = 'Playing music' + ' ' + filename # Shows the path in bottom status bar
            statusbar['text'] = 'Playing music' + ' ' + os.path.basename(
                filename)  # Shows the filename in bottom status bar
            mixer.music.play()
        except:
            # print("Select a file ")
            tkinter.messagebox.showerror('File not selected', 'Select a file first')
    else:
        mixer.music.unpause()
        statusbar['text'] = 'music has been resumed'


# Functions for pausing the music
def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = 'Music paused'


# Function for stopping music
def stop_music():
    mixer.music.stop()
    statusbar['text'] = 'Music Stopped'


# Dialog box for help> About us
def about_us():
    tkinter.messagebox.showinfo('Music Player', 'This player was built on Tkinter python')


# Submenu for file
sub_menu = Menu(menu_bar, tearoff=0)  # setting tearoff 0 to remove dotted part
menu_bar.add_cascade(label='file', menu=sub_menu)
sub_menu.add_command(label='open', command=browse_file)
sub_menu.add_command(label='close', command=root.destroy)
# Submenu for help
sub_menu = Menu(menu_bar, tearoff=0)  # setting tearoff 0 to remove dotted part
menu_bar.add_cascade(label='help', menu=sub_menu)
sub_menu.add_command(label='About us', command=about_us)

mixer.init()  # initializing mixer

# Window size using Geometry
# root.geometry('600x500')

# Changing title
root.title("Music Player")

# Changing icon
root.iconbitmap(r'music.ico')

# Adding widget(text,image) and pack
# label
text = Label(root, text='Welcome to player')
text.pack(pady=14)

# Frame for control
control_frame = Frame(root)
control_frame.pack(padx=14, pady=14)

# play button

play_photo = PhotoImage(file='play.png')
play_button = Button(control_frame, image=play_photo, command=play_music)
# play_button.pack(side=LEFT, padx=10)
play_button.grid(row=0, column=0)

# stop button

stop_photo = PhotoImage(file='stop-button.png')
stop_button = Button(control_frame, image=stop_photo, command=stop_music)
# stop_button.pack(side=LEFT, padx=10)
stop_button.grid(row=0, column=1)
# pause button

pause_photo = PhotoImage(file='pause.png')
pause_button = Button(control_frame, image=pause_photo, command=pause_music)
# pause_button.pack(side=LEFT, padx=10)
pause_button.grid(row=0, column=2)

# Scaling volume control
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_volume_scale)
scale.set(50)  # default value set at 50
mixer.music.set_volume(.5)
scale.pack(pady=10)

# Adding status bar at bottom
statusbar = Label(root, text='Welcome to music player', relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
