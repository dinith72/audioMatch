import  os
from os import listdir
from os.path import  join
import filecmp
# import aud


# mp3Song =
sourcePath = 'D:\\unsorted songs\\sourceSongs'
matchPath = 'D:\\din songs'
songs = []
for file in listdir(sourcePath): # getting the target sources directory
    songs.append(join(sourcePath , file)) # adding all the target songs into the songs array

for targetSong in songs: # getting each song from the target songs array
    print(targetSong)
    statusFinal = False
    for matchfile in listdir(matchPath): # comparing it with all the songs to be matched
        matchSong = join(matchPath,matchfile)
        # print(matchSong)
        status = filecmp.cmp(targetSong, matchSong)
        statusFinal = status & statusFinal
# song1 = open(songs[2], 'rb').read()
# song2 = open(songs[3], 'rb').read()
# print(filecmp.cmp(songs[0] , songs[1]))

#

# print(status)