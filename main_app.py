import numpy as np
import streamlit as st
import cv2
from tensorflow.keras.models import load_model #load the saved backend model

#Loading the Model
model = load_model('F:/PhD/Python/NLP practice (not to upload)/30 LIVE PROJECTS/plant disease/plant_disease_detection_and_prediction.h5')

#Name of Classes
CLASS_NAMES = ['Corn-Common_rust', 'Potato-Early_blight', 'Tomato-Bacterial_spot']

#Setting Title of App
st.title("Plant Disease Detection and Prediction")
st.markdown("Upload an image of the plant leaf")

#Uploading the plant leaf image
plant_image = st.file_uploader("Choose an image", type='jpg')
submit = st.button('Predict')

#Once the 'predict' button is clicked
if submit:
    if plant_image is not None:
        
        #Convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(plant_image.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        
        #Displaying the image
        st.image(opencv_image, channels="BGR")
        st.write(opencv_image.shape)
        
        #Resizing the image
        opencv_image = cv2.resize(opencv_image, (256, 256))
        
        #Convert image to 4 Dimensions
        opencv_image.shape = (1, 256, 256, 3)
        
        #Make Prediction
        Y_pred = model.predict(opencv_image)
        result = CLASS_NAMES[np.argmax(Y_pred)]
        st.title(str("This is" + result.split('-')[0] + "leaf with" + result.split('-')[1]))