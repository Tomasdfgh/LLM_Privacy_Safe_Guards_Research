import os
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt


def plot_histogram_from_hashmap(hashmap, title):

    data = []
    for i in hashmap:
        data.append(hashmap[i])

    plt.hist(data, bins = 100, edgecolor = 'black')
    plt.title(title)
    plt.xlabel("Different Words In Training Data")
    plt.ylabel("Frequency")
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
                        if w not in hashmap_:
                            hashmap_[w] = 1
                        else:
                            hashmap_[w] += 1
                print(f"Processed {filename}: {len(hashmap)} entries")

            except Exception as e:
                print(f"Error processing {filename}: {e}")
    
    return hashmap_

# Example usage
if __name__ == "__main__":
    folder_path = r"C:\Users\tomng\Desktop\Everything\Engineering Science\Fourth Year - Term 1\ESC499 - Thesis\data_breakdown\Method 2 - Vanilla Tokenizer"
    hashmap = load_hashmaps_from_excels(folder_path)
    title = "Distribution of Occurance of Words using Vanilla Tokenizer"
    plot_histogram_from_hashmap(hashmap, title)