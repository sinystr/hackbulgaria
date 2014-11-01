class CashDesk:
    def f(self, l, s):
        return s == 0 or l != [] and (self.f(l[1:], s) or self.f(l[1:], s - l[0]))

    def __init__(self, money={100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}):
        self.money = money

    def take_money(self, take_money):
        for key in take_money:
            self.money[key] += take_money[key]

    def total(self):
        sum = 0
        for key in self.money:
            sum += key * self.money[key]
        return sum

    def can_withdraw_money(self, money_sum):
        l = []
        for i in self.money:
            for k in range(0, self.money[i]):
                l.append(i)
        return(self.f(l, money_sum))
