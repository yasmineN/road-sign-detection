# Objective

Pre process data to be compatabile for YOLO.

Translate XML files that contains a bounding box to txt YOLO format.

Image manipluation: eg. adding smaller images inside images.

Detect road signs: cross walk, Stop, give way, etc.



Steps:

1. Convert files from xml to txt yolo format (optional if annotation is already in txt) or use

''' from preprocessing import convert_voc_to_yolo
	convert_voc_to_yolo()
	'''

2. Map the detected classes to place inside the txt file (optional)


