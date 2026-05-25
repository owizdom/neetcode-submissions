from typing import List

def contains_duplicate(words: List[str]) -> bool:
    backList = []
    for word in words:
        if word in backList:
            return True
        backList.append(word)   # only runs if we didn't return above

    return False   # runs only after the loop finishes — checked EVERY word, no dupes found
#return len(set(words)) != len(words)
# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))