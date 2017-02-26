from classes.automation import Automation
from classes.employee import Employee

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
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

    return render_template('index.html')

#@app.route('/',methods=['POST'])
#def main():
    # read the posted values from the UI
    # _name = request.form['inputName']
    # _email = request.form['inputEmail']
    # _password = request.form['inputPassword']

if __name__ == "__main__":
    app.run()
