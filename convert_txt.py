import os
import xml.etree.ElementTree as ET


'''
 The script aims to convert XML files to a text file compatible with YOLO
 Steps:
 1. Parse XML
 2. Convert to YOLO Format
 3. Save the new txt files
'''

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    object_info = {}
    for dim in root.findall('.//size'):
         width = int(dim.find('width').text)
         height = int(dim.find('height').text)
    for obj in root.findall('.//object'):
        name = obj.find('name').text
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
    

        object_info[name] = (xmin, ymin, xmax, ymax, width, height)

    return object_info

def convert_to_yolo_format(object_info):
    yolo_format_lines = []
    #print(object_info)

    for label, bbox in object_info.items():
        x_center = (bbox[0] + bbox[2]) / (2 * bbox[4])
        y_center = (bbox[1] + bbox[3]) / (2 * bbox[5])
        width = (bbox[2] - bbox[0]) / bbox[4]
        height = (bbox[3] - bbox[1]) / bbox[5]

        yolo_line = f"{label} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"
        yolo_format_lines.append(yolo_line)

    return yolo_format_lines

def write_to_txt_file(output_file, yolo_format_lines):
    with open(output_file, 'w') as file:
        for line in yolo_format_lines:
            file.write(line + '\n')

def process_folder(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.xml'):
            xml_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.txt')

            # image_width = 400  # replace with the actual image width
            # image_height = 300  # replace with the actual image height

            object_info = parse_xml(xml_file)
            yolo_format_lines = convert_to_yolo_format(object_info)
            write_to_txt_file(output_file, yolo_format_lines)

# Replace 'input_folder' and 'output_folder' with your actual input and output folder paths
input_folder = '/Users/yn/Projects/Yolo/images_phone/labels/xml'
output_folder = '/Users/yn/Projects/Yolo/images_phone/labels/train'

process_folder(input_folder, output_folder)
