import datetime
def checkInput(employeeId, employeePosition, employeeSalary, employeeStartDate):
    isValid = True
    
   #รหัสพนักงงานต้องเป็นตัวเลขไม่เกิน5หลัก
    if len(employeeId)> 5:
        print("Employee ID must be less than 5 characters")
        isValid = False

    #ตําแหน่งงานต้องไม่เป็นค่าว่าง
    if employeePosition == "":
        print("Employee Position cannot be empty")
        isValid = False 
          #ตำแหน่งปัจจุบันเป็นได้แค่ Senior,Junior,Manager
    if employeePosition != "Senior" and employeePosition != "Junior" and employeePosition != "Manager":
        print("Employee Position must be Senior, Junior, or Manager")
        isValid = False
        
    #เงินเดือนต้องเป็นตัวเลขมีค่ามากกว่าศูนย์ และ ทศนิยมสูงสุด 2 ตำแหน่ง
    if employeeSalary == "":
        print("Employee Salary cannot be empty")
        isValid = False
    else:
        try:
            salary = float(employeeSalary)
            if salary <= 0:
                print("Employee Salary must be a positive number")
                isValid = False
            if len(employeeSalary.split('.')[1]) > 2:
                print("Employee Salary must have at most 2 decimal places")
                isValid = False
        except ValueError:
            print("Employee Salary must be a number")
            isValid = False
            
    
    #วันเดือนปีที่เริ่มทำงานต้องก่อนวันที่ปัจจุบันและไม่เป็นค่าว่าง
    if employeeStartDate == "":
        print("Employee Start Date cannot be empty")
        isValid = False
    else:
        try:
            datetime.datetime.strptime(employeeStartDate, '%Y-%m-%d')
        except ValueError:
            print("Employee Start Date must be in the format 'YYYY-MM-DD'")
            isValid = False 

    return isValid
    