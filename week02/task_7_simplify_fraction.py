from fractions import *


def simplify_fraction(fraction):

    fracted_number = Fraction(fraction[0], fraction[1])
    return (fracted_number.numerator, fracted_number.denominator)
