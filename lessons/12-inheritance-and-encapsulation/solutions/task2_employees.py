class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_pay(self):
        return self.salary / 12


class Manager(Employee):
    def __init__(self, name, salary, annual_bonus):
        super().__init__(name, salary)
        self.annual_bonus = annual_bonus

    def monthly_pay(self):
        # Start with the normal pay calculation, then add the bonus
        return super().monthly_pay() + self.annual_bonus / 12


staff = [
    Employee("Alan", 36_000),
    Manager("Grace", 54_000, 6_000),
    Employee("Tim", 30_000),
]
for person in staff:
    print(f"{person.name}: £{person.monthly_pay():,.2f} per month")
