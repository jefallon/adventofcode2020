def read_decks(infile):
    deck_1 = []
    deck_2 = []
    with open(infile, 'r') as f:
        for row in f:
            card = row.strip()
            if card == 'Player 1:':
                deck = deck_1
            elif card == 'Player 2:':
                deck = deck_2
            elif card != '':
                deck.append(int(card))
    return deck_1,deck_2

def play_game(deck_1, deck_2):
    seen_decks = set()
    while True:
        if (tuple(deck_1),tuple(deck_2)) in seen_decks:
            return 1, deck_1
        else:
            seen_decks.add((tuple(deck_1),tuple(deck_2)))
            card_1 = deck_1.pop(0)
            card_2 = deck_2.pop(0)
            if card_1 <= len(deck_1) and card_2 <= len(deck_2):
                winner = play_game(deck_1[:card_1], deck_2[:card_2])[0]
                if winner == 1:
                    deck_1.extend([card_1, card_2])
                    if len(deck_2) == 0:
                        return 1, deck_1
                else:
                    deck_2.extend([card_2, card_1])
                    if len(deck_1) == 0:
                        return 2, deck_2

            elif card_1 > card_2:
                deck_1.extend([card_1,card_2])
                if len(deck_2) == 0:
                    return 1, deck_1
            else:
                deck_2.extend([card_2, card_1])
                if len(deck_1) == 0:
                    return 2, deck_2

def get_score(deck):
    score = sum([(idx+1)*y for idx, y in enumerate(deck[::-1])])
    return score

if __name__ == '__main__':
    infile = 'Advent22.txt'
    deck_1, deck_2 = read_decks(infile)
    winning_deck = play_game(deck_1, deck_2)[1]
    print(get_score(winning_deck))
