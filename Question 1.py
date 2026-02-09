import string

def word_frequencies(filename):
    counts = {}

    # Read the file
    with open(filename, "r") as file:
        text = file.read()

    # Split into tokens
    tokens = text.split()

    for token in tokens:
        # Convert to lowercase
        token = token.lower()

        # Remove punctuation from beginning and end
        token = token.strip(string.punctuation)

        # Keep tokens with at least two alphabetic characters
        if sum(char.isalpha() for char in token) >= 2:
            counts[token] = counts.get(token, 0) + 1

    # Sort by frequency (descending) and take top 10
    top_10 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]

    # Print results
    for word, count in top_10:
        print(f"{word} -> {count}")


# Run the function
word_frequencies("sample-file")
