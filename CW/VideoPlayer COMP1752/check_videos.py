import tkinter as tk
import tkinter.scrolledtext as tkst


import video_library as lib
import font_manager as fonts

# Set text content of a text area widget 
# Text_area: the text area widget to modify
# Content: the new content to set
def set_text(text_area, content):
    # Clear existing content
    text_area.delete("1.0", tk.END)
    # Insert new content
    text_area.insert(1.0, content)


class CheckVideos():
    def __init__(self, window):
        window.geometry("800x450")
        window.title("Check Videos")

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)


       
    

    
    def check_video_clicked(self):
        # Get the video number from the input text box
        key = self.input_txt.get()
        # Get the video name from the video_library
        name = lib.get_name(key)
        # If the video exists, get the director, rating and play count
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            # Set a vảiable to hold the video details to insert into the video_txt widget
            video_details = f"{name}\n{director}\nRating: {rating}\nPlays: {play_count}"
            # Set content of the video_txt widget by video_details
            set_text(self.video_txt, video_details)
        else:
            # If the video does not exist, set the video_txt widget to display an error message
            set_text(self.video_txt, f"Video {key} not found")
            # Configure label status
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):
        # Get a list of all videos from the video_library by calling the list_all function
        video_list = lib.list_all()
        # Set the content of the list_txt widget by the video_list
        set_text(self.list_txt, video_list)
        # Configure label status
        self.status_lbl.configure(text="List Videos button was clicked!")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
