#!/usr/bin/env checkio --domain=py run cipher-map2

# 
# END_DESC

from typing import List

def recall_password(grille: List[str], password: List[str]) -> str:
    # your code here
    return None


if __name__ == '__main__':
    print("Example:")
    print(recall_password(['X...', '..X.', 'X..X', '....'],
 ['itdf', 'gdce', 'aton', 'qrdi']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert recall_password(['X...', '..X.', 'X..X', '....'],
 ['itdf', 'gdce', 'aton', 'qrdi']) == 'icantforgetiddqd'
    assert recall_password(['....', 'X..X', '.X..', '...X'],
 ['xhwc', 'rsqx', 'xqzz', 'fyzr']) == 'rxqrwsfzxqxzhczy'
    print("Coding complete? Click 'Check' to earn cool rewards!")