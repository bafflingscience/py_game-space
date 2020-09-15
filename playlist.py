import pygame
import time
import os
import pytest
pygame.mixer.init()

class Playlist:
    def __index__(self):
        self.pl = []
        self.songs = [
        "sounds/pl/Before The Night.mp3",
        "sounds/pl/Dusk.mp3",
        "sounds/pl/Endless Lines.mp3",
        "sounds/pl/Illusory.mp3"
        ]

        for song in self.songs:
            self.pl.append(song)
            pygame.mixer.music.load(self.pl[0][0])
            pygame.mixer.music.play([1][1])
            pygame.music.music.queue()
            pygame.congatants
            pygame.mixer.music.set_endevent(pygame.ENDOFTRACK)
            pygame.mixer.music.get_endevent()