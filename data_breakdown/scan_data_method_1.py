import json
import os
import pandas as pd
from openpyxl import Workbook
import openpyxl
import re
from wordsegment import load, segment


# Initialize an empty list to store the data
def iterate_through_file(file_):

    load()
    data_hash = {}
    for n, i in enumerate(file_):
        
        with open(i, 'r', encoding='utf-8') as file:

            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    
                    data_line = []
                    obj = json.loads(line)
                    if obj['id'] % 1000 == 0:
                        print("File " + str(n) + ", id " + str(obj['id']))

                        
                    split_string = re.split(r'[ .,!?#\-\n]+', obj['text'])
                    for word in split_string:

                        word = word.lower()
                        word = re.sub(r'[!@;#$°%^&<*}~>•+●²=()/":…-]+', '', word)
                        word = word.replace("'", "")
                        word = word.replace("[", "")
                        word = word.replace("]", "")
                        words = [word]
                        data_line.extend(words)

                    data_line = set(data_line)

                    for w in data_line:

                        word = gf.remove_illegal_characters(w)
                        if word not in data_hash:
                            data_hash[word] = 1
                        else:
                            data_hash[word] += 1

                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON: {e}")
                    continue

    max_rows = 500000
    df = pd.DataFrame(list(data_hash.items()), columns=['Key', 'Value'])
    num_sheets = (len(df) // max_rows) + 1

    for i in range(num_sheets):
        start_row = i * max_rows
        end_row = (i + 1) * max_rows
        df_chunk = df.iloc[start_row:end_row]
        excel_link = r"data_file_" + str(i) + ".xlsx"
        create_new_workbook_with_sheet(excel_link)
        df_chunk.to_excel(excel_link, index=False)



if __name__ == "__main__":

    #Parameters:
    data_link = r"/home/nguyen/Training_Data_Test"

    #Get file links and generate excel file
    files = gf.get_file_paths(data_link)
    gf.iterate_through_file(files)
