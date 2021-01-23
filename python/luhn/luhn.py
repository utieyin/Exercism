class Luhn:
    def __init__(self, card_num):
        self.card_number = [card for card in card_num.replace(" ", "")]

    def valid(self):
        if len(self.card_number) > 1:
            for number in self.card_number:
                if not number.isnumeric():
                    return False
            cards = [int(x) for x in self.card_number]
            a = 2
            while a <= len(cards):
                pos = len(cards) - a
                cards[pos] = (cards[pos] * 2) - 9 if cards[pos] * 2 > 9 else cards[pos] * 2
                a += 2
            return True if sum(cards) % 10 == 0 else False
        return False