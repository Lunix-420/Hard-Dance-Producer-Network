#======================================================================================================================
# Script for Kick of the Month @HardDanceProducerNetwork Discord server (https://discord.gg/UytMWCzPDr)
# 
# This script renames and copies all files in it's folder to a new folder.
# When finished, it prints a legend of the original file names and the new names enumerated with emojis
# 
# Usage:
#   1. Place this script in the folder containing the files you want to rename
#   2. Run the script
#   3. Check the "renamed" folder for the renamed files
#
# Note: This script will not rename itself or any Python files in the folder
#
# AUTHOR: Lunix @discordapp.com/users/lunix420
# DATE: 2023-01-13
#======================================================================================================================

import os
import shutil
from pathlib import Path

def generate_emojis():
    emojis = [
        "🌟", "📎", "📌", "🔖", "📂", "📃", "🎉", "💼", "📷", "📹",
        "📀", "📆", "🎨", "🎤", "🎸", "🎮", "🕹️", "📡", "🚀", "🛰️",
        "🔍", "📚", "📝", "🔐", "🔑", "🔒", "🔓", "💡", "🔦", "📸",
        "📽️", "🎬", "🎥", "🎭", "🎨", "🎤", "🎧", "🎹", "🎷", "🎺",
        "🎻", "🥁", "🎲", "🎯", "🎳", "🎰", "🚁", "🚂", "🚗", "🚤",
        "🍕", "🌮", "🍔", "🍟", "🥪", "🍱", "🍲", "🍜", "🍝", "🍛",
        "🍣", "🍤", "🍥", "🍙", "🍚", "🍜", "🍢", "🍡", "🍧", "🍨",
        "🍩", "🍪", "🎂", "🍰", "🧁", "🥧", "🍫", "🍬", "🍭", "🍮",
        "🍯", "🍎", "🍏", "🍐", "🍑", "🍒", "🍓", "🥝", "🍈", "🍇",
        # Add more emojis if needed
    ]

    return emojis

def enumerate_with_emojis(file_list):
    emojis = generate_emojis()

    enumerated_files = []
    for index, file_path in enumerate(file_list):
        emoji = emojis[index % len(emojis)]
        # Construct the new filename with emoji and original file extension
        new_name = f"Kick #{index}{file_path.suffix}"
        enumerated_files.append((emoji, file_path, new_name))

    return enumerated_files

def move_and_rename_files(source_folder, destination_folder):
    source_folder_path = Path(source_folder)
    destination_folder_path = source_folder_path / "renamed"

    # Create "renamed" folder if it doesn't exist
    destination_folder_path.mkdir(parents=True, exist_ok=True)

    # Get a list of all files in the source folder (excluding Python files)
    all_files = [file for file in source_folder_path.glob("*") if file.is_file() and file.suffix.lower() != ".py"]

    # Enumerate files with emojis
    enumerated_files = enumerate_with_emojis(all_files)
    
    # Print list
    for (emoji, source_file, new_name) in enumerated_files:
        # Construct the destination path
        destination_file = destination_folder_path / new_name

        # Copy and rename the file, keeping the original file
        shutil.copy2(str(source_file), str(destination_file))

        # Print legend entry
        print("{:<0} {:<20} {:<50}".format(emoji + "-", new_name, source_file.name))

    print("="*60)

if __name__ == "__main__":
    source_folder_path = "."  # Change this to the path of the folder containing your files
    move_and_rename_files(source_folder_path, "renamed")
