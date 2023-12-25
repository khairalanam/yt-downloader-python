from multiprocessing import Pool
from time import time
from pytube import Playlist, YouTube, Stream
from pytube.exceptions import VideoUnavailable
from .Application import Application
import os
import asyncio
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


class YTDownloader(Application):
    def __init__(self, name, dimensions):
        super().__init__(name, dimensions)
        self.video_count = 0
        self.curr_label = self.add_label("", 20, 0)
        self.curr_label.pack_forget()
        self.curr_label.place(relx=0.5, rely=0.45)
        # self.video_title = self.add_label("", 20, 0)
        self.progress_bar = self.add_progress_bar()
        self.progress_bar.pack_forget()
        self.progress_bar_percentage = self.add_label("", 20, 0)
        self.progress_bar_percentage.pack_forget()
        print("YT Initialised!")

    def on_progress(self, stream: Stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        completion_percentage = (bytes_downloaded / total_size) * 100
        self.progress_bar_percentage.configure(
            text=f"{round(completion_percentage, 1)}%")
        self.curr_label.configure(text=f"Downloading: {stream.title}", font=("Helvetica", 14, "bold"))
        self.progress_bar_percentage.update()
        self.curr_label.update()
        self.progress_bar.set(completion_percentage / 100)

    def download_video(self, video_obj: (YouTube, int)):
        try:
            video_object: YouTube = video_obj[0]
            video_url = video_object.watch_url
            video_yt_obj: YouTube = YouTube(
                video_url, on_progress_callback=self.on_progress)
            size: int = video_obj[1]

            # self.video_title.pack(padx=20, pady=30)
            self.progress_bar.place(relx=0.5, rely=0.6)
            self.progress_bar_percentage.place(relx=0.5, rely=0.55)
            start = time()
            video = video_yt_obj.streams.get_highest_resolution()
            # self.curr_label.configure(text=f"Downloading: {video.title}", font=("Helvetica", 14, "bold"))
            video.download(output_path=os.path.join(
                os.path.expanduser("~"), "Downloads"))
            self.curr_label.configure(text=f"({self.video_count + 1}/{size}) Downloaded {
                                      video.title}: {time() - start}s", font=("Helvetica", 14, "bold"))

            print(
                f"({self.video_count + 1}/{size}) Downloaded {video.title}: {time() - start}s")
            self.video_count += 1
            # self.video_title.forget()
        except Exception as e:
            print(f"Error downloading {video.title}: {e}")

    async def download_playlist(self, playlist_link):
        try:
            self.curr_label.configure(text="")
            self.curr_label.place(relx=0.5, rely=0.45)
            self.progress_bar_percentage.configure(text="0%")
            self.progress_bar.set(0)

            # Playlist object creation
            playlist_object = Playlist(playlist_link.get())
            list_of_videos = [*playlist_object.videos]

            # Set timer
            start = time()

            playlist_name = self.add_label(f"Playlist name: {playlist_object.title}", 10, 10)
            playlist_name.forget()
            playlist_name.place(relx=0.1, rely=0.45)
            playlist_thumbnail = self.show_image_from_url(
                list_of_videos[0].thumbnail_url)
            playlist_image = self.add_image(playlist_thumbnail, 20, 20, (320, 180))
            playlist_image.forget()
            playlist_image.place(relx=0.1, rely=0.55)

            # Download process using multiprocessing
            loop = asyncio.get_event_loop()
            with ThreadPoolExecutor(max_workers=os.cpu_count()) as pool:
                await asyncio.gather(*[loop.run_in_executor(pool, self.download_video, (video, playlist_object.length)) for video in list_of_videos])

                print(f"Time taken: {time() - start} s")
                self.curr_label.place_forget()
                self.curr_label.configure(
                    text="Finished Downloading!!! Check Your Downloads Folder", font=("Helvetica", 20, "bold"))
                self.curr_label.pack(padx=20, pady=20)
                self.video_count = 0
                self.progress_bar_percentage.place_forget()
                self.progress_bar.place_forget()
                playlist_image.place_forget()
                playlist_name.place_forget()

        except VideoUnavailable:
            self.add_label("Invalid Link!", 40, 40)

    def start_playlist_download_thread(self, playlist_link):
        loop = asyncio.get_event_loop()
        download_thread = Thread(target=loop.run_until_complete, args=(
            self.download_playlist(playlist_link),))
        download_thread.start()
