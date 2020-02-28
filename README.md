# Frame-Division-Data-Collection
Download videos from youtube/ Upload videos onto the server and have it output frames of Images with a random interval between capturing frames


General guide :
To Kill Ports  :
lsof -P | grep ':4000' | awk '{print $2}' | xargs kill -9

Reactjs :
1. Figure this out or copy paste previous projects

NodeServe :
1. Copy the Server.js
2. Copy the pacakage-lock.json
3. npm install <necessary packages>

Django :
1. django-admin startproject mysite
2. cd mysite
3. python3 manage.py startapp polls
4. python3 manage.py runserver

templates :
1. cd polls
2. mkdir templates
3. touch index.html
extras:
1. Add static paths in settings.py
2. Add the installed apps in settings.py
3. Add the cross origin request
4. corsheaders in installed apps
http://www.srikanthtechnologies.com/blog/python/enable_cors_for_django.aspx

Requirements :
1. Divide a video into frames using OpenCV in python
2. Make the application dynamic, enable frontend interactions 


########--------------------------------------------------------------------------------------------------
to accomplish requirement: 1
1. Divide a video into frames using OpenCV in python
