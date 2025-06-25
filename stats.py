def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    words = text.split()
    counter = {}
    for w in words:
        for l in w:
            #print(l)
            new_l = l.lower()
            if new_l in counter:
                counter[new_l] += 1
            else:
                counter[new_l] = 1
    return counter
