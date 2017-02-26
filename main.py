from classes.automation import Automation
from classes.employee import Employee

#Initialize empty list of objects
array_of_employees = []
array_of_automations = []

#Mock employee data
employeeDummy = {'Employee1': [30000,100,False],
                 'Employee2':[30000,100,False],
                 'Employee3':[30000,100,False],
                 'Employee4':[30000,100,False],
                 'Employee5':[30000,100,False],
                 'Employee6':[30000,100,False],
                 'Technnician1': [37000,0,True]
}

#Mock automation data
automationDummy = {'Automotan1' :[150],
                   'Automotan2' :[150],
                   'Automotan3' :[150],
                   'Automotan4' :[150]}

#Populate Employee Array
for key,val in employeeDummy.items():
    array_of_employees.append(Employee(val[0],val[1],val[2]))
#Populate Automation array
for key,val in automationDummy.items():
    array_of_automations.append(Automation(val[0]))




def __main__():

    tax_rate = 0.1

    #Employee data
    total_salary = sum(emp.Salary() for emp in array_of_employees if emp.Status() == False)
    total_production = sum(emp.Production() for emp in array_of_employees if emp.Status() == False)

    #Left hand side of equation, employee side
    lhs = (total_salary * tax_rate) / total_production

    #Robot data
    robots_added = len(array_of_automations)
    robots_production = sum(automation.Production() for automation in array_of_automations)
    #Technician data/new employee data
    technicians_tax = sum(emp.Salary() for emp in array_of_employees if emp.Status() == True)* tax_rate


    robot_tax = (lhs*robots_production) - technicians_tax

    print("Robot Tax: ", robot_tax)

    print("Per robot tax: ", robot_tax/robots_added)
__main__()
