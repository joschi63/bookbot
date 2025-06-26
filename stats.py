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

def sort_on(counters):
    return counters["count"]

def sort_character_dic(counter):
    new_counter = []

    for c in counter:
        if c.isidentifier():
            new_counter.append({"character": c, "count": counter[c]})
    
    new_counter.sort(reverse=True, key=sort_on)

    return new_counter