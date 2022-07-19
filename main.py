import os
import shutil
from PIL import Image
#user_input = input("Enter the path of your file: ")
start = input("Enter the timestamp in seconds:")
start = float(start)
user_input = "/Users/sowbaranika/Desktop/Images 2/testing/"
img_dict = {}
for image in os.listdir(user_input):
 file_name_full = os.path.join(user_input, image)
 timestamp = os.path.getmtime(file_name_full)
 img_dict[timestamp] = file_name_full
timestamp_min = min(img_dict.keys())
for image in os.listdir(user_input):
     print(img_dict[timestamp_min])
     Image2 = Image.open(img_dict[timestamp_min])
     Image2.show()
     os.rename(img_dict[timestamp_min], user_input + "Processed_" + image)
     timestamp_min = timestamp_min + start



