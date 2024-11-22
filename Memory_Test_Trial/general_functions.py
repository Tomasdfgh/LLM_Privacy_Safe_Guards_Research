import os
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import re
import nltk
from nltk.tokenize import word_tokenize


def plot_histogram_from_hashmap(l, not_founded,k_below_5, k_below_10, method):

	title = {1: "Simple Split", 2: "Vanilla Tokenizer", 3: "Semantics Split"}
	title_use = "Frequency of words based on their presence in the training dataset: " + title[method]
	
	percent_not_found = str(round(100 * not_founded/(len(l) + not_founded),4))
	k_5 = str(round(100 * k_below_5/(len(l) + not_founded), 4))
	k_10 = str(round(100 * k_below_10/(len(l) + not_founded), 4))
	text_on_hist = "Percentage of words unrecognizable: " + percent_not_found + "%"
	text_k_5 = "Percentage of words memorized with k = 5: " + k_5 + "%"
	text_k_10 = "Percentage of words memorized with k = 10: " + k_10 + "%"

	plt.figure(figsize=(7, 4))
	plt.text(0.1, 0.9,text_on_hist,transform=plt.gca().transAxes,fontsize=7, color="black")
	plt.text(0.1, 0.86,text_k_5,transform=plt.gca().transAxes,fontsize=7, color="black")
	plt.text(0.1, 0.82,text_k_10,transform=plt.gca().transAxes,fontsize=7, color="black")
	plt.hist(l, bins = 500, edgecolor = 'black')
	plt.title(title_use, fontsize=7)
	plt.xlabel("Number of times a word occur in a training datapoint", fontsize = 7)
	plt.ylabel("Number of times that word is generated", fontsize = 7)
	plt.show()

def plot_all_histogram_from_hashmap(l, not_founded, k_below_5, k_below_10):


	# Create a figure with 2 subplots horizontally
	fig, axs = plt.subplots(1, 2, figsize=(14, 4))


	title = {1: "Simple Split", 2: "Vanilla Tokenizer", }
	#3: "Semantics Split"}

	for i in title:

		percent_not_found = str(round(100 * not_founded[i - 1] / (len(l[i - 1]) + not_founded[i - 1]), 4))
		k_5 = str(round(100 * k_below_5[i - 1] / (len(l[i - 1]) + not_founded[i - 1]), 4))
		k_10 = str(round(100 * k_below_10[i - 1] / (len(l[i - 1]) + not_founded[i - 1]), 4))
		
		text_on_hist = "Percentage of words unrecognizable: " + percent_not_found + "%"
		text_k_5 = "Percentage of words memorized with k = 5: " + k_5 + "%"
		text_k_10 = "Percentage of words memorized with k = 10: " + k_10 + "%"

		# First subplot
		title_use = "Frequency of words based on their presence in the training dataset: " + title[i]
		axs[i - 1].hist(l[i - 1], bins=500, edgecolor='black')
		axs[i - 1].set_title(title_use, fontsize=7)
		axs[i - 1].set_xlabel("Number of times a word occur in a training datapoint", fontsize=7)
		axs[i - 1].set_ylabel("Number of times that word is generated", fontsize=7)
		axs[i - 1].text(0.1, 0.9, text_on_hist, transform=axs[i - 1].transAxes, fontsize=7, color="black")
		axs[i - 1].text(0.1, 0.86, text_k_5, transform=axs[i - 1].transAxes, fontsize=7, color="black")
		axs[i - 1].text(0.1, 0.82, text_k_10, transform=axs[i - 1].transAxes, fontsize=7, color="black")

	# Adjust layout for better spacing
	plt.tight_layout()
	plt.show()

def med_1_split_sample(file):

	with open(file, 'r', encoding='utf-8') as file:
		content = file.read()

	data_line = []
	split_string = re.split(r'[ .,!?#\-\n]+', content)
	for word in split_string:

		word = word.lower()
		word = re.sub(r'[!@;#$°%^&<*}~>•+●²=()/":…-]+', '', word)
		word = word.replace("'", "")
		word = word.replace("[", "")
		word = word.replace("]", "")
		words = [word]
		data_line.extend(words)

	return data_line

def med_2_split_sample(file):

	with open(file, 'r', encoding='utf-8') as file:
		content = file.read()
	words = word_tokenize(content)
	actual_words = []
	for i in words:
		actual_words.append(i.lower())

	return actual_words

def get_all_files(directory):

	file_list = []
	for root, _, files in os.walk(directory):
		for file in files:
			file_path = os.path.join(root, file)
			file_list.append(file_path)
	return file_list

def perform_test(files, hashmap, met):
	if met == 2: nltk.download('punkt')
	counter = []
	not_founded = 0
	k_below_5 = 0
	k_below_10 = 0
	for i in files:
		if met == 1:
			word_list = med_1_split_sample(i)
		if met == 2:
			word_list = med_2_split_sample(i)
		if met == 3:
			pass

		for i in word_list:
			try:
				k_eid_mem = hashmap[i]
				counter.append(k_eid_mem)

				#Count every time k is lower than 5 or 10
				if k_eid_mem <= 5: k_below_5 += 1
				if k_eid_mem <= 10: k_below_10 += 1

			except:
				not_founded += 1
				pass

	return counter, not_founded, k_below_5, k_below_10