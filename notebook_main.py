import welcome_message
from tkinter import Tk
from sign_up import first_use
from login import not_first_use
from data_correctness import cursor
import center_window
welcome_message.play()



root = Tk()
root.title('Personal_Notebook')
root.configure(bg='black')
root.title("Notebook.")

try :
    cursor.execute("""SELECT * FROM Users""")
except :
    pass

users = cursor.fetchall()
if users :
    center_window.center_window(root, 350, 300)
    not_first_use(root)
else :
    center_window.center_window(root, 350, 250)
    first_use(root)










