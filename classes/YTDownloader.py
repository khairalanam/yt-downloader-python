from .Application import Application


class YTDownloader(Application):
    def __init__(self, name, dimensions):
        super().__init__(name, dimensions)
        print("YT Initialised!")

    @staticmethod
    def start_download(link):
        print("Started Downloading!")
