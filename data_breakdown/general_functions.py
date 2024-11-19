import json
import os
import pandas as pd
from openpyxl import Workbook
import openpyxl


def get_all_files(directory):

    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

def create_new_workbook_with_sheet(filename):
    workbook = Workbook()
    sheet = workbook.active
    workbook.save(filename)


def get_file_paths(directory, recursive=True):

    file_paths = []
    if recursive:
        for root, _, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
    else:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                file_paths.append(filepath)

    return file_paths

def remove_illegal_characters(value):
    illegal_chars = set(chr(i) for i in range(32)) | {chr(127)}
    if isinstance(value, str):
        # Remove illegal characters from the string
        return ''.join(char for char in value if char not in illegal_chars)
    return value

def load_hashmaps_from_folder(folder_path):

    hashmap = {}

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        print("File : " +str(filename))
        if filename.endswith(".json"):  # Only process .json files
            file_path = os.path.join(folder_path, filename)

            # Read the JSON file
            with open(file_path, 'r', encoding='utf-8') as file:
                try:

                    hashmap_ = json.load(file)  # Load the JSON content as a dictionary

                    #Add this to the big hashmap
                    for w in hashmap_:

                        if w not in hashmap:
                            hashmap[w] = 1
                        else:
                            hashmap[w] += 1

                except json.JSONDecodeError as e:
                    print(f"Error reading {filename}: {e}")

    return hashmap