import pygame
import datetime
import time

pygame.mixer.init()

# Times to play sound at.
updateTimes = [2,32]

while True:
	d = datetime.datetime.now()
	if d.minute in updateTimes:
		pygame.mixer.Sound('sound.wav').play()
		# Ensure the ping only goes off once per update.
		time.sleep(120)