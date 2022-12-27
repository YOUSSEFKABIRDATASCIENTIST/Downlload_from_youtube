

from pytube import YouTube
from pytube import Playlist
#here we give the path where the playlist video will be saved
path="Y:\CoursesUniversity\BBB"
# here we give the path of the playlist
playlist = Playlist('https://www.youtube.com/watch?v=Te67sBlJJMg&list=PLD4dEalVnw4U2YVu2P79dQ_i_eTQ4N-O8')
print('the Urls of  videos in playlist: %s' % len(playlist.video_urls))

for video in playlist.video_urls:
    youtubeObject = YouTube(video)
    youtubeObject=youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(path)
    except:
        print("Error found")
 
print("Download is completed successfully")
    


