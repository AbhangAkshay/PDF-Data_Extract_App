import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import easyocr
import os
from PIL import Image

# from app_req import data_dir

image_path = r"App\Output\image_1.jpg"
output_folder = r"App"

reader = easyocr.Reader(['en'])


def read_text_from_image(image_path):
    
    image = cv2.imread(image_path)
    
    results = reader.readtext(image_path)
    image = cv2.imread(image_path)
    
    return image, results

image,results = read_text_from_image(image_path)

print(image,results)

def find_and_extract_text_bbox(image, results, target_text):
    image = Image.fromarray(image)
    width = image.width
    text_bbox = None  # Initialize the variable to store the bounding box
    
    for (bbox, text, prob) in results:
        text_lower = str(text).lower()
        if text_lower == target_text:
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = (int(top_left[0]), int(top_left[1]))
            top_right = (int(top_right[0]), int(top_right[1]))
            bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
            bottom_left = (int(bottom_left[0]), int(bottom_left[1]))

            text, prob, text_bbox = text, prob, (0,top_left[1], width, bottom_right[1])
            return text, prob, text_bbox

# # find_and_extract_text_bbox(image, results, target_text)        



def crop_and_save(image,bbox,label,output_folder):
    im = Image.fromarray(image)
    roi = im.crop(bbox)
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Define the output path
    output_path = os.path.join(output_folder, f"{label}.jpg")
    
    # Save the cropped image
    roi.save(output_path)


test1 = ['haemoglobin', 'rbc count', 'lymphocytes', 'monocytes']
output_folder = 'CROP-IMGS'
for target_text in test1:
    text, prob, text_bbox = find_and_extract_text_bbox(image, results, target_text)
    print(target_text, text, prob, text_bbox)
    crop_and_save(image, text_bbox, target_text, output_folder)
    
