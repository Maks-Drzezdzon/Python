
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
