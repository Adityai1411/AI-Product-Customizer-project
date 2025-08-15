import os
from PIL import Image

def ensure_dir(directory):
    """Create directory if it doesn't exist."""
    os.makedirs(directory, exist_ok=True)

def save_image(image, output_path):
    """Save PIL image to disk."""
    ensure_dir(os.path.dirname(output_path))
    image.save(output_path)
    print(f"[INFO] Saved image to {output_path}")
