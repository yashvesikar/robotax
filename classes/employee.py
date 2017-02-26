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
    def __init__(self,tax,wage,productivity,status):
        self.tax = tax
        self.wage = wage
        self.productivity = productivity
        self.status = status

    def Wage(self):
        return self.wage
        
    def Tax(self):
        return self.tax

    def Production(self):
        return self.productivity

    def Status(self):
        return self.status

    def __str__(self):
        return "Employee salary: {} , Employee Productivity: {}".format(self.salary,self.productivity)
