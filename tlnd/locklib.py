from guizero import Window, Text, PushButton, App, Box
import tkinter as tk

def on_closing():
    # Do nothing when Alt+F4 is pressed or the title bar's close button is clicked
    pass

def unlock():
    # This function will be called to close the window
    mainWindow.destroy()  # Close the main window

def lock():
    global mainWindow  # Declare mainWindow as global to access it in unlock
    app = App()
    mainWindow = Window(app, title='Timelok New Daemon', bg='#000000')
    mainWindow.tk.attributes('-fullscreen', True)

    # Set the protocol for the WM_DELETE_WINDOW event
    mainWindow.tk.protocol("WM_DELETE_WINDOW", on_closing)

    centerBox = Box(mainWindow, layout="grid")
    warning = Text(centerBox, text="Ordinateur verrouillé", color="#FFFFFF", grid=[0, 0], align="top")
    subtext = Text(centerBox, text="Allez voir l'acceuil pour le déverouiller", color="#FFFFFF", grid=[0, 1], align="top")

    centerBox.tk.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    app.display()