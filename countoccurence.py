
def count_word_occurrences(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Example usage:
sentence = input("Enter a sentence: ")
result = count_word_occurrences(sentence)
print(result)
