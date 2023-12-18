from PIL import Image
import os
import random

def parse_yolo_annotation(yolo_annotation_file):
    with open(yolo_annotation_file, 'r') as file:
        lines = file.readlines()

    bounding_boxes = []
    for line in lines:
        elements = line.split()
        if len(elements) == 5:  # Assuming YOLO format: class x_center y_center width height
            x_center, y_center, width, height = map(float, elements[1:])
            x, y, w, h = int((x_center - width / 2) * image_width), int((y_center - height / 2) * image_height), int(width * image_width), int(height * image_height)
            bounding_boxes.append((x, y, w, h))

    return bounding_boxes


def add_small_images_to_bigger_image(bigger_image_path, small_images_folder, output_folder, bounding_boxes, num_small_images=5, small_image_size=80):
    # Open the bigger image
    bigger_image = Image.open(bigger_image_path)

    for box in bounding_boxes:
        x, y, w, h = box

        # Choose three random small images from the folder
        small_image_files = [f for f in os.listdir(small_images_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
        if len(small_image_files) < num_small_images:
            continue  # Skip if there are not enough valid small images

        chosen_small_images = random.sample(small_image_files, num_small_images)

        # Create a copy of the bigger image for each set of small images
        bigger_image_copy = bigger_image.copy()  # Create a copy to avoid overwriting the original image

        for small_image_filename in chosen_small_images:
            small_image = Image.open(os.path.join(small_images_folder, small_image_filename))

            # Resize small image to fixed size
            small_image = small_image.resize((small_image_size, small_image_size))

            # Randomly place small image inside the bounding box
            x_offset = random.randint(0, w - small_image_size)
            y_offset = random.randint(0, h - small_image_size)

            # Paste the small image onto the bigger image
            bigger_image_copy.paste(small_image, (x + x_offset, y + y_offset))

        # Save the result in the output folder
        output_image_name = f"output_image_{x}_{y}.png"  # You can customize the naming convention
        output_image_path = os.path.join(output_folder, output_image_name)
        bigger_image_copy.save(output_image_path)


# Example usage:
bigger_image_path = ''
small_images_folder = ''
output_image_path = ''
yolo_annotation_file = ''

# Get image dimensions (replace with actual dimensions)
image_width = 1440
image_height = 1088

# Parse YOLO annotation to get bounding boxes
bounding_boxes = parse_yolo_annotation(yolo_annotation_file)

# Add small images to the bigger image
add_small_images_to_bigger_image(bigger_image_path, small_images_folder, output_image_path, bounding_boxes)
