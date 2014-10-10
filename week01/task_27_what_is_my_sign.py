def what_is_my_sign(day, month):
    # We validate the day and month
    if day < 0 or day > 31:
        return "There's no such day!"

    if month < 0 or month > 12:
        return "There's no such month!"

    def January():
        if day <= 20:
            return "Capricorn"
        return "Aquarius"

    def February():
        if day <= 19:
            return "Aquarius"
        return "Pisces"

    def March():
        if day <= 20:
            return "Pisces"
        return "Aries"

    def April():
        if day <= 20:
            return "Aries"
        return "Taurus"

    def May():
        if day <= 21:
            return "Taurus"
        return "Gemini"

    def June():
        if day <= 21:
            return "Gemini"
        return "Cancer"

    def July():
        if day <= 22:
            return "Cancer"
        return "Leo"

    def August():
        if day <= 22:
            return "Leo"
        return "Virgo"

    def September():
        if day <= 23:
            return "Virgo"
        return "Libra"

    def October():
        if day <= 23:
            return "Libra"
        return "Scorpio"

    def November():
        if day <= 22:
            return "Scorpio"
        return "Sagittarius"

    def December():
        if day <= 21:
            return "Sagittarius"
        return "Capricorn"

    months = {
        1: January,
        2: February,
        3: March,
        4: April,
        5: May,
        6: June,
        7: July,
        8: August,
        9: September,
        10: October,
        11: November,
        12: December
    }

    return months[month]()
