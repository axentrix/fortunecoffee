import os
from PIL import Image

# Root folder where your 6 folders are located
root_input = "all_images"
root_output = "output_webp"

# Create output root if it doesn't exist
os.makedirs(root_output, exist_ok=True)

# Walk through all subdirectories
for dirpath, dirnames, filenames in os.walk(root_input):
    for filename in filenames:
        if filename.lower().endswith(".png"):
            input_path = os.path.join(dirpath, filename)

            # Create corresponding output path
            relative_path = os.path.relpath(dirpath, root_input)
            output_dir = os.path.join(root_output, relative_path)
            os.makedirs(output_dir, exist_ok=True)

            # Build output filename
            output_filename = os.path.splitext(filename)[0] + ".webp"
            output_path = os.path.join(output_dir, output_filename)

            # Convert and save
            with Image.open(input_path) as img:
                img.save(output_path, "WEBP")
                print(f"Converted: {input_path} → {output_path}")
