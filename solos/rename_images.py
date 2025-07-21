import os


folder_path = r"C:\work\fortunecoffee\solos\symbol-revealed"  

prefix = "eye_"                   
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')


for filename in os.listdir(folder_path):
    if filename.lower().endswith(image_extensions):
        old_path = os.path.join(folder_path, filename)
        new_filename = prefix + filename
        new_path = os.path.join(folder_path, new_filename)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_filename}")

print("✅ Done renaming all image files.")
