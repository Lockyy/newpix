newpix

======

Checks once a minute for a new xkcd.com/1190 update. 
Once it finds one it logs the time found and the hash in the image url. It also downloads the image to the images folder.
After it has found, logged and downloaded the latest image it goes to sleep for 25 minutes to prevent wasteful checking.

It won't start properly checking till 3 minutes past the last newpix, to ensure that newpix are correctly logged around 
when they are actually posted.

Ping wav found at: http://soundjax.com

======

Operation:

python newpix.py
