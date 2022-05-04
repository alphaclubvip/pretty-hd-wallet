def get_start(raw):
    same = None
    char = None
    text = ''

    for key, c in enumerate(raw):
        i = int(c, 16)

        if key == 0:
            char = i
            text = c
        elif key == 1:
            if i == char:
                same = 0
                text += c
            elif char + 1 == i:
                same = 1
                char = i
                text += c
            elif char - 1 == i:
                same = -1
                char = i
                text += c
            else:
                return text.upper()
        else:
            if same == 0 and char == i:
                text += c
            elif same == 1 and char + 1 == i:
                char = i
                text += c
            elif same == -1 and char - 1 == i:
                char = i
                text += c
            else:
                return text.upper()

    return text.upper()


def get_end(raw):
    raw = raw[::-1]
    same = None
    char = None
    text = ''

    for key, c in enumerate(raw):
        i = int(c, 16)

        if key == 0:
            char = i
            text = c
        elif key == 1:
            if i == char:
                same = 0
                text += c
            elif char + 1 == i:
                same = -1
                char = i
                text += c
            elif char - 1 == i:
                same = 1
                char = i
                text += c
            else:
                return text[::-1].upper()
        else:
            if same == 0 and char == i:
                text += c
            elif same == 1 and char - 1 == i:
                char = i
                text += c
            elif same == -1 and char + 1 == i:
                char = i
                text += c
            else:
                return text[::-1].upper()

    return text[::-1].upper()
