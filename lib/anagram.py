class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word.lower())

    def match(self, possible_matches):
        return [w for w in possible_matches if sorted(w.lower())
               == self.sorted_word and w.lower() != self.word.lower()]
