import pygtrie
import networkx

ALPHABET = "alphabet_rus.txt"
WORD_LIST = "word_rus.txt"

with open(ALPHABET, encoding="utf-8") as file:
    alphabet = {char: pos for pos, char in enumerate(file.read())}

words = pygtrie.CharTrie()
with open(WORD_LIST, encoding="utf-8") as file:
    for word in file:
        words[word[:-1] + "!"] = True

graph = []


def neighbours(string):
    strings = set()
    for i in range(len(string) - 1):
        for letter in alphabet:
            strings.add(string[:i] + letter + string[i:])
            if alphabet[letter] > alphabet[string[i]]:
                strings.add(string[:i] + letter + string[i + 1:])
    for letter in alphabet:
        strings.add(string[:-1] + letter + '!')
    return strings


for word in words:
    for neighbour in neighbours(word):
        if words.has_node(neighbour):
            graph.append((word[:-1], neighbour[:-1]))

G = networkx.Graph()
G.add_edges_from(graph)
print([p for p in networkx.all_shortest_paths(G,source='кот',target='ель')])

with open('graph.txt', 'w', encoding="utf-8") as file:
    for edge in graph:
        file.write(edge[0] + ' ' + edge[1] + '\n')
