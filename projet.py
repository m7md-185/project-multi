import  tkinter as TK
from tkinter import messagebox
import vlc
import yt_dlp
import os
import sys

sys.stdout = open(os.devnull, "w")
sys.stderr = open(os.devnull, "w")
os.environ["PYTHON_VLC_VERBOSE"] = "0"

def play_media(format_type):
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Warning", "Please enter a video URL!")
        return

    try:
        # yt-dlp options
        ydl_opts = {"quiet": True, "format": format_type}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            stream_url = info["url"]
            play_stream(stream_url)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def play_stream(stream_url):
    try:
        # Create VLC instance
        instance = vlc.Instance("--quiet", "--no-video-title-show")
        player = instance.media_player_new()
        media = instance.media_new(stream_url)
        player.set_media(media)

        # Set audio volume to 100%
        player.audio_set_volume(100)

        # Play the video
        player.play()

        # Confirmation message removed
        # messagebox.showinfo("Playing", "Media is now playing with sound.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while trying to play: {e}")

# Setup the GUI
root = TK.Tk()
root.title("Media Player")

TK.Label(root, text="Enter the video URL:").pack(pady=5)
url_entry = TK.Entry(root, width=50)
url_entry.pack(pady=5)

TK.Button(root, text="Play High Resolution", command=lambda: play_media("best")).pack(pady=5)
TK.Button(root, text="Play Low Resolution", command=lambda: play_media("worst")).pack(pady=5)
TK.Button(root, text="Play Audio Only", command=lambda: play_media("bestaudio")).pack(pady=5)

root.mainloop()