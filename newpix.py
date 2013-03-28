import pygame
import datetime
import time
import urllib
import urllib2
import sys

class newpix(object):

	def __init__(self):
		self.NEWPIX = 20
		self.MINUTE = 60
		# URL to grab image from.
		self.IMAGEURL = "http://imgs.xkcd.com/comics/time.png"
		# File path of sound file.
		self.SOUNDPATH = "sound.wav"
		
	def main(self):
		pygame.mixer.init()

		# Ensure that we log the first image.
		oldURL = None
		# Get current minute
		lastMinute = datetime.datetime.now().minute

		# Loop till the minute advances so that the rest of the script all executes around the minute mark.
		#while datetime.datetime.now().minute == lastMinute:
			#pass

		while True:
			# Get the datetime
			dateTime = datetime.datetime.utcnow()
			# Get the current minute.
			currentMinute = dateTime.minute
			# Get the current url that time.png gets redirected to.
			newURL = self.getRedirectURL(self.IMAGEURL)
			# If the newURL isn't the same as the old URL then there has been a change!
			# Handle this.
			if not newURL == oldURL:
				oldURL = newURL
				self.newImageFound(newURL)
			else:
				time.sleep(self.MINUTE)

	def getRedirectURL(self, url):
		# Get the image and store it's hash in oldHash.
		request = urllib2.Request(url)
		result = urllib2.urlopen(request)
		return result.geturl()

	def getDateTimeString(self):
		dateTime = datetime.datetime.utcnow()
		return dateTime.isoformat(" ")
 
	def newImageFound(self, url):
		datetime = self.getDateTimeString()
		print "New image found at " + datetime
		print "Hash of new image is " + url.rsplit('/', 1)[1]
		pygame.mixer.Sound(self.SOUNDPATH).play()
		image = urllib.URLopener()
		image.retrieve(url, "images/" + datetime + ".png")
		time.sleep(self.NEWPIX * self.MINUTE)