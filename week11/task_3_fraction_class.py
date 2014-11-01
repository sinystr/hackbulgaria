class Fraction():

    def gcd(a, b):
        while b != 0:
            (a, b) = (b, a % b)
        return a

    def simplify(self):
        while Fraction.gcd(self.num, self.denom) > 1:
            gcd = Fraction.gcd(self.num, self.denom)
            self.num /= gcd
            self.denom /= gcd
        self.num, self.denom = int(self.num), int(self.denom)

    def __init__(self, num, denom):
        self.num, self.denom = num, denom

    def __add__(self, other):
        return_num = self.num * other.denom + self.denom * other.num
        return_denom = self.denom * other.denom
        return_fraction = Fraction(return_num, return_denom)
        return_fraction.simplify()
        return return_fraction

    def __truediv__(self, other):
        return_num = self.num * other.denom
        return_denom = self.denom * other.num
        return_fraction = Fraction(return_num, return_denom)
        return_fraction.simplify()
        return return_fraction

    def __sub__(self, other):
        if self.num * other.denom - self.denom * other.num < 1:
            return_num = 0
            return_denom = 1
        else:
            return_num = self.num * other.denom - self.denom * other.num
            return_denom = self.denom * other.denom
        return_fraction = Fraction(return_num, return_denom)
        return_fraction.simplify()
        return return_fraction

    def __lt__(self, other):
        if (self - other).num == 0:
            return True
        return False

    def __gt__(self, other):
        if (other - self).num == 0:
            return True
        return False
