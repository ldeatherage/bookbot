from collections import Counter
import string

def count_words(text):
    """
    Returns the number of words in the given text.
    """
    words = text.split()  # Splitting the text into words using whitespace
    return len(words)

def count_characters(text):
    """
    Counts the occurrences of each alphabetic character in the given text.
    Converts all characters to lowercase to avoid duplicates.
    
    :param text: The input string (book text).
    :return: A dictionary with character frequencies (only alphabetic characters).
    """
    text = text.lower()  # Convert all characters to lowercase
    char_counts = Counter(c for c in text if c in string.ascii_lowercase)  # Filter only letters
    return dict(char_counts)  # Convert Counter to dictionary

def generate_report(text):
    """
    Generates and prints a report showing word count and letter frequencies.
    """
    word_count = count_words(text)
    char_count_result = count_characters(text)

    print("\n==== Book Report ====")
    print(f"Total words: {word_count}\n")
    print("Character Frequency (A-Z only):")
    for char, count in sorted(char_count_result.items()):
        print(f"'{char}': {count}")

def main():
    try:
        with open("books/frankenstein.txt", "r") as f:
            file_contents = f.read()
        
        # Generate and print report
        generate_report(file_contents)

    except FileNotFoundError:
        print("Error: The file 'frankenstein.txt' was not found.")

main()