n = int(input())
word = str(input())

split_word = []
for i in range(len(word)):
    w = word[i].split(' ')
    split_word.append(w)

answer = []
for word in split_word:
    answer.append(int(*word))
print(sum(answer))