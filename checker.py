import pygame
import datetime
import time
import urllib
import urllib2
import sys
import os

class checker(object):

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
		oldURL = self.getRedirectURL(self.IMAGEURL)
		self.newImageFound(oldURL, False)

		while not datetime.datetime.utcnow().minute == 3 and not datetime.datetime.utcnow().minute == 33:
			time.sleep(60)

		while True:
			# Get the datetime
			dateTime = datetime.datetime.utcnow()
			# Get the current minute.
			currentMinute = dateTime.minute
			# Get the current url that time.png gets redirected to.
			newURL = self.getRedirectURL(self.IMAGEURL)
			# If the newURL isn't the same as the old URL then there has been a change!
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
		output = str(dateTime.year) + "-"
		output += str(dateTime.month) + "-"
		output += str(dateTime.day) + " "
		# I wish osx would just let me use :s in filepaths
		output += str(dateTime.hour) + ","
		output += str(dateTime.minute)
		return output
 
	def newImageFound(self, url, sleep = True):
		datetime = self.getDateTimeString()
		urlHash = url.rsplit('/', 1)[1]
		filepath = "images/" + datetime + " " + urlHash
		print "New image found at " + datetime
		print "Hash of new image is " + urlHash
		print "New image saved at " + filepath
		pygame.mixer.Sound(self.SOUNDPATH).play()
		image = urllib.URLopener()
		image.retrieve(url, filepath)
		if sleep == True:
			time.sleep(self.NEWPIX * self.MINUTE)
