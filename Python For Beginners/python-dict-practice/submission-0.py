from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    m_dict = {}
    m_list = []
    for character in word:
        m_list.append(character)
    m_dict = {character:m_list.count(character) for character in word}
    return m_dict



# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
