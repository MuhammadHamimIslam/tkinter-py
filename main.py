from PIL import Image

# Load the image
input_path = "assets/download.png"
output_path = "assets/i.png"
new_size = (50, 50)  # width, height

# Open and resize
with Image.open(input_path) as img:
    resized_img = img.resize(new_size)
    resized_img.save(output_path)

print(f"Image resized to {new_size} and saved as {output_path}")