from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.template import Context, loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.template import Context, loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
import json
# to read images from urls
import os
import time
import matplotlib.pyplot as plt
import ast
# to read images from urls
import PIL
from PIL import Image
import numpy as np
import cv2
import random


@csrf_exempt
def index(request):
    decodeddata = request.body.decode('utf-8')
    dictdata = ast.literal_eval(decodeddata)
    username = dictdata["username"]

    # Video input
    vid_name = dictdata["videoname"]
    vid_url = dictdata["videourl"]
    #provide the image type
    img_type = dictdata["imagetype"]
    #provide the random range in secs
    low = int(dictdata["low"])
    high = int(dictdata["high"])

    print("username : " + username)
    print("vid_url : "+vid_url)
    print("vid_name :"+vid_name)
    print("img_type : "+img_type)
    print("low : "+str(low))
    print("high : "+str(high))

    # for storing all the image names
    image_names = []

    # reading video file
    cap = cv2.VideoCapture(vid_url)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # getting the frame length of the video
    position = 1
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print( length )
    frame_count = 1

    # Video Capture using OpenCV VideoCapture
    start_time = time.time()

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open video")

    # starting process
    while frame_count < length - 1:
        # selecting a random number of skip frames within the range (low,high)
        # per second 30 frames
        skip = random.randint(low*30,high*30)
        current_count = 1
        print("skip : "+str(skip))

        while current_count != skip:
            ret, frame = cap.read()
            frame_count = frame_count + 1
            current_count = current_count + 1

        print("current_count : "+str(current_count))
        ret, frame = cap.read()
        frame_count = frame_count + 1
        if frame is not None:
            image_names.append("output_"+str(vid_name)+"_"+str(position)+"."+img_type)
            cv2.imwrite("assets/output_"+str(vid_name)+"_"+str(position)+"."+img_type, frame)
            position = position + 1

        print("frame_count : "+str(frame_count))

    print("Images derived :")
    print(image_names)
    elapsed_time = time.time() - start_time
    print("Performace measure : "+str(elapsed_time))

    '''
    for images in image_names:
        print("Sending to back end...")
        files = {'file': open(images, 'rb')}
        headers = {
            'username': username,
        }
        response = requests.request("POST", 'http://192.168.1.8:4000/upload', files=files, headers=headers)
        print(response)
    '''
    print("Backend Process Complete")
    context = {"data":"data"}
    return render(request, 'index.html', context)

@csrf_exempt
def runmodel(request):
    context = {"data":"data"}
    return render(request, 'index.html', context)
