# Вывести последнюю букву в слове
word = 'Архангельск'

print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'

print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'

vovels = 'ауоиэыяюеё'
vovels_count = 0
for letter in word.lower():
    vovels_count += 1 if letter in vovels else 0

print(vovels_count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'

print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'

words = sentence.split()
word_lengths = map(len, words)

print(sum(word_lengths) / len(words))
