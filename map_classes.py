import os

def change_class_names(input_folder, output_folder, class_mapping):
    for filename in os.listdir(input_folder):
        if filename.startswith('PXL') and filename.endswith('.txt'):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename)

            with open(input_file, 'r') as infile:
                lines = infile.readlines()

            updated_lines = []
            for line in lines:
                elements = line.split()
                if len(elements) > 0:
                    class_id = elements[0]
                    if class_id in class_mapping:
                        elements[0] = class_mapping[class_id]
                        updated_lines.append(' '.join(elements) + '\n')

            with open(output_file, 'w') as outfile:
                outfile.writelines(updated_lines)

# Replace 'input_folder' and 'output_folder' with your actual input and output folder paths
input_folder = 'path/to/val/labels/folder'
output_folder = 'path/to/val/labels/folder'


# # Define a mapping from class numbers to class names
# class_mapping = {
#     0: 'give_way',
#     1: 'direction',
#     2: 'bus_stop',
#     3: 'no_entry',
#     4: 'street_name',
#     5: 'sticker',
#     6: 'crosswalk',
#     7: 'speedlimit',
#     8: 'trafficlight',
#     9: 'stop'
# }


# Define a mapping from class numbers to class names
class_mapping = {
    'give_way': '0',
    'direction': '1',
    'bus_stop':'2',
    'no_entry':'3',
    'street_name':'4',
    'sticker':'5',
    'crosswalk':'6',
    'speedlimit':'7',
    'trafficlight':'8',
    'stop':'9'
}

change_class_names(input_folder, output_folder, class_mapping)
