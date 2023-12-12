from classes.YTDownloader import YTDownloader
from tkinter import StringVar

# App creation
app: YTDownloader = YTDownloader("YT Downloader", "1024x640")

# Title
app.add_label("Insert the playlist link to download", 20, 40)

# Input for playlist link
playlist_link: StringVar = app.add_entry(400, 40)

# Download button
app.add_button("Download", 200, 40,
               YTDownloader.start_playlist_download, playlist_link)

# Run the app
app.run_app()
