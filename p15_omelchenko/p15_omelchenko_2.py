card_number = ('A', *range(2, 10), 'J', 'Q', 'K')
card_suit = ('diamonds', 'clubs', 'hearts', 'spades')
def card_shuffle():
    for x in card_number:
        for y in card_suit:
            yield(str(x) + " " + y)
card_generator = card_shuffle()
while(True):
    print(next(card_generator))