from PIL import Image

# Sample image path (a placeholder since an actual image is not provided)
image_path = 'assets/img.png'  # Replace this with the actual image path like 'bird.jpg'

# Open the image
im = Image.open(image_path)

# Ensure the image is in RGBA mode (necessary for transparency)
if im.mode != 'RGBA':
    im = im.convert('RGBA')

width, height = im.size
pixels = im.load()

# Apply gradient transparency
for y in range(int(height * 0.55), int(height * 0.75)):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        alpha = a - int((y - height * 0.55) / (height * 0.20) * 255)
        alpha = max(alpha, 0)  # Ensure alpha doesn't go negative
        pixels[x, y] = (r, g, b, alpha)

# Set full transparency from the end of the gradient to the bottom of the image
for y in range(int(height * 0.75), height):
    for x in range(width):
        r, g, b, _ = pixels[x, y]
        pixels[x, y] = (r, g, b, 0)

# Save the modified image
modified_image_path = 'output.png'  # Output file path
im.save(modified_image_path)

modified_image_path
