class Employee:

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class HourlyEmployee(Employee):

    def __init__(self, name, payment_per_hour):
        super().__init__(name)
        self.payment_per_hour = payment_per_hour

    def weeklyPay(self, hours):
        if hours >= 40:
            return 40 * self.payment_per_hour
        return hours * self.payment_per_hour


class SalariedEmployee(Employee):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def weeklyPay(self, hours):
        if hours > 0:
            return self.salary
        return 0


class Manager(SalariedEmployee):

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def weeklyPay(self, hours):
        if hours > 0:
            return self.salary + self.bonus
        return 0
