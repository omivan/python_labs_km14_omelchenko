card_number = ('A', *range(2, 10), 'J', 'Q', 'K')
card_suit = ('diamonds', 'clubs', 'hearts', 'spades')
def card_shuffle():
    for x in card_suit:
        for y in card_number:
            yield(str(y) + " " + x)
card_generator = card_shuffle()
while(True):
    print(next(card_generator))