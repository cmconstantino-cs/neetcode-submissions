def print_string_characters(word1: str, word2: str) -> None:
    length_a = len(word1)
    length_b = len(word2)
    for a in range(length_a):
        print(word1[a])
    for b in range(length_b):
        print(word2[b])

# do not modify below this line
print_string_characters("Hello, World!", "Good Job!")
