n = int(input())
words = [input() for _ in range(n)]

for word in words:
    if word[::-1] in words:
        len_word=len(word)
        mid=len_word//2
        print(len_word, word[mid])
        break