# Function to count the number of words in a string
def get_num_words(text):
    words = text.split()
    return len(words)

# Function to count occurrences of each character
def get_char_counts(text):
    char_counts = {}
    for char in text.lower():  # Normalize to lowercase
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

# ✅ NEW: Function to sort character counts and return a list of dictionaries
def sort_char_counts(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha():  # Only include alphabetical characters
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)  # Sort from greatest to least
    return sorted_list
