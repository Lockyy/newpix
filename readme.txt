newpix

======

Checks once a minute for a new xkcd.com/1190 update. 
Once it finds one it logs the time found and the hash in the image url. It also downloads the image to the images folder.

Due to the realisation that time between newpix can change the program will now check every single minute, on the minute to ensure that no newpix are missed in case the time between newpix changed again.

Ping wav found at: http://soundjax.com

======

Without pygame the program will not alert you when a new image is posted, it will just function as a way to grab and store the images/hashes as they appear.