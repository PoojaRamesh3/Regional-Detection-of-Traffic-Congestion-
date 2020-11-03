# Program To Read video 
# and Extract Frames 
import cv2
import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import os 
from os.path import isfile, join
import convert as cvt


img_width, img_height = 150, 150
model_path = './models/model.h5'
model_weights_path = './models/weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)

def predict(file):
  x = load_img(file, target_size=(img_width,img_height))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = model.predict(x)
  result = array[0]
  answer = np.argmax(result)
  res=""
  print(answer)
  if answer == 0:
    res="Accident"
    print("Label: Accident")
  elif answer == 1:
    res="Heavy Traffic"
    print("Labels: Heavy Traffic")
  elif answer == 2:
    res="Fire Accident"
    print("Label: Fire Accident")
  elif answer == 3:
    res="Low Traffic"
    print("Label: Low Traffic")

  return res

# Function to extract frames 
def FrameCapture(path): 
	
	# Path to video file 
	vidObj = cv2.VideoCapture(path) 

	# Used as counter variable 
	count = 0

	# checks whether frames were extracted 
	success = 1
	while success: 
		# vidObj object calls read 
		# function extract frames 
		success, image = vidObj.read() 
		# Saves the frames with frame-count 
		cv2.imwrite("frame/frame%d.jpg" % count, image) 
		result = predict("frame/frame"+str(count)+".jpg")
		image = cv2.imread("frame/frame"+str(count)+".jpg")
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(image, str(result) ,(219,151), font, 5,(0,0,255),5,cv2.LINE_AA)
		cv2.imwrite("frame/frame"+str(count)+".jpg", image)
		print(count,result)
		count += 1
		if count==100:
			break
	
 
def process(path):
	# Calling the function 
	FrameCapture(path) 
	cvt.process()