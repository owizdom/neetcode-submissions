from typing import List

def read_integers() -> List[int]:
    line = input()
    parts = line.split(",")
    result = []
    for part in parts:
        result.append(int(part))
    return result
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
