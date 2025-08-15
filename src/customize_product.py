# customize_product.py
from diffusers import StableDiffusionImg2ImgPipeline
import torch
from PIL import Image
import os

def apply_customization(input_image_path, prompt, output_image_path):
    """Apply AI customization to a product using Stable Diffusion (img2img)."""
    device = "cuda" if torch.cuda.is_available() else "cpu"

    pipe = StableDiffusionImg2ImgPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
    pipe = pipe.to(device)

    init_image = Image.open(input_image_path).convert("RGB").resize((512, 512))
    image = pipe(prompt=prompt, image=init_image, strength=0.7).images[0]

    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
    image.save(output_image_path)
    print(f"[INFO] Customized product saved to {output_image_path}")


