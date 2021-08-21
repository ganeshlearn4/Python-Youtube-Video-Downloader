import threading
import tkinter as tk

from pytube import YouTube


class DownloadThread(threading.Thread):
    url = None

    statusLabel = None

    def __init__(self, url, statusLabel):
        threading.Thread.__init__(self)
        self.url = url
        self.statusLabel = statusLabel

    def run(self):
        self.statusLabel["text"] = "Downloading"

        def progressCallback(stream, chunk, bytes_remaining):
            progress = (round((1 - bytes_remaining / video.filesize) * 100, 3), "% done")
            self.statusLabel["text"] = progress

        try:
            youtube = YouTube(self.url)
            youtube.register_on_progress_callback(progressCallback)

            video = youtube.streams.filter(progressive=True, file_extension="mp4").first()

            video.download("C:/")

            self.statusLabel["text"] = "Download Completed"
        except Exception as e:
            self.statusLabel["text"] = "Error while Downloading"


class BuildGUI:
    window = None

    inputField = tk.StringVar

    downloadButton = None
    statusLabel = None

    def __init__(self, window):
        self.window = window
        self.constructInputField()
        self.constructButton()
        self.constructStatusText()

    def constructInputField(self):
        self.inputField = tk.Entry(self.window, textvariable=self.inputField)
        self.inputField.place(x=102, y=117, width=292, height=32)

    def startDownloading(self):
        url = self.inputField.get()

        if url is "":
            self.statusLabel["text"] = "Please enter URL"
        else:
            self.statusLabel["text"] = "Starting Download"

            downloadThread = DownloadThread(url, self.statusLabel)
            downloadThread.start()

    def constructButton(self):
        self.downloadButton = tk.Button(self.window, text="Download", command=self.startDownloading)
        self.downloadButton.place(x=102, y=157, width=292, height=32)

    def constructStatusText(self):
        self.statusLabel = tk.Label(text="Download Video with Youtube Video Link")
        self.statusLabel.config(font=("Calibiri", 14))
        self.statusLabel.place(x=0, y=200, width=500, height=32)


def main():
    window = tk.Tk()
    window.iconbitmap("icon.ico")
    window.geometry('500x300')
    window.resizable(False, False)

    BuildGUI(window)

    window.mainloop()


if __name__ == "__main__":
    main()
