# Завдання 1
def popularity(text: str = ''):
    words = {}
    text = text.lower().strip('\n').split()
    for word in text:
        if word not in words.keys():
            words[word] = 1
        else:
            words[word] += 1
    sorted_words = sorted(words.items(), key=lambda x: (-x[1], x[0]))
    return [key for key, _ in sorted_words]


# print(popularity('apple kiwi pineapple kiwi apple kiwi'))
# print(popularity('aPPle pine Apple kiwi Apple kiwi'))
# print(popularity('aPPle pine Apple kiwi Apple kiwi'))
# print(popularity('aab aaa aac aab aac aaa x'))
