
from tkinter import *
from tkinter import scrolledtext as tkst
from tkinter import messagebox as msg


import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", END)
    text_area.insert(1.0, content)

class CreateVideoList():
    def __init__(self,window):
        self.window = self.create_window(window)
        self.create_widgets()
        self.keys = []

    def create_window(self,window):
        window.title('Create Video List')
        window.geometry('1200x600')
        return window
    
    def create_widgets(self):
        self.list_videos_btn = Button(self.window, text='List All Videos',command=self.list_videos_clicked)
        self.list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        self.listvideo = tkst.ScrolledText(self.window, width=48, height=12, wrap='none')
        self.listvideo.grid(row=1, column=0, columnspan=2, rowspan=2, sticky='W', padx=10, pady=10)

        self.playlist = tkst.ScrolledText(self.window, width=48, height=12, wrap='none')
        self.playlist.grid(row=1, column=3, columnspan=2, rowspan=2, sticky='NW', padx=10, pady=10)

        self.detail_btn = Button(self.window, text='See Detail', command=self.detail_clicked)
        self.detail_btn.grid(row=4, column=0, padx=10, pady=10)

        self.detail_txt = Text(self.window, width=24, height=4, wrap='none')
        self.detail_txt.grid(row=5, column=0, padx=10, pady=10)

        self.enter_lbl = Label(self.window, text='Enter Video Number: ')
        self.enter_lbl.grid(row=3, column=3, padx=10, pady=10)

        self.input_number = Entry(self.window, width=3)
        self.input_number.grid(row=3, column=4, padx=10, pady=10)

        self.add_video_btn = Button(self.window, text='Add Video to Playlist' ,command=self.add_video_clicked)
        self.add_video_btn.grid(row=4, column=2, padx=10, pady=10)

        self.play_btn = Button(self.window, text='Play',command=self.play_playlist)
        self.play_btn.grid(row=4, column=3,  padx=10, pady=10)

        self.reset_btn = Button(self.window, text='Reset PlayList',command=self.reset_list_clicked)
        self.reset_btn.grid(row=4, column=4, padx=10, pady=10)

        self.status_lbl = Label(self.window, text='', font=('Helvetica', 10))
        self.status_lbl.grid(row=9, column=2, columnspan=4, sticky='W', padx=10, pady=10)


        

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.listvideo, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

    def add_video_clicked(self):
        key = self.input_number.get() #get the key from the input field
        if key in lib.library:   # check if the key is in the library
            film = lib.library[key] # get a film by key
            self.keys.append(key)   # add key to the list of keys
            self.playlist.insert(END, film.info() + "\n")    # insert film to playlist widget
            # show status
            self.status_lbl.configure(text=f'Video:  {lib.library[key].info()} added to playlist.')
        else:
            self.playlist.delete(1.0, END)
            msg.showerror('Error', f'Video {key} not found')
        
        


    def reset_list_clicked(self):
        for key in lib.library: # iterate through the library
            lib.library[key].play_count = 0 # reset play count for each film
        self.playlist.delete(1.0, END) # clear the playlist widget
        self.detail_txt.delete(1.0, END) # clear the detail widget
        self.status_lbl.configure(text='Playlist reset successfully') # show status

    def play_playlist(self):
        # key = self.input_number.get()
        # if key in lib.library:
        #     lib.increment_play_count(key)       
        #     self.status_lbl.configure(text='Playlist played successfully')
        # else:
        #     msg.showerror('Error', f'Video {key} not found')
        for key in self.keys:
            lib.increment_play_count(key)
        self.status_lbl.configure(text='Playlist played successfully')   

    def detail_clicked(self):
        key = self.input_number.get()
        if key in lib.library:
            film = lib.library[key]
            details = f"{film.name}\n{film.director}\nRating: {film.rating}\nPlays: {film.play_count}"
            self.detail_txt.delete(1.0, END)
            self.detail_txt.insert(END, details)
        else:
            msg.showerror('Error', f'Video {key} not found')
    
if __name__ == "__main__":
    window = Tk()
    fonts.configure()
    CreateVideoList(window)
    window.mainloop()
            
