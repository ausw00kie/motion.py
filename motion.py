from gpiozero import MotionSensor
from pygame import mixer
import pygame

# Need global pygame init
mixer.init()
pygame.init()

# Set up Motion sensor
pir = MotionSensor(4)
file = "crow.mp3"

# Load the music
mixer.music.load(file)


while True:
    if pir.motion_detected:
		pygame.mixer.music.play()
		playing = 1
		while (playing == 1): #stay stuck in this loop until the song finishes
			playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing
