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
    def __init__(self,tax,wage,productivity,numberOfEmployees,status):
        self.tax = float(tax)
        self.wage = float(wage)
        self.productivity = float(productivity)
        self.status = status
        self.numberOfEmployees = int(numberOfEmployees)

    def Wage(self):
        return self.wage

    def Tax(self):
        return self.tax

    def Production(self):
        return self.productivity

    def Status(self):
        return self.status

    def NumberOfEmployees(self):
        return self.numberOfEmployees

    # def __str__(self):
    #     return "Employee salary: {} , Employee Productivity: {}".format(self.salary,self.productivity)
