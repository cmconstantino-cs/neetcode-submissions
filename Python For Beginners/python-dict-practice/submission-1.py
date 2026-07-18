from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    m_dict = {}
    m_list = []
    for c in word:
        m_list.append(c)
    m_dict = {c:m_list.count(c) for c in word}
    return m_dict

# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
