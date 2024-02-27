import json

# Load the word list
with open('altogether.txt', 'r') as f:
    words_list = f.read().splitlines()

# Load the JSON file
with open('output.json', 'r') as f:
    data = json.load(f)

# Calculate frequencies
word_freq = {}
for word in words_list:
    if word in data:
        freq = data[word]
        if freq == 1:
            freq *= 6
        else:
            freq = min(freq * 4.22, 75)
    else:
        freq = 5
    word_freq[word] = freq

# Export results to finn.txt
output_path = '../fasctrendz.github.io/finn.txt'
with open(output_path, 'w') as f:
    for word, freq in word_freq.items():
        f.write(f"{word.upper()};{freq}\n")

print(f"Output saved to: {output_path}")
