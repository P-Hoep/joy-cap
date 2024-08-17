import os
from PIL import Image

def resize_and_crop(image, target_size):
    # Calculate the ratio to resize the image while ensuring it is at least target_size in both dimensions
    width, height = image.size
    ratio = max(target_size / width, target_size / height)

    new_width = int(width * ratio)
    new_height = int(height * ratio)

    # Resize the image with the new dimensions
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)

    # Now, center crop the resized image to the target size
    left = (new_width - target_size) / 2
    top = (new_height - target_size) / 2
    right = (new_width + target_size) / 2
    bottom = (new_height + target_size) / 2

    return resized_image.crop((left, top, right, bottom))

def process_images(directory, target_size=1024):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        try:
            with Image.open(file_path) as img:
                width, height = img.size

                if width >= target_size and height >= target_size:
                    resized_and_cropped_img = resize_and_crop(img, target_size)
                    resized_and_cropped_img.save(file_path)  # Overwrite the original image
                    print(f"Processed and saved: {filename}")
                else:
                    os.remove(file_path)
                    print(f"Deleted: {filename}")

        except Exception as e:
            print(f"Could not process {filename}: {e}")

if __name__ == "__main__":
    directory = "images"  # Replace with the path to your images directory
    process_images(directory)
