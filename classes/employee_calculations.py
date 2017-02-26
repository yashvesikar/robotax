import calculations_template

class employee_calculations(calculations):
    def __init__(self, array_of_employees):
        self.employees = array_of_employees

    def sum():
        employee_tax_sum = 0
        for employee in self.employees:
            employee_tax_sum += employee.payrollTax
        return employee_tax_sum

    def productivity():
        employee_productivity = self.averageOutput * len(array_of_employees)
        return employee_productivity
        # for employee in self.employees:
        #     employee_productivity+=
        # employee_productivity = employee_productivity/len(array_of_employees)


    # def get_salary():
    #     return self.salary
    #
    #     self.hourlyRate = hourlyRate
    #     self.averageOutput = averageOutput
    #     self.position = position
    #     self.payrollTax = payrollTax
    #     self.annualCost = annualCost
    #
    # def get_hourlyRate():
    #     return self.hourlyRate
    #
    # def get_averageOutput():
    #     return self.averageOutput
    #
    # def get_position():
    #     return self.position
    #
    # def get_payrollTax():
    #     return self.payrollTax
    #
    # def get_annualCost():
    #     return self.annualCost
