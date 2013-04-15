import datetime
import time
import urllib
import urllib2
import sys
import os
try:
	import pygame
except:
	pass

class checker(object):

	def __init__(self):
		self.MINUTE = 60
		# URL to grab image from.
		self.IMAGEURL = "http://imgs.xkcd.com/comics/time.png"
		# File path of sound file.
		self.SOUNDPATH = "sound.wav"
		# Check if pygame imported correct, if it did then we can play the ping.
		if "pygame" in sys.modules:
			self.pygame = True
		self.saveIntoRepo = True
		
	def main(self):
		if self.pygame:
			pygame.mixer.init()

		# Ensure that we log the first image.
		oldURL = self.getRedirectURL(self.IMAGEURL)
		self.newImageFound(oldURL, False)

		lastMinute = datetime.datetime.utcnow().minute

		while datetime.datetime.utcnow().minute == lastMinute:
			time.sleep(1)

		while True:
			# Get the current minute.
			currentMinute = datetime.datetime.utcnow().minute
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
		if dateTime.day < 10:
			output += "0"
		output += str(dateTime.day) + " "
		# I wish osx would just let me use :s in filepaths
		if dateTime.hour < 10:
			output += "0"
		output += str(dateTime.hour) + "-"
		if dateTime.minute < 10:
			output += "0"
		output += str(dateTime.minute)
		return output

	def getGitFilePath(self):
		images = os.listdir("xkcdTimeImages")
		latestImage = 0
		for image in images:
			if not image[0] == "T":
				continue
			imageList = image.split(".", 1)
			imageList = imageList[0].split("Time", 1)
			imageNumber = int(imageList[1])
			if imageNumber > latestImage:
				latestImage = imageNumber
		latestImage += 1
		output = "xkcdTimeImages/Time" + str(latestImage) + ".png"
		return output
 
	def newImageFound(self, url, sleep = True):
		datetime = self.getDateTimeString()
		urlHash = url.rsplit('/', 1)[1]

		imageExists = False
		if not os.listdir("images") == []:
			for image in os.listdir("images"):
				if image[17:] == urlHash:
					imageExists = True

		if not imageExists:
			filepath = "images/" + datetime + " " + urlHash
			print "[" + datetime + "]"
			print "New image found"
			print urlHash
			print "Image saved at " + filepath
			if self.pygame:
				pygame.mixer.Sound(self.SOUNDPATH).play()
			grabber = urllib.URLopener()
			grabber.retrieve(url, filepath)
			if self.saveIntoRepo:
				gitFilePath = self.getGitFilePath()
				print "Image saved at " + gitFilePath
				grabber.retrieve(url, gitFilePath)
			print "\n"
		else:
			print "[" + datetime + "]"
			print "Duplicate image found."
			print urlHash + "\n"