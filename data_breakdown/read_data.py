import os
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import json

import general_functions as gf

def plot_histogram_from_hashmap(hashmap, title):

    data = []
    for i in hashmap:
        data.append(hashmap[i])

    plt.hist(data, bins = 5000, edgecolor = 'black', log = True)
    #plt.xscale('log')
    plt.title(title)
    plt.xlabel("Different Words In Training Data")
    plt.ylabel("Frequency")
    plt.show()

def plot_histograms_from_multiple_hashmaps(hashmaps, titles):
    num_plots = len(hashmaps)
    fig, axs = plt.subplots(1, num_plots, figsize=(6 * num_plots, 4))

    # If only one subplot, make axs iterable
    if num_plots == 1:
        axs = [axs]

    for idx, hashmap in enumerate(hashmaps):
        data = [value for value in hashmap.values()]
        axs[idx].hist(data, bins=5000, edgecolor='black', log=True)
        axs[idx].set_title(titles[idx])
        axs[idx].set_xlabel("Different Words In Training Data")
        axs[idx].set_ylabel("Frequency")

    plt.tight_layout()
    plt.show()


def load_hashmaps_from_excels(folder_path):
    hashmap_ = {}

    for filename in os.listdir(folder_path):
        if filename.endswith(".xlsx"):
            file_path = os.path.join(folder_path, filename)

            try:

                df = pd.read_excel(file_path, engine='openpyxl')
                hashmap = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))

                for w in hashmap:
                    if isinstance(hashmap[w], int):
                        w_copy = w
                        try:
                            w = w.lower()
                        except:
                            pass
                        if w not in hashmap_:
                            hashmap_[w] = hashmap[w_copy]
                        else:
                            hashmap_[w] += hashmap[w_copy]

                print(f"Processed {filename}: {len(hashmap)} entries")

            except Exception as e:
                print(f"Error processing {filename}: {e}")
    
    return hashmap_

if __name__ == "__main__":

    title_ = {
    1: "Simple Split",
    2: "Vanilla Tokenizer",
    3: "Semantic Split"
    }

    hashmaps = {
    1: r"C:\Users\tomng\Desktop\Everything\Engineering Science\Fourth Year - Term 1\ESC499 - Thesis\data_breakdown\Method 1 - Simple split\method_1_hashmap.json",
    2: r"C:\Users\tomng\Desktop\Everything\Engineering Science\Fourth Year - Term 1\ESC499 - Thesis\data_breakdown\Method 2 - Vanilla Tokenizer\method_2_hashmap.json",
    3: r"C:\Users\tomng\Desktop\Everything\Engineering Science\Fourth Year - Term 1\ESC499 - Thesis\data_breakdown\Method 3 - Semantics\method_3_hashmap.json",
    }


    #-----------------------Convert Excel Sheets to .json-------------------------------#

    convert_excel = False
    if convert_excel:

        #Define which word splitting method to convert
        method = 1
        
        excel_location = {
        1: r"C:\Users\tomng\Desktop\Everything\Engineering Science\Fourth Year - Term 1\ESC499 - Thesis\data_breakdown\Method 1 - Simple split",
        2: r"C:\Users\tomng\Desktop\Everything\Engineering Science\Fourth Year - Term 1\ESC499 - Thesis\data_breakdown\Method 2 - Vanilla Tokenizer",
        3: r"C:\Users\tomng\Desktop\Everything\Engineering Science\Fourth Year - Term 1\ESC499 - Thesis\data_breakdown\Method 3 - Semantics",
        }
        hashmap = load_hashmaps_from_excels(method_3)
        with open(hashmaps[method], "w", encoding="utf-8") as file:
            json.dump(hashmap, file)

    #------------------Plot the Distributions of Training Data--------------------------#

    plot = True
    if plot:
        hashmap_list = []
        titles = []
        for i in hashmaps:
            title = "Log-Scaled Distribution of Word Occurrences with " + title_[i]
            with open(hashmaps[i], 'r', encoding='utf-8') as file:
                hashmap_final = json.load(file)
            hashmap_list.append(hashmap_final)
            titles.append(title)

        plot_histograms_from_multiple_hashmaps(hashmap_list,titles)