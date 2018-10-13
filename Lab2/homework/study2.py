from youtube_dl import YoutubeDL

option = {
    'format':'bestaudio/audio'
}
dl = YoutubeDL(option)
dl.download(['https://www.youtube.com/watch?v=8mn-FFjIbo8'])