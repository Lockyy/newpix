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
	# Only check once per minute. Also ensures that sound only places once a minute.
	time.sleep(60)