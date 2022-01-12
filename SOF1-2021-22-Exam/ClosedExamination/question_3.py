from __future__ import annotations


############# DO NOT DELETE THESE LINES OF CODE ######################
KEYPAD = {'0':'', '1':'', '2':'ABC', '3':'DEF', '4':'GHI', '5':'JKL', 
          '6':'MNO', '7':'PQRS', '8':'TUV', '9':'WXYZ'}

################## WRITE YOUR CODE HERE ###########################


def get_words(keys_pressed: str, current: str, words: set[str]):
    """Mutate the set words by adding possible combinations from keys_pressed via recursion.
    
    Args:
        keys_pressed: A string of digits corresponding to keypresses, as in t9_words
        current: The in-progress word as a string
        words: Set of copmleted words
    """
    if not keys_pressed:
        words.add(current)
        return

    letters = KEYPAD[keys_pressed[0]]
    keys_pressed = keys_pressed[1:]

    if not letters:
        get_words(keys_pressed, current, words)
    else:
        for c in letters:
            get_words(keys_pressed, current + c, words)


def t9_words(keysPressed: str) -> set[str]:
    """Return every possible combination of letters from the T9 keypad input.
    
    Args:
        keysPressed: A string of digits corresponding to keypresses.
    
    Returns:
        A set of strings.
    """
    keys_pressed = keysPressed

    words = set()
    current = ''
    get_words(keys_pressed, current, words)
    return words


t9Words = t9_words
