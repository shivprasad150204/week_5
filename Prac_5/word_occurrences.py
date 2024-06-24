"""
Word Occurrence Counter

"""

def main():
    text = input("Text: ")
    word_counts = count_words(text)
    max_length = max(len(word) for word in word_counts)
    for word in sorted(word_counts):
        print(f"{word:{max_length}} : {word_counts[word]}")

def count_words(text):
    word_counts = {}
    words = text.split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

if __name__ == "__main__":
    main()
