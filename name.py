import os
from pathlib import Path

def rename_images_to_numbers(folder_path):
    """
    Renames all image files in the specified folder to numbered names (1.jpg, 2.jpg, etc.)
    Properly handles existing numbered files by renaming them first.
    """
    # Define common image extensions (added .jfif)
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.jfif'}
    
    folder = Path(folder_path)
    
    # Get all image files from the folder
    image_files = []
    for file in folder.iterdir():
        if file.is_file() and file.suffix.lower() in image_extensions:
            image_files.append(file)
    
    # Sort files to maintain consistent order
    image_files.sort()
    
    # Check if there are any images to rename
    if not image_files:
        print(f"No image files found in {folder_path}")
        return
    
    print(f"Found {len(image_files)} image(s) to rename:")
    
    # Strategy: First rename to temporary names, then to final names
    # This avoids conflicts with existing numbered files
    
    # Step 1: Rename all files to temporary names
    temp_files = []
    for i, image_file in enumerate(image_files, 1):
        temp_name = f"__temp_{i}.jpg"
        temp_path = folder / temp_name
        try:
            image_file.rename(temp_path)
            temp_files.append(temp_path)
            print(f"Step 1: {image_file.name} -> {temp_name}")
        except Exception as e:
            print(f"Error renaming {image_file.name} to temporary name: {e}")
    
    # Step 2: Rename temporary files to final names
    for i, temp_file in enumerate(temp_files, 1):
        new_name = f"{i}.jpg"
        new_path = folder / new_name
        try:
            temp_file.rename(new_path)
            print(f"Step 2: {temp_file.name} -> {new_name}")
        except Exception as e:
            print(f"Error renaming {temp_file.name} to {new_name}: {e}")
    
    print("Renaming complete!")

if __name__ == "__main__":
    # Get folder path from user input or use current directory
    folder_path = input("Enter folder path (press Enter for current directory): ").strip()
    
    if not folder_path:
        folder_path = os.getcwd()
    
    # Validate folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist!")
    else:
        rename_images_to_numbers(folder_path)
