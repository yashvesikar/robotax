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
    def __init__(self, salary,productivity,status):
        self.salary = salary
        self.productivity = productivity
        self.status = status

    def Salary(self):
        return self.salary

    def Production(self):
        return self.productivity

    def Status(self):
        return self.status

    def __str__(self):
        return "Employee salary: {} , Employee Productivity: {}".format(self.salary,self.productivity)
