import pytube

youtubeVideoId = " "

youtubeVideo = pytube.YouTube(youtubeVideoId)
audio = youtubeVideo.streams.get_audio_only()
audio.download(filename='audio.mp3')

#correr: python transcript.py