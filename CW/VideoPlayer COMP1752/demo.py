# Import necessary libraries
import tkinter as tk  # Import the tkinter library for GUI
from tkinter import messagebox  # Import messagebox for displaying messages
import font_manager as fonts  # Import font_manager module
from video_library import LibraryItem  # Import LibraryItem class from video_library module
import video_library as lib  # Import video_library module for video library functions

# Function to set text in a text area
def set_text(text_area, content):
    """
    Function to set text in a text area widget.

    Parameters:
        text_area (tk.Text): The text area widget to set text in.
        content (str): The content to set in the text area.
    """
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class CreateVideoListGUI:
    def __init__(self, window):
        """
        Initialize the CreateVideoListGUI class.

        Parameters:
            window (tk.Tk): The Tkinter window.
        """
        self.window = window
        self.window.title("Create Video List")

        fonts.configure()  # Configure fonts

        # Create "List All Videos" button and assign command when clicked
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_all_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        # Create label "Enter Video Number"
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Create entry for "Video Number"
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Create "Add Video" button and assign command when clicked
        add_video_btn = tk.Button(window, text="Add Video", command=self.add_video_clicked)
        add_video_btn.grid(row=0, column=3, padx=10, pady=10)

        # Create "Play Playlist" button and assign command when clicked
        play_video_btn = tk.Button(window, text="Play Playlist", command=self.play_playlist_clicked)
        play_video_btn.grid(row=0, column=4, padx=10, pady=10)

        # Create "Reset Video" button and assign command when clicked
        reset_video_btn = tk.Button(window, text="Reset Video", command=self.reset_video_clicked)
        reset_video_btn.grid(row=5, column=3, padx=10, pady=10)

        # Create text area to display video list
        self.list_txt = tk.Text(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Create text area to display selected video details
        self.video_txt = tk.Text(window, width=48, height=12, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Create label "Status" to display status
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_all_videos_clicked()

    def list_all_videos_clicked(self):
        """
        Action to perform when "List All Videos" button is clicked.
        """
        all_videos = lib.list_all()
        set_text(self.list_txt, all_videos)
        self.status_lbl.configure(text="List All Videos button was clicked!")

    # def play_playlist_clicked(self):
    #     """
    #     Action to perform when "Play Playlist" button is clicked.
    #     Currently, this function does nothing.
    #     """
    #     pass

    def add_video_clicked(self):
        """
        Action to perform when "Add Video" button is clicked.
        """
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplaycount: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

    def reset_video_clicked(self):
        """
        Action to perform when "Reset Video" button is clicked.
        It prompts for confirmation before resetting.
        """
        confirmation = messagebox.askyesno("Reset Confirmation", "Are you sure you want to reset?")
        if confirmation:
            self.input_txt.delete(0, tk.END)
            set_text(self.list_txt, "")
            set_text(self.video_txt, "")
            self.status_lbl.configure(text="Video reset successfully.")

    def play_playlist_clicked(self):
        """
        Action to perform when "Play Playlist" button is clicked.
        """
        play_count = ()
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplaycount: {play_count}"
            lib.increment_play_count(key)
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

def main():
    window = tk.Tk()
    app = CreateVideoListGUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()
