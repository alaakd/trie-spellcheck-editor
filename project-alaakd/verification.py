# verify the trie

from trie import Trie


trie: Trie = Trie()

mode = ""
while mode not in ("lookup", "spell check", "suggest"):
    print('modes are: "lookup", "spell check", "suggest"')
    mode = input("mode> ")


match mode:
    case "lookup":
        while True:
            word = input("word> ")
            if word in trie:
                print(f"{word} is a lexicon word.")
            else:
                print(f"{word} is NOT a lexicon word.")
    case "spell check":
        while True:
            sentence = input("sentence> ")
            for start, end in trie.spell_check(sentence):
                print(f"spelling error: {sentence[start:end+1]} at {(start, end)}")
    case "suggest":
        while True:
            prefix = input("prefix> ")
            limit = int(input("limit> "))
            print(f"suggestions: {', '.join(trie.suggestions(prefix, limit))}")



