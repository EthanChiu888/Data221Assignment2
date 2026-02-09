import string

with open("sample-file", "r") as file: # Opens the file in read mode
    content = file.read().lower() # Reads the entire file and converts all text to lowercase

tokens = content.split() # splits the text into raw tokens based on whitespace

clean_tokens = []
# Loops through each token
for word in tokens:
    clean_word = word.strip(string.punctuation) # Removes punctuation from the beginning and end of the word
    # Keeps only words that contain at least two alphabetic characters
    if sum(char.isalpha() for char in clean_word) >= 2:
        clean_tokens.append(clean_word)
# This list stores bigrams
bigrams = []
# Create bigrams by pairing consecutive cleaned tokens
for i in range(len(clean_tokens) - 1):
    bigrams.append(clean_tokens[i] + " " + clean_tokens[i + 1])
# Dictionary that counts the frequency of each bigram
bigram_counts = {}
# Count how many times each bigram appears
for bigram in bigrams:
    if bigram in bigram_counts:
        bigram_counts[bigram] += 1
    else:
        bigram_counts[bigram] = 1
# Sort bigrams by frequency in descending order and keep the top 5
top_5 = sorted(bigram_counts.items(), key=lambda x: x[1], reverse=True)[:5]

for bigram, count in top_5:
    print(f"{bigram} -> {count}") # Prints the top 5 bigrams
