import  os
from os import listdir
from os.path import  join
import filecmp
import shutil



sourcePath = 'D:\\unsorted songs\\sourceSongs'
matchPath = 'D:\\din songs'
destinationPathSp = 'D:\\new songs' # spcial path for getting only the new files added
destinationPath = 'D:\\din songs'
songs = []
for file in listdir(sourcePath): # getting the target sources directory
    songs.append(join(sourcePath , file)) # adding all the target songs into the songs array

for targetSong in songs: # getting each song from the target songs array
    print(targetSong)
    doesNotExist = True
    for matchfile in listdir(matchPath) : # comparing it with all the songs to be matched
        if doesNotExist == True:
            matchSong = join(matchPath,matchfile)
            # print(matchSong)
            status = not filecmp.cmp(targetSong, matchSong) # if songs are similar status = false
            doesNotExist = status and doesNotExist

    if doesNotExist == True: # if the file is not in the main folder it is copied
        destinationFile = join(destinationPath, os.path.basename(targetSong)) # createting the new destination file
        print(destinationFile)
        shutil.copy(targetSong,destinationPath)
        shutil.copy(targetSong,destinationPathSp)

# if status == False:
#     shutil.copyfile(songs[0],destinationPath)
# print(os.path.basename(songs[0]))

#

# print(status)