

TERMINAL = None


def extend_trie_with_word(trie, word, terminal=TERMINAL):
    curr = trie
    for char in word:
        if char not in curr:
            curr[char] = {}
        curr = curr[char]
    curr[terminal] = terminal


def trie_contains_word(trie, word, terminal=TERMINAL):
    """
    Advance through the trie until all characters in the word are consumed.
    """
    curr = trie
    for char in word:
        if char not in curr:
            return False
        curr = curr[char]
    return terminal in curr
