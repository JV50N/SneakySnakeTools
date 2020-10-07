#!/usr/bin/python

# Before starting this application, install the Pillow Library
# pip3 install pillow

import sys

from PIL import Image
from PIL.ExifTags import TAGS

#path to the image or video
image_name = sys.argv[1]

#read the image data using PIL
image = Image.open(image_name)

# extracts image EXIF data
exif_data = image.getexif()

# Loop through all EXIF Data Fields
for tag_id in exif_data:
	# get the tag name, and display for a normal Human
	tag = TAGS.get(tag_id, tag_id)
	data = exif_data.get(tag_id)
	# decode the bytes
	if isinstance(data, bytes):
		data = data.decode()
	print(f"{tag:25}:{data}")


