from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
import os
import moviepy.editor as mp
import requests as req
from bs4 import BeautifulSoup as bs
import re

# Folder to save the MP3
# Folder to save the MP3
sep = os.sep
save_path = os.path.expanduser("~" + sep + "Music" + sep + "Youtube Downloads" )

# Create the main window
root = tk.Tk()
root.title("YouTube Audio Downloader")
# -------- Functions
def convert_to_mp3(input_file, output_file):
    clip = mp.AudioFileClip(input_file)
    clip.write_audiofile(output_file)
    clip.close()

def download_audio():
    url = url_entry.get()  # Get URL from the entry widget
    if not url.strip():
        return
    try:
        video = YouTube(url)
        audio_stream = video.streams.get_audio_only()
        audio_stream.download(output_path=save_path)
        # audio_stream.download(output_path=save_path, filename=video.title + ".mp3")
        root.destroy()  # Close the GUI after successful download
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download: {str(e)}")
    audio_filename = audio_stream.default_filename
    # Getting cleaned title
    response = req.get(url)
    soup = bs(response.text,"html.parser")
    title_elem = soup.find('title')
    if title_elem:
        full_title = title_elem.text
    else:
        full_title = "Title not found"
    cleaned_title = re.sub(r'\s*-\sYoutube','',full_title,flags=re.IGNORECASE)
    output_filename = cleaned_title + ".mp3"
    # print(cleaned_title)
    convert_to_mp3(os.path.join(save_path,audio_filename),os.path.join(save_path,output_filename))
    os.remove(os.path.join(save_path, audio_filename))

# Automatically use the native theme if available (for newer Tkinter versions)
try:
    from tkinter import ttk
    ttk_style = ttk.Style()
    ttk_style.theme_use(ttk_style.theme_use())
except ImportError:
    pass  # Fallback to default theme if ttk is not available

# Calculate position for the window to be centered on the screen
window_width = 500
window_height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Frame for Entry and Button widgets
frame = tk.Frame(root)
frame.pack(pady=20)

# URL entry widget
url_entry = tk.Entry(frame, width=40)
url_entry.grid(row=0, column=0, padx=(0, 10))
url_entry.focus_set()  # Set focus to the URL entry widget

# Download button
download_button = tk.Button(frame, text="Download", command=download_audio)
download_button.grid(row=0, column=1)
# Bind the Enter key to the download_audio function
root.bind('<Return>', lambda event: download_audio())

root.mainloop()


