import pygame
import datetime
import time
import urllib
import urllib2
import sys
import os

class checker(object):

	def __init__(self):
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
		urlObtained = False
		while urlObtained == False:
			try:
				# Get the image and store it's hash in oldHash.
				request = urllib2.Request(url)
				result = urllib2.urlopen(request)
				urlObtained = True
			except:
				pass
		return result.geturl()

	def getDateTimeString(self):
		dateTime = datetime.datetime.utcnow()
		output = str(dateTime.year) + "-"
		if dateTime.month < 10:
			output += "0"
		output += str(dateTime.month) + "-"
		output += str(dateTime.day) + " "
		# I wish osx would just let me use :s in filepaths
		if dateTime.hour < 10:
			output += "0"
		output += str(dateTime.hour) + "-"
		if dateTime.minute < 10:
			output += "0"
		output += str(dateTime.minute)
		return output
 
	def newImageFound(self, url, sleep = True):
		datetime = self.getDateTimeString()
		urlHash = url.rsplit('/', 1)[1]

		imageExists = False

		for image in os.listdir("images"):
			if image[17:] == urlHash:
				imageExists = True

		if not imageExists:
			filepath = "images/" + datetime + " " + urlHash
			print "[" + datetime + "]"
			print "New image found"
			print urlHash
			print "Image saved at " + filepath + "\n"
			pygame.mixer.Sound(self.SOUNDPATH).play()
			image = urllib.URLopener()
			image.retrieve(url, filepath)
		else:
			print "[" + datetime + "]"
			print "Duplicate image found."
			print urlHash + "\n"