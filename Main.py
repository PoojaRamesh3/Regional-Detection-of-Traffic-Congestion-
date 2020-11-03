import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd

import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
import train as TR
import predict as PR
import video as vid
import cv2
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.preprocessing import image

bgcolor="#DAF7A6"
bgcolor1="#B7C526"
fgcolor="black"


def Home():
	global window
	def clear():
	    print("Clear1")
	    txt.delete(0, 'end')
	    txt1.delete(0, 'end')
	    txt2.delete(0, 'end')



	window = tk.Tk()
	window.title("Traffic Prediction")

 
	window.geometry('1280x720')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen', True)

	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)
	

	message1 = tk.Label(window, text="Traffic Prediction" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	message1.place(x=100, y=20)

	lbl = tk.Label(window, text="Select Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl.place(x=100, y=200)
	
	txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt.place(x=400, y=215)

	lbl1 = tk.Label(window, text="Select Image",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl1.place(x=100, y=300)
	
	txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt1.place(x=400, y=315)

	lbl2 = tk.Label(window, text="Select Video",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl2.place(x=100, y=400)
	
	txt2 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt2.place(x=400, y=415)

	def browse():
		path=filedialog.askdirectory()
		print(path)
		txt.delete(0, 'end')
		txt.insert('end',path)
		if path !="":
			print(path)
		else:
			tm.showinfo("Input error", "Select Dataset Folder")	

	def browse1():
		path=filedialog.askopenfilename()
		print(path)
		txt1.delete(0, 'end')
		txt1.insert('end',path)
		if path !="":
			print(path)
		else:
			tm.showinfo("Input error", "Select Image")	

	def browse2():
		path=filedialog.askopenfilename()
		print(path)
		txt2.delete(0, 'end')
		txt2.insert('end',path)
		if path !="":
			print(path)
		else:
			tm.showinfo("Input error", "Select Video")	

	def trainprocess():
		sym=txt.get()
		if sym != "" :
			TR.process(sym,4)
			tm.showinfo("Input", "Training Successfully Finished")
		else:
			tm.showinfo("Input error", "Select Dataset")

	def predictimgprocess():
		sym=txt1.get()
		if sym != "" :
			result=PR.process(sym)
			#tm.showinfo("Input", res)
			img = cv2.imread(sym)
			font = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(img, str(result) ,(19,51), font, 1,(0,0,255),5,cv2.LINE_AA)
			cv2.imwrite("output.jpg", img)
			plt.imshow(image.load_img("output.jpg"))
			plt.show()
			#plt.imshow(image.load_img(np.random.choice(image_files)))
			#plt.show()
			
		else:
			tm.showinfo("Input error", "Select image File")
	
	def predictvideoprocess():
		sym=txt2.get()
		if sym != "" :
			vid.process(sym)
			#tm.showinfo("Input", res)
			cap = cv2.VideoCapture('video.avi')
			 
			# Read until video is completed
			while(cap.isOpened()):
			  # Capture frame-by-frame
			  ret, frame = cap.read()
			  if ret == True:
			 
			    # Display the resulting frame
			    cv2.imshow('Frame',frame)
			 
			    # Press Q on keyboard to  exit
			    if cv2.waitKey(25) & 0xFF == ord('q'):
			      break
			 
			  # Break the loop
			  else: 
			    break
			 
			# When everything done, release the video capture object
			cap.release()
			 
			# Closes all the frames
			cv2.destroyAllWindows()
		else:
			tm.showinfo("Input error", "Select Video")

	browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	browse.place(x=650, y=200)

	browse1 = tk.Button(window, text="Browse", command=browse1  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	browse1.place(x=650, y=300)

	browse2 = tk.Button(window, text="Browse", command=browse2  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	browse2.place(x=650, y=400)

	clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
	clearButton.place(x=950, y=200)
	 
	trainbutton = tk.Button(window, text="Train", command=trainprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	trainbutton.place(x=270, y=600)

	prbutton = tk.Button(window, text="Image Predict", command=predictimgprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	prbutton.place(x=540, y=600)

	vprbutton = tk.Button(window, text="Video Predict", command=predictvideoprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	vprbutton.place(x=800, y=600)

	#NNbutton = tk.Button(window, text="NEURAL NETWORK", command=NNprocess  ,fg=fgcolor   ,bg=bgcolor1 ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	#NNbutton.place(x=620, y=600)


	quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	quitWindow.place(x=1060, y=600)

	window.mainloop()
Home()

