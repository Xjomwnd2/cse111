import os
import shutil
from datetime import datetime
import pytest

def create_directory(directory):
    """Create a directory if it doesn't exist.
    
    Parameters:
        directory: str - Path to the directory
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_file_extension(filename):
    """Get the extension of a file.
    
    Parameters:
        filename: str - Name of the file
    Returns:
        str - Extension of the file
    """
    return os.path.splitext(filename)[1].lower()

def organize_files(source_dir, dest_dir):
    """Organize files from source directory into categorized folders.
    
    Parameters:
        source_dir: str - Source directory containing files
        dest_dir: str - Destination directory for organized files
    Returns:
        dict - Summary of moved files
    """
    # Create destination directory
    create_directory(dest_dir)
    
    # Initialize counters
    summary = {"images": 0, "documents": 0, "audio": 0, "other": 0}
    
    # File extension mappings
    extensions = {
        "images": [".jpg", ".jpeg", ".png", ".gif"],
        "documents": [".doc", ".docx", ".pdf", ".txt"],
        "audio": [".mp3", ".wav", ".flac"]
    }
    
    try:
        # Iterate through files in source directory
        for filename in os.listdir(source_dir):
            if os.path.isfile(os.path.join(source_dir, filename)):
                ext = get_file_extension(filename)
                
                # Determine category
                category = "other"
                for cat, exts in extensions.items():
                    if ext in exts:
                        category = cat
                        break
                
                # Create category directory
                category_dir = os.path.join(dest_dir, category)
                create_directory(category_dir)
                
                # Move file
                shutil.move(
                    os.path.join(source_dir, filename),
                    os.path.join(category_dir, filename)
                )
                
                # Update summary
                summary[category] += 1
                
        return summary
    
    except Exception as e:
        print(f"Error organizing files: {str(e)}")
        return summary

def main():
    source = input("Enter source directory path: ")
    dest = input("Enter destination directory path: ")
    
    if os.path.exists(source):
        summary = organize_files(source, dest)
        print("\nOrganization Summary:")
        for category, count in summary.items():
            print(f"{category.capitalize()}: {count} files")
    else:
        print("Source directory does not exist!")

# Test functions
def test_get_file_extension():
    assert get_file_extension("test.txt") == ".txt"
    assert get_file_extension("image.JPG") == ".jpg"
    assert get_file_extension("noextension") == ""

if __name__ == "__main__":
    main()