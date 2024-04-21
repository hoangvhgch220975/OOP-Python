

from tkinter import *
from tkinter import messagebox as msg
from tkinter import scrolledtext as tkst


import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", END)
    text_area.insert(1.0, content)

class UpdateVideo:
    def __init__(self, window):
        self.window = self.create_window(window)
        self.create_widgets()

    def create_window(self, window):
        window.title('Update Video')
        window.geometry('400x300')
        return window

    def create_widgets(self):
        self.video_number_lbl = Label(self.window, text='Video Number: ')
        self.video_number_lbl.grid(row=0, column=0,padx=10, pady=10, sticky='W')
        
        self.video_number_txt = Entry(self.window)
        self.video_number_txt.grid(row=0, column=1,columnspan=2, padx=10, pady=10)

        self.new_rating_lbl = Label(self.window, text='New Rating: ')
        self.new_rating_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')

        self.new_rating_txt = Entry(self.window)
        self.new_rating_txt.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        self.submit_btn = Button(self.window, text='Submit', command=self.update_video)
        self.submit_btn.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky='W')

        self.annonce_txt = tkst.ScrolledText(self.window, width=24, height=4, wrap='none')
        self.annonce_txt.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='NESW')
    
    
    
    def update_video(self):
        video_number = self.video_number_txt.get()
        new_rating = self.new_rating_txt.get()
        if video_number in lib.library and new_rating.isnumeric() == True:
            video = lib.library[video_number]
            lib.set_rating(video_number, int(new_rating))
            message = f'Video Name: {video.name}\n Director: {video.director}\n New Rating: {video.rating}\nPlay Count: {video.play_count}'
            msg.showinfo('Success', 'Video updated successfully')
        elif new_rating.isnumeric() == False:
            message = f'Error: Rating must be a number'
            msg.showerror('Error', 'Rating must be a number')
        else:
            message = f'Error: Video {video_number} not found'
            msg.showerror('Error', 'Video not found')
        self.annonce_txt.delete(1.0, END)
        self.annonce_txt.insert(END, message)

if __name__ == "__main__":
    window = Tk()
    fonts.configure()
    UpdateVideo(window)
    window.mainloop()

