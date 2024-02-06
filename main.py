import string

text = input("Введите текст: ")
text = text.lower()
punctuation = string.punctuation
for symbol in punctuation:
    text = text.replace(symbol, ' ')

words = text.split()
print(words)
unique_words = set(words)
words_len = len(unique_words)
print(f'Количество разных слов: {words_len}')
word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Частота слов:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")