import os
import pygame
from pyfiglet import Figlet
from printy import printy

#check if there is a directory in PlaylistPath.txt
playlistpath = open("PlaylistPath.txt", "r")
if(playlistpath.read() == ''):
    playlistpath.close()
    printy("No playlist path found", "y")
    inputpath = input("Enter path to playlist >>>>")
    playlistpath = open("PlaylistPath.txt", "w")
    playlistpath.write(inputpath)
    playlistpath.close()
else:
    printy("Found playlist, loading...","y")
    playlistpath.seek(0)
    inputpath = playlistpath.read()
    playlistpath.close()

# Load playlist from file
os.chdir(inputpath)
print(os.getcwd())
playlists = os.listdir()

#main title
custom_fig = Figlet(font='slant')
printy(custom_fig.renderText('TerMP3'), 'rB')

#print playlist
printy('yourplaylist: ' + str(playlists), 'gB')
printy('write help for help', 'gB')
playlistid = 0

#inizializing pygame mixer and loading music
pygame.mixer.init()
pygame.mixer.music.load(playlists[playlistid])
paused = False

#command handling
while True:    
    instruction = input(">>>>")
    if instruction == "quit":
        printy('exiting the program', 'b>')
        break
    elif instruction == "play":
        if paused:
            pygame.mixer.music.unpause()
            paused = False
        else:
            pygame.mixer.music.play()
            printy('playing', 'n>')
    elif instruction == "pause":
        paused = True
        pygame.mixer.music.pause()
        printy('music paused', 'r>')
    elif instruction == "stop":
        pygame.mixer.music.stop()
        printy('music stopped', 'm>')
    elif instruction == "next":
        playlistid += 1
        if playlistid >= len(playlists):
            playlistid = 0
        pygame.mixer.music.load(playlists[playlistid])
        pygame.mixer.music.play()
        printy('playing ' + playlists[playlistid], 'y>')
    elif instruction == "prev":
        playlistid -= 1
        if playlistid < 0:
            playlistid = len(playlists) - 1
        pygame.mixer.music.load(playlists[playlistid])
        pygame.mixer.music.play()
        printy('playing ' + playlists[playlistid], 'y>')
    elif instruction == "help":
        printy('play - plays the music', 'gB')
        printy('pause - pauses the music', 'gB')
        printy('stop - stops the music', 'gB')
        printy('next - plays the next song', 'gB')
        printy('prev - plays the previous song', 'gB')
        printy('quit - quits the program', 'gB')