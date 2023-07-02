import os
from pytube import YouTube, Playlist


FULL_PATH = os.path.abspath(".")
PLAYLIST_URL = input("Enter the playlist link: ")
playlist = Playlist(PLAYLIST_URL)

path = os.path.join(FULL_PATH, playlist.title)

if not os.path.isdir(path):
    os.mkdir(path)

for url in playlist:
    try:
        video = YouTube(url)
        print(f"Downloading {video.title}")

        video_path = os.path.join(path, f"{video.title}.mp4")
        if os.path.isfile(video_path):
            print("Video already exists. Skipping...")
            continue

        # The method below download audio only but, if you want the format video, use get_highest_resolution()
        stream = video.streams.get_audio_only()
        stream.download(output_path=path)
        print("Download completed")

    except Exception as e:
        print(f"an error occurred while downloading the video: {e}")
