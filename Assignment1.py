class Employee:
    def __init__(self):
        self.permanent = input("Is the employee permanent? (Y/N)")
        self.no_of_delivery = int(input("Enter the number of packages delivered: "))
        self.distance = int(input("Enter the distance traveled: "))
        self.shift = input("Did the employee work the night shift? (Y/N)")
        self.grade = input("Enter the employee's grade (A1, A2, A3): ")
    def calculate_basic_pay(self):
        if self.permanent == 'Y':
            basicsal = 5000
            basic_pay = basicsal + (self.no_of_delivery * 50) + (self.distance * 75)
            if self.shift == 'Y':
                basic_pay += (basic_pay * 0.1)
        elif self.permanent == 'N':
            basicsal = 3000
            basic_pay = basicsal + (self.no_of_delivery * 30) + (self.distance * 65)
            if self.shift == 'Y':
                basic_pay += (basic_pay * 0.1)
        return basic_pay
    
    def bonus(self):
        if self.grade == 'A1':
            bonus = (self.calculate_basic_pay() * 0.05)
        elif self.grade == 'A2':
            bonus = (self.calculate_basic_pay() * 0.1)
        elif self.grade == 'A3':
            bonus = (self.calculate_basic_pay() * 0.15)
        return bonus
    
    def calculate_net_pay(self):
        return self.calculate_basic_pay() + self.calculate_bonus()
    
    def display_pay_details(self):
        num=self.calculate_basic_pay()
        print("Basic Pay:",num)
        print("Bonus:",self.calculate_bonus())
        print("Net Pay:",self.calculate_net_pay())

# Employee Inputs
employee = Employee()
employee.display_pay_details()

