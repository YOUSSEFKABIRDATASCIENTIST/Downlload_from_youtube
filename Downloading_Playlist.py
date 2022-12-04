
# =============================================================================
# from pytube import Playlist
# path="Y:\CoursesUniversity\Big_Data"
# playlist = Playlist('https://www.youtube.com/watch?v=zez2Tv-bcXY&list=PL9ooVrP1hQOFrYxqxb0NJCdCABPZNo0pD')
# print('Number of videos in playlist: %s' % len(playlist.video_urls))
# 
# # Loop through all videos in the playlist and download them
# for video in playlist.videos:
#     print('le nom de videoest:',video)
#     video.streams.first().download(path)
# =============================================================================
    
########################################"
##########################################
from pytube import YouTube
from pytube import Playlist

path="Y:\CoursesUniversity\BBB"
playlist = Playlist('https://www.youtube.com/watch?v=Te67sBlJJMg&list=PLD4dEalVnw4U2YVu2P79dQ_i_eTQ4N-O8')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

for video in playlist.video_urls:
    print('le nom de videoest:',video)
    youtubeObject = YouTube(video)
    youtubeObject=youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(path)
    except:
        print("Error found")
    print("Download is completed successfully")
    


