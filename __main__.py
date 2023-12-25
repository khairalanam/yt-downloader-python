from classes.YTDownloader import YTDownloader
from tkinter import StringVar

# App creation
app: YTDownloader = YTDownloader("YT Downloader", "1024x640", "./assets/main-logo.ico")

# Title
playlist_label = app.add_label("Insert the playlist link to download", 20, 30)

# Input for playlist link
playlist_link: StringVar = app.add_entry(400, 40)

# Download button
app.add_button("Download", 200, 40,
               app.start_playlist_download_thread, playlist_link)

# Run the app
app.run_app()
