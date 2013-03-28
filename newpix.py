import pygame
import datetime
import time

pygame.mixer.init()

# Times to play sound at.
updateTimes = [2,32]
interval = 30

# Get current minute
lastMinute = datetime.datetime.now().minute

# Loop till the minute advances.
while datetime.datetime.now().minute == lastMinute:
	pass

while True:
	# Get the datetime
	d = datetime.datetime.now()
	# When we hit an update time start the sound loop.
	if d.minute in updateTimes:
		# The sound loop plays the sound, then sleeps.
		# This causes the sound to play every 'interval' minutes
		while True:
			pygame.mixer.Sound('sound.wav').play()
			time.sleep(interval * 60)
	# Only check once a minute for whether we're at an update time.
	time.sleep(60)
