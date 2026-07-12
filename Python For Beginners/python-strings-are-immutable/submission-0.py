def remove_fourth_character(word: str) -> str:
    part_a = word[:3]
    part_b = word[4:]
    new_word = part_a + part_b
    return new_word


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
