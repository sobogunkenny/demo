# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def __init__(self, word, anagram):
    self.word = word
    self.anagram = anagram
    
def find_anagrams(word, anagram):
    sorted_word = sorted(word)
    sorted_anagram = sorted(anagram)
    if sorted_word == sorted_anagram:
        return True
    else:
        return False

