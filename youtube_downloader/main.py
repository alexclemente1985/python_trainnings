from PySide6.QtWidgets import *
from ui.youtube_downloader import Ui_MainWindow

import sys
from pytube import YouTube, Playlist
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import pip_system_certs

# Projeto descontinuado por conta de problemas da lib pytube para downloads de vídeos (403 forbidden)
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Youtube Downloader")

        self.btn_download.clicked.connect(self.yt_download)

    def yt_download(self):
        video_url = self.txt_link.text()
        print("video_url: ", video_url)

        if self.rdb_video.isChecked():
            try:
                YouTube(video_url).streams.filter(res="720p").first().download()
            except Exception as e:
                YouTube(video_url).streams.filter(res="480p").first().download()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()