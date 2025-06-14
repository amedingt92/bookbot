import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    # ✅ 1. Check for proper CLI usage
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with error code

    # ✅ 2. Use the CLI argument as the file path
    path_to_book = sys.argv[1]

    # ✅ 3. Read and analyze the book
    book_text = get_book_text(path_to_book)
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")

    char_counts = get_char_counts(book_text)
    sorted_chars = sort_char_counts(char_counts)

    # ✅ 4. Print sorted character frequencies
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

if __name__ == "__main__":
    main()
