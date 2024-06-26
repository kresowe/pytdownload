import streamlit as st
from pytube import YouTube
import os
import random

st.write("""
# Simple YouTube Downloader

### based on [pytube](https://pytube.io/en/latest/)""")
link = st.text_input("Link to video")
file_name = st.text_input("File name")
mode = st.radio(
    "Download format:",
    ["video + audio", "audio only"] )

if st.button("Prepare file"):
    yt = YouTube(link)
    tmp_name = f'{random.randrange(16**10):x}'
    if mode == "video + audio":
        tmp_file_name = tmp_name + '.mp4'
        file_name = file_name + '.mp4'
        yt.streams.filter(progressive=True, file_extension='mp4').first().download(
            'downloads', tmp_file_name)
    else:
        tmp_file_name = tmp_name + '.mp3'
        file_name = file_name + '.mp3'
        yt.streams.filter(only_audio=True).order_by('abr').desc().first().download('downloads', tmp_file_name)

    with open(os.path.join('downloads', tmp_file_name), 'rb') as f:
        st.download_button('Download', f, file_name=file_name)
        os.remove(os.path.join('downloads', tmp_file_name))
