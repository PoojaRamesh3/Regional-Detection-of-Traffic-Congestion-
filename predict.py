import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from keras.preprocessing import image



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

def process(path):
	result = predict(path)
	return result
