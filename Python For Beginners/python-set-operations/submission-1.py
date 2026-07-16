from typing import List

def count_unique_words(words: List[str]) -> int:
    if words:
        new_set = set(words)
        n = len(new_set)
        return n
    return 0

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
