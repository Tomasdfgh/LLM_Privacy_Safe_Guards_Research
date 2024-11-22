import general_functions as gf
import json

if __name__ == "__main__":

    #---------------------------------------Primary Setup---------------------------------------#

    #Hyperparameters
    method = 2 #1,2 or 3 only
    datapoints = r"C:\Users\tomng\Desktop\Dataset\top_k\50"
    hashmap = {
    1: r"C:\Users\tomng\Desktop\Everything\Engineering Science\Fourth Year - Term 1\ESC499 - Thesis\data_breakdown\Method 1 - Simple split\method_1_hashmap.json",
    2: r"C:\Users\tomng\Desktop\Everything\Engineering Science\Fourth Year - Term 1\ESC499 - Thesis\data_breakdown\Method 2 - Vanilla Tokenizer\method_2_hashmap.json",
    #3: r"C:\Users\tomng\Desktop\Everything\Engineering Science\Fourth Year - Term 1\ESC499 - Thesis\data_breakdown\Method 3 - Semantics\method_3_hashmap.json",
    }

    #Get all the training files in the training dataset
    files = gf.get_all_files(datapoints)


    #--------------------------------------Main Setup----------------------------------------#

    #Plotting Indicators
    plot_single = False
    if plot_single:

        #Open up the hashmap
        with open(hashmap[method], 'r', encoding='utf-8') as file:
            hashmap_ = json.load(file)

        counter, not_founded, k_below_5, k_below_10 = gf.perform_test(files, hashmap_, method)
        gf.plot_histogram_from_hashmap(counter,not_founded, k_below_5, k_below_10, method)

    plot_all = True
    if plot_all:

        counter = []
        not_founded = []
        k_below_5 = []
        k_below_10 = []
        hashmap_ = []

        for i in hashmap:
            with open(hashmap[i], 'r', encoding='utf-8') as file:
                hashmap_.append(json.load(file))

            counter_, not_founded_, k_below_5_, k_below_10_ = gf.perform_test(files, hashmap_[i- 1], i)
            counter.append(counter_)
            not_founded.append(not_founded_)
            k_below_5.append(k_below_5_)
            k_below_10.append(k_below_10_)


        gf.plot_all_histogram_from_hashmap(counter,not_founded, k_below_5, k_below_10)