from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        #stream.download(save_path)
        highest_res = stream.get_highest_resolution()
        highest_res.download(output_path=save_path)
        print("Download Successfully.")

    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")

    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter the video URL: ")
    save_path = open_file_dialog()

    if save_path:
        print("Download started...")
        download_video(video_url, save_path) 
    else:
        print("Invalid folder...")