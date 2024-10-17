from PIL import Image
import os

def resize_images(directory, sizes):
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img = Image.open(os.path.join(directory, filename))
            for size in sizes:
                resized_img = img.resize(size)
                resized_filename = f"{size[0]}x{size[1]}_resized_{filename}"
                resized_img.save(os.path.join(directory, resized_filename))
                print(f"Saved: {resized_filename}")

if __name__ == "__main__":
    dir_path = input("Enter the directory path: ")
    
    size_input = input("Enter new sizes (width height) separated by commas (e.g., 800 600, 1024 768): ")
    sizes = [tuple(map(int, size.strip().split())) for size in size_input.split(',')]
    
    resize_images(dir_path, sizes)
    print("Images resized.")
