import datetime

def junior_calculation(employeeId, employeePosition, employeeSalary, employeeStartDate):
    numberofWorkedDay = (datetime.datetime.now() - datetime.datetime.strptime(employeeStartDate, '%Y-%m-%d')).days
    if numberofWorkedDay < 60:
            return 0
    else:
            return  float(employeeSalary)/365*numberofWorkedDay
def calculate_money(employeeId, employeePosition, employeeSalary, employeeStartDate):
    money = 0
    
    if employeePosition == "Junior":
        money = junior_calculation(employeeId, employeePosition, employeeSalary, employeeStartDate)
    elif employeePosition == "Senior":
        money = junior_calculation(employeeId, employeePosition, employeeSalary, employeeStartDate)*3
    elif employeePosition == "Manager":
        money = junior_calculation(employeeId, employeePosition, employeeSalary, employeeStartDate)*5 +(float(employeeSalary)*0.5)
    return money