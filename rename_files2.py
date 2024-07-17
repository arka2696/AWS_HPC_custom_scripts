import os
import re
import shutil

# Define the directory containing the original files
source_directory = r'C:\Users\nqg26\Desktop\Py\rename_files\Input'

# Define the directory to save the renamed files
target_directory = r'C:\Users\nqg26\Desktop\Py\rename_files\Output'

# Create the target directory if it doesn't exist
os.makedirs(target_directory, exist_ok=True)

# Define the regex pattern to match old file names (case insensitive)
pattern = re.compile(r'scan_Plate_D_p00_0_([A-D]\d{2})f(\d{2})d(\d)\.tif', re.IGNORECASE)

# Define the constants for the new file name format
new_plate = 'BBBC013'

# Iterate over files in the source directory
for filename in os.listdir(source_directory):
    print(f'Processing file: {filename}')
    # Check if the file name matches the regex pattern
    match = pattern.match(filename)
    if match:
        # Extract the matched groups
        well_position = match.group(1)  # e.g., A02
        site_number = match.group(2)    # e.g., 00
        channel_number = match.group(3) # e.g., 0
        
        # Create the new file name using the extracted groups
        new_filename = f'{new_plate}_{well_position}_s{site_number}_w{channel_number}.tif'
        
        # Get the full paths
        old_file_path = os.path.join(source_directory, filename)
        new_file_path = os.path.join(target_directory, new_filename)
        
        print(f'Old file path: {old_file_path}')
        print(f'New file path: {new_file_path}')
        
        # Check if the old file exists
        if os.path.exists(old_file_path):
            # Copy and rename the file
            shutil.copy2(old_file_path, new_file_path)
            print(f'Copied and renamed: {filename} -> {new_filename}')
        else:
            print(f'File not found: {old_file_path}')
    else:
        print(f'File name does not match pattern: {filename}')

print('Renaming and copying completed.')
