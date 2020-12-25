subject_number = 7
card_pub = 12320657
door_pub = 9659666

def transform(val, subj):
    return (val*subj) % 20201227

def get_loops(pub_key):
    val = 1
    loops = 0
    while val != pub_key:
        loops += 1
        val = transform(val, subject_number)
    return loops

def get_both_loops():
    card_loops = get_loops(card_pub)
    door_loops = get_loops(door_pub)
    return card_loops, door_loops

def get_key():
    card_loops, door_loops = get_both_loops()
    val = 1
    while card_loops:
        val = transform(val, door_pub)
        card_loops -= 1
    card_key = val
    val = 1
    while door_loops:
        val = transform(val, card_pub)
        door_loops -= 1
    door_key = val
    return card_key, door_key

if __name__ == '__main__':
    print(get_key())