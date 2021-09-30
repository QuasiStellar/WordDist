words = []
with open("word_rus.txt", encoding="utf-8") as file:
    for line in file:
        words.append(line[:-1])
print(len(words))
graph = []


def close(w1, w2):
    if abs(len(w1) - len(w2)) > 1:
        return False
    if len(w1) == len(w2):
        dist = 0
        for ch in range(len(w1)):
            if w1[ch] != w2[ch]:
                dist += 1
                if dist > 1:
                    return False
        return True
    if len(w1) > len(w2):
        if w1[1:] == w2 or w1[:-1] == w2:
            return True
        return False
    else:
        if w2[1:] == w1 or w2[:-1] == w1:
            return True
        return False


for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if close(words[i], words[j]):
            graph.append((words[i], words[j]))

print(graph)
