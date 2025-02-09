import re
from collections import Counter
import pytest

def read_file(filename):
    """Read content from a text file.
    
    Parameters:
        filename: str - The path to the text file
    Returns:
        str - The content of the file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return ""

def process_text(text):
    """Process text by converting to lowercase and removing special characters.
    
    Parameters:
        text: str - The input text to process
    Returns:
        list - List of processed words
    """
    # Convert to lowercase and split into words
    words = text.lower()
    # Remove special characters and numbers
    words = re.sub(r'[^a-z\s]', '', words)
    return words.split()

def count_words(words):
    """Count frequency of each word in the list.
    
    Parameters:
        words: list - List of words to count
    Returns:
        Counter - Dictionary-like object with word frequencies
    """
    return Counter(words)

def display_results(word_counts, top_n=10):
    """Display the top N most frequent words.
    
    Parameters:
        word_counts: Counter - Counter object with word frequencies
        top_n: int - Number of top words to display
    """
    print(f"\nTop {top_n} most frequent words:")
    for word, count in word_counts.most_common(top_n):
        print(f"{word}: {count}")

def main():
    filename = input("Enter the path to your text file: ")
    text = read_file(filename)
    if text:
        words = process_text(text)
        word_counts = count_words(words)
        display_results(word_counts)

# Test functions
def test_process_text():
    text = "Hello, World! This is a test."
    result = process_text(text)
    assert "hello" in result
    assert "world" in result
    assert "test" in result
    assert len(result) == 5

def test_count_words():
    words = ["hello", "world", "hello", "test"]
    result = count_words(words)
    assert result["hello"] == 2
    assert result["world"] == 1
    assert result["test"] == 1

if __name__ == "__main__":
    main()