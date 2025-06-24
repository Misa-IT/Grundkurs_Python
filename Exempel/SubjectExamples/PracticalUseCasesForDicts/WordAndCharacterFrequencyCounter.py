# Detta exempel är helt AI-genererat

def count_word_frequency(text):
    """Count the frequency of each word in a text."""
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Initialize an empty dictionary
    word_counts = {}
    
    # Count each word
    for word in words:
        # Remove punctuation (simple approach)
        word = word.strip('.,!?":;()[]{}')
        
        if word:  # Skip empty strings
            # If word exists in dictionary, increment its count
            # Otherwise, add it with a count of 1
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    
    return word_counts

# Example text
sample_text = """
Python is amazing. Python is powerful. Python is versatile.
Programming in Python is fun and efficient. Python has many libraries.
"""

# Count word frequencies
word_frequencies = count_word_frequency(sample_text)

# Display results
print("Word frequencies:")
for word, count in word_frequencies.items():
    print(f"'{word}': {count}")

# Find the most common words
print("\nMost common words:")
most_common = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)
for word, count in most_common[:3]:  # Top 3 words
    print(f"'{word}': {count}")

# Another example: counting character frequencies
def count_char_frequency(text):
    """Count the frequency of each character in a text."""
    char_counts = {}
    
    for char in text.lower():
        if char.isalnum():  # Only count alphanumeric characters
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    
    return char_counts

# Count character frequencies
char_frequencies = count_char_frequency(sample_text)

# Display results
print("\nCharacter frequencies:")
for char, count in sorted(char_frequencies.items()):
    print(f"'{char}': {count}")