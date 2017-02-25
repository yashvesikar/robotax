class employee(object):
    def __init__(self, payType, pay, averageOutput, payrollTax, annualCost):
        if payType.lower() == 'salary':
            self.salary = pay
            self.hourlyRate = 0.0
        else:
            self.hourlyRate = pay
            self.salary = 0.0
        self.averageOutput = averageOutput
        self.payrollTax = payrollTax
        self.annualCost = annualCost
