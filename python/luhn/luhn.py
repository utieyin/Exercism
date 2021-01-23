class Luhn:
    def __init__(self, card_num):
        self.card_number = card_num.replace(" ", "")

    def valid(self):
        if not self.card_number.isdigit():
            return False
        if len(self.card_number) > 1:
            cards = [int(x) for x in self.card_number]
            even = 2
            while even <= len(cards):
                pos = len(cards) - even
                cards[pos] = (cards[pos] * 2) - 9 if cards[pos] * 2 > 9 else cards[pos] * 2
                even += 2
            return True if sum(cards) % 10 == 0 else False
        return False