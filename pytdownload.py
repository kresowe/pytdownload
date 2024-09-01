import streamlit as st
from pytubefix import YouTube
import os
import re
import random


def valid_yt_url(inp: str) -> bool:
    yt_url_regex = r"^(https?:\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu\.be))\/([\w\-]+)(\S+)$"
    return re.fullmatch(yt_url_regex, inp) is not None


st.write("""
# Simple YouTube Downloader

### based on [pytubefix](https://github.com/JuanBindez/pytubefix)""")
link = st.text_input("Link to video")
file_name = st.text_input("File name")
mode = st.radio(
    "Download format:",
    ["video + audio", "audio only"] )

try:
    if st.button("Prepare file"):
        if not valid_yt_url(link):
            raise ValueError
        yt = YouTube(link)
        tmp_name = f'{random.randrange(16**10):x}'
        if mode == "video + audio":
            tmp_file_name = tmp_name + '.mp4'
            file_name = file_name + '.mp4'
            ys = yt.streams.get_highest_resolution()
            ys.download(output_path='downloads', filename=tmp_file_name)
        else:
            tmp_file_name = tmp_name + '.mp3'
            file_name = file_name + '.mp3'
            ys = yt.streams.get_audio_only()
            ys.download(output_path='downloads', filename=tmp_file_name)

        with open(os.path.join('downloads', tmp_file_name), 'rb') as f:
            st.download_button('Download', f, file_name=file_name)
            os.remove(os.path.join('downloads', tmp_file_name))
except ValueError:
    st.error("Please provide a valid YouTube link.")
except Exception as e:
    st.error(f"Sorry, this video cannot be downloaded.")
    # st.error(f"Sorry, this video cannot be downloaded. Error: {e}")
