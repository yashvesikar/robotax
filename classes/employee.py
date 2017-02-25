class Employee(object):
    def __init__(self, payType, pay, annualHours, payrollTax, annualCost):
        if payType.lower() == 'salary':
            self.salary = pay
            self.hourlyRate = 0.0
        else:
            self.hourlyRate = pay
            self.annualHours = annualHours
            self.salary = 0.0
        self.payrollTax = payrollTax
        self.annualCost = annualCost
