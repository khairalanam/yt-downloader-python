from .Application import Application
from multiprocessing import Pool
from pytube import Playlist, YouTube
from time import time


class YTDownloader(Application):
    def __init__(self, name, dimensions):
        super().__init__(name, dimensions)
        print("YT Initialised!")

    def start_playlist_download(self, playlist_link):
        try:
            start = time()
            playlist_object = Playlist(playlist_link.get())
            self.add_label(playlist_object.title, 40, 40)
            list_of_videos = [video.streams.get_highest_resolution()
                              for video in playlist_object.videos]
            self.add_image([*playlist_object.videos][0].thumbnail_url, 40, 40)
            with Pool() as pool:
                pool.map(YTDownloader.download_video, list_of_videos)
        except:
            self.add_label("Invalid Link!", 40, 40)
        else:
            print(f"{time() - start} s")

    @staticmethod
    def download_video(video):
        video.download()
