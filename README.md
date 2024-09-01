# pytdownload

## Simple YouTube Downloader

Just provide a YouTube link and how you would like to name the file and you can download a video or audio from YouTube.

It is based on [pytubefix](https://github.com/JuanBindez/pytubefix)

This app is available at:

https://pytdownload-mb.streamlit.app/

### Running locally

Within venv: 

```bash
streamlit run pytdownload.py
```

### Docker

Supposing you have [Docker Desktop](https://docs.docker.com/desktop/) installed.

You can download and use a Docker image of this app using the commands:

```bash
docker pull kresowe/pytdownload:0.1
docker run -p 8501:8501 -t -i pytdownload:0.1
```