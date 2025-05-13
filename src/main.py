import os
import shutil
from pathlib import Path
from page import generate_pages_recursive

def copy_static(source_dir: str, dest_dir: str) -> None:
    """
    Recursively copy all files from source_dir to dest_dir.
    First deletes all contents of dest_dir to ensure a clean copy.
    """
    # Delete the destination directory if it exists
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    
    # Create the destination directory
    os.makedirs(dest_dir)
    
    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        # Calculate the relative path from source_dir
        rel_path = os.path.relpath(root, source_dir)
        
        # Create corresponding directories in dest_dir
        for dir_name in dirs:
            src_dir = os.path.join(root, dir_name)
            dst_dir = os.path.join(dest_dir, rel_path, dir_name)
            os.makedirs(dst_dir)
            print(f"Created directory: {dst_dir}")
        
        # Copy files
        for file_name in files:
            src_file = os.path.join(root, file_name)
            dst_file = os.path.join(dest_dir, rel_path, file_name)
            shutil.copy2(src_file, dst_file)
            print(f"Copied file: {dst_file}")

def main():
    # Copy static files to public directory
    copy_static("static", "public")
    
    # Generate all pages from content directory
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()

