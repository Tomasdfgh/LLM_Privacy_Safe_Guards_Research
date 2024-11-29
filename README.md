![image](https://github.com/user-attachments/assets/9da78a71-b992-471d-8c3b-d345aca7b50a)

<div align="center">

# Engineering Science Machine Intelligence Thesis

</div>

This research project is still ongoing. The repository will continually be updated as the work progresses. The primary focus of this project is to investigate the privacy vulnerabilities of large language models (LLMs), particularly their potential to memorize and expose private training data. By exploring methods such as black-box and white-box attacks, the research aims to identify conditions under which private data can be retrieved and to propose safeguards to prevent such breaches. This repository includes the code, datasets, and experimental results used in analyzing LLM memorization and privacy risks, serving as a living document of the research journey.

## Training Data Distribution

The graphs below show the training data distribution for all three methods that was used to split the data set into its k-eidetic memories. The x axis of each subplot shows the number of times a word appear in a training data point, which means that the left leaning datum on the x axis are words that does not appear frequently within a dataset. The Frequency of each subplot (the y axis) shows how common are words that appear in x amount of times in the training data are. From this graph, it becomes obvious there is a large amount of words that appear only once or twice within the dataset. While it is guaranteed that there are some amount of noise within the split from words being split incorrectly, the amount of words that appear in only a small subset of the training data point is concerning as it could means the methods that I am splitting the words are incorrect. To validate the methods that I am using, I have found the Zipf curve for each method. The results of which are displayed in the next section. 

<div align="center">
  <img src="https://github.com/user-attachments/assets/856e6a19-b3b8-4df5-be9f-4a2871aa6316" alt="All Split Method Distribution" width="950">
  <p><em>Figure 1: Distribution of training data across the three data splits methods: Hard Coded Simple Split, NLTK Vanilla Encoder, and Deep Semantics Splitting.</em></p>
</div>

## Zipf Curve

The Zipf curve, named after linguist George Zipf, is a graphical representation of the frequency distribution of words in a given language or dataset. It reflects Zipf's Law, which states that the frequency of a word is inversely proportional to its rank in the frequency table, meaning the most common word occurs much more frequently than the second most common word, and so on. When plotted on a log-log scale, the Zipf curve typically appears as a straight line, indicating a power-law relationship. This phenomenon highlights the skewed nature of linguistic usage, where a small subset of words dominates communication while the majority are rarely used. The 3 curves below are not a straight line, yet they closely follow a power-law distribution, indicating that the frequency of words still generally decreases as their rank increases, though with slight deviations which can most likely be attributed to the noise from the method of splitting. One thing to note is that the closer it is to being a straight line shows the more accurate it is, and the simple split is the farthest followed by the vanilla tokenizer. The third method is showing the distribution of only the first 15 percent of the training data as it is still being generated.

<div align="center">
<img src="https://github.com/user-attachments/assets/40e33d22-ac6d-4d7e-ad7c-75b30fe37a6c" alt="All Split Method Distribution" width="300">
  <p><em>Figure 2: Zipf curve across the three data splits methods: Hard Coded Simple Split, NLTK Vanilla Encoder, and Deep Semantics Splitting.</em></p>
</div>

## Memorization Test

The memorization test shows that the percentage of generated words from GPT2 that appear in 5 or 10 of the training data points is less than 1 percent. This shows that memorization does indeed occur but only at a minimal amount. These tests were done on only a subset of the data as not all data have been generated yet. More will follow soon as the research progresses.

<div align="center">
  <img src="https://github.com/user-attachments/assets/189c7c77-2020-468c-a5eb-8e0c6cb4da4a" alt="Method 1 and 2 Result" width="750">
  <p><em>Figure 3: Results of the memorization test using Method 1 and Method 2.</em></p>
</div>
