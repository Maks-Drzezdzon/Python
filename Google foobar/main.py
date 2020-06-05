

from collections import Counter


def foobar1(x):
    d = {
        'z': 'a', 'y': 'b', 'x': 'c',
        'w': 'd', 'v': 'e', 'u': 'f',
        't': 'g', 's': 'h', 'r': 'i',
        'q': 'j', 'p': 'k', 'o': 'l',
        'n': 'm', 'm': 'n', 'l': 'o',
        'k': 'p', 'j': 'q', 'i': 'r',
        'h': 's', 'g': 't', 'f': 'u',
        'e': 'v', 'd': 'w', 'c': 'x',
        'b': 'y', 'a': 'z'
    }

# x = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
# y = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
    a = ""
    for letter in y:
        if letter in d:
            a = a + letter.replace(letter, d[letter])
        else:
            a = a + letter

    return a.strip(" ")


def foobar2(s):
    # Your code here
    a = "".join([letter for letter in s if letter is not '-']
                ).lstrip("<").rstrip(">")
    counter = 0

    left_stack = a.copy()
    right_stack = []

    while left_stack:
        f = left_stack.pop(0)
        right_stack.append(f)

        if f == '>':
            for letter in left_stack:
                if f != letter:
                    counter += 1
        elif f == '<':
            for letter in right_stack:
                if f != letter:
                    counter += 1
    return counter


a = "--->-><-><-->-"
print(foobar2(">><><>"))  # 10
print(foobar2("<<>><"))  # 4
print(foobar2(">----<"))  # 2
