newpix

======

Checks once a minute for a new xkcd.com/1190 update. 
Once it finds one it logs the time found and the hash in the image url. It also downloads the image to the images folder.
After it has found, logged and downloaded the latest image it goes to sleep for 25 minutes to prevent wasteful checking.

Ping wav found at: http://soundjax.com

======

Operation:

python newpix.py

Regardless of when you start it, it should stabalise to wake up and start checking approx. 5 mins before a newpix.
