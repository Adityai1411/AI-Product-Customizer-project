from rembg import remove
from PIL import Image
import os

def remove_bg(input_path, output_path):
    """
    Remove background from an image using rembg.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    input_image = Image.open(input_path).convert("RGBA")
    output_image = remove(input_image)
    output_image.save(output_path)
    print(f"[INFO] Background removed and saved to {output_path}")
