from tkinter import *
from tkinter import messagebox as msg

#### CREATE WINDOW #####
class GUIWindow():
    def __init__(self):
        self.window = Tk()
        self.window.title("Hello GUI App")
        self.window.geometry("300x200")
    ### CREATE WIDGET #####
        self.lbl_massage = Label(self.window, text= 'Hello World')
        self.lbl_massage.grid(row =0, column =0)

        self.lbl_pythons = Label(self.window, text = 'Hello Python')
        self.lbl_pythons.grid(row =1, column=1)

        self.btn_OK = Button(self.window, text = 'OK', command = self.btn_OK_Clicked)
        self.btn_OK.grid(row =2, column=2)

    def btn_OK_Clicked(self):
        msg.showinfo('Info','OK button clicked')

    def run(self):
        self.window.mainloop()

program = GUIWindow()
program.run()