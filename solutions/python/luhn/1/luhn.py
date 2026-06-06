class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        string_card = str(self.card_num).replace(" ", "")
        
        if len(string_card) <= 1 or not string_card.isdigit():
            return False

        digits = [int(char) for char in string_card]

        for i in range(len(digits) - 2, -1, -2):
            temp = digits[i] * 2
            if temp > 9:
                temp -= 9
            digits[i] = temp

        return sum(digits) % 10 == 0