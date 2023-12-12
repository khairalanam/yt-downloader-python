from .Application import Application
from multiprocessing import Pool
from pytube import Playlist, YouTube
from time import time


class YTDownloader(Application):
    def __init__(self, name, dimensions):
        super().__init__(name, dimensions)
        print("YT Initialised!")

    @staticmethod
    def start_playlist_download(playlist_link):
        try:
            start = time()
            playlist_object = Playlist(playlist_link.get())
            list_of_videos = [video.streams.get_highest_resolution()
                              for video in playlist_object.videos]
            with Pool() as pool:
                pool.map(YTDownloader.download_video, list_of_videos)
        except:
            YTDownloader.show_error(
                "Invalid Link", "The Youtube link provided is invalid!")
        else:
            print(f"{time() - start} s")

    @staticmethod
    def download_video(video):
        video.download()
