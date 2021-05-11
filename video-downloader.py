from tkinter import *
from pytube import YouTube
from tkinter import messagebox


window=Tk()
window.title("YouTube Video Downloader")
window.geometry("400x300")

photo = PhotoImage(file = "youtube.png")
window.iconphoto(False, photo)



#function to download video
def download():
    
    
    try:
        
        YouTube(link).streams.first().download()
        print("Video downloaded succesfully")
    except:
        messagebox.showinfo("URL Error", "Please check your url")
        

# making labels 

text=Label(window, text="Enter YouTube Video URL:").pack(pady=10)
url_entry=Entry(window,width=40,bg="black",fg="white").pack(pady=10)
download_button=Button(window,text="download video", command=lambda: download()).pack(pady=10)

link=url_entry.get()




window.mainloop()
