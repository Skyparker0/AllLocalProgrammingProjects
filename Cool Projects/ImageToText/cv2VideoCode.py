# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:20:59 2021

@author: batte
"""

import numpy as np
import cv2
import sys
from PIL import Image
import PILImageFilters
import ImageToTextCode
import Splotch
# import tkinter as Tk

display_text = ""



def pil_to_cv2(pilImage):
    numpy_image = np.array(pilImage.convert("RGB"))  
    # convert to a openCV2 image, notice the COLOR_RGB2BGR which means that 
    # the color is converted from RGB to BGR format
    opencv_image=cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) 
    return opencv_image

def cv2_to_pil(cv2Image):
    color_coverted = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2RGB)
    pil_image=Image.fromarray(color_coverted)
    return pil_image

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# def task():
#     Tk.Label(root, justify=Tk.LEFT, text=display_text).pack()
#     root.after(1, task)  # reschedule event in 2 seconds
   
# root = Tk.Tk()   
# root.after(1, task)
# root.mainloop()


time = 0

while(True):
    time += 1
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    # Our operations on the frame come here    
    pil_image = cv2_to_pil(frame)
    
    edited_pil_image = Splotch.splotch(pil_image,time)#PILImageFilters.ditherFilter(pil_image)

    opencvImage = pil_to_cv2(edited_pil_image)

    #display_text = ImageToTextCode.alter_image_to_text(pil_image,15)
    # # Display the resulting frame
    cv2.imshow('editedframe',opencvImage)
    # cv2.imshow('originalframe',frame)
    #print(display_text)
    
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
sys.exit()