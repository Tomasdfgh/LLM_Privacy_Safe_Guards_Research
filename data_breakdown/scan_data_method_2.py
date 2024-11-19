import json
import os
import pandas as pd
from openpyxl import Workbook
import openpyxl
import re
import nltk
from nltk.tokenize import word_tokenize

import general_functions as gf

# Initialize an empty list to store the data
def iterate_through_file(file_, med2_link, existing_files):

    #Download the tokenizer model
    nltk.download('punkt')

    for n, i in enumerate(file_):
        
        with open(i, 'r', encoding='utf-8') as file:

            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:

                    data_hash = {}
                    data_line = []
                    obj = json.loads(line)
                    if obj['id'] % 1 == 0:
                        print("File " + str(n) + ", id " + str(obj['id']))

                    json_name = f"{obj['id']}.json"
                    save_path = os.path.join(med2_link, json_name)

                    if save_path not in existing_files:


                        words = word_tokenize(obj['text'])
                        data_line.extend(words)
                        data_line = set(data_line)

                        for w in data_line:

                            word = gf.remove_illegal_characters(w)
                            if word not in data_hash:
                                data_hash[word] = 1
                            else:
                                data_hash[word] += 1

                        #Save the hashmap for a later use
                        with open(save_path, "w", encoding="utf-8") as file:
                            json.dump(data_hash, file)

                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON: {e}")
                    continue


if __name__ == "__main__":

    #Parameters:
    data_link = r"C:\Users\tomng\Desktop\Training_Data_Ordered"
    med_2_save_link = r"C:\Users\tomng\Desktop\Med2_map"

    # #Get file links and generate excel file
    # existing_files = gf.get_all_files(med_3_save_link)
    # files = gf.get_file_paths(data_link)
    # iterate_through_file(files,med_3_save_link, existing_files)

    print("Done creating .json files")
    hashmap = gf.load_hashmaps_from_folder(med_2_save_link)

    max_rows = 500000
    df = pd.DataFrame(list(hashmap.items()), columns=['Key', 'Value'])
    num_sheets = (len(df) // max_rows) + 1

    for i in range(num_sheets):
        start_row = i * max_rows
        end_row = (i + 1) * max_rows
        df_chunk = df.iloc[start_row:end_row]
        excel_link = r"data_file_" + str(i) + ".xlsx"
        gf.create_new_workbook_with_sheet(excel_link)
        df_chunk.to_excel(excel_link, index=False)

