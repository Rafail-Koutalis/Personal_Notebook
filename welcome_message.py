from tkinter import PhotoImage,Label,Tk
import os
import sys
import center_window

root_2 = Tk()
root_2.configure(bg='black')
root_2.title("Personal Notebook")
center_window.center_window(root_2,520,650)

def play() :
    def destroy_root(event):
        root_2.destroy()

    root_2.bind("<Button>", destroy_root)

    def resource_path(relative):
        return os.path.join(os.environ.get("_MEIPASS2", os.path.abspath(".")), relative)

    def resource_path2(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)




    path = resource_path2("chad_1.png")
    img = PhotoImage(file=path)
    label = Label(root_2, image=img,bg='black')



    label_1 = Label(root_2, text='Oh, i see you studied.\nKeep it up champ.\n',
                        font=('helvetica', 16, 'bold'), bg='black', fg='white')
    label_3 = Label(root_2, text='\n Press anywhere on the frame to proceed.', font=('helvetica', 14, 'bold'),
                        bg='black', fg='white')


    label_1.grid(row=0, column=0)
    label.grid(row=1)
    label_3.grid(row=2, column=0)
    root_2.rowconfigure(0,weight=1)
    root_2.rowconfigure(1,weight=1)
    root_2.rowconfigure(2,weight=1)

    root_2.mainloop()

