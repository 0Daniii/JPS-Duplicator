import os
import sys

def cleanup_photos():
    # Manual input instead of popup window
    print("--- RAW/JPG Cleanup Tool ---")
    folder_selected = input("Drag and drop your photo folder here and press Enter: ").strip()
    
    # This cleans up the path if you drag and drop in macOS (removes extra quotes/spaces)
    folder_selected = folder_selected.replace("\\", "").replace("'", "").replace('"', '').strip()

    if not os.path.isdir(folder_selected):
        print(f"Error: '{folder_selected}' is not a valid folder.")
        return

    deleted_count = 0
    for filename in os.listdir(folder_selected):
        if filename.lower().endswith(".jpg"):
            base_name = os.path.splitext(filename)[0]
            
            # Check for .RW2 (standard Panasonic RAW)
            raw_file = base_name + ".RW2"
            raw_path = os.path.join(folder_selected, raw_file)

            if os.path.exists(raw_path):
                jpg_path = os.path.join(folder_selected, filename)
                try:
                    os.remove(jpg_path)
                    print(f"Deleted: {filename} (RAW version found)")
                    deleted_count += 1
                except Exception as e:
                    print(f"Could not delete {filename}: {e}")

    print("-" * 30)
    print(f"Done! Cleaned up {deleted_count} duplicate JPGs.")

if __name__ == "__main__":
    cleanup_photos()