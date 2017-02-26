# <<<<<<< Updated upstream
# class Employee(object):
#     def __init__(self, payType, pay, annualHours, payrollTax, annualCost):
#         if payType.lower() == 'salary':
#             self.salary = pay
#             self.hourlyRate = 0.0
#         else:
#             self.hourlyRate = pay
#             self.annualHours = annualHours
#             self.salary = 0.0
#         self.payrollTax = payrollTax
#         self.annualCost = annualCost
# =======
import math
class Employee(object):
    def __init__(self,tax,wage,productivity,NumberOfEmployees,status):
        self.tax = tax
        self.wage = wage
        self.productivity = productivity
        self.status = status
        self.NumberOfEmployees = int(NumberOfEmployees)
    def Wage(self):
        return int(self.wage)

    def Tax(self):
        return int(self.tax)

    def Production(self):
        return int(self.productivity)

    def Status(self):
        return self.status

    def NumberOfEmployees(self):
        return self.NumberOfEmployees

    # def __str__(self):
    #     return "Employee salary: {} , Employee Productivity: {}".format(self.salary,self.productivity)
