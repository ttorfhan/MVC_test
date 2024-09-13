from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QLineEdit,QInputDialog, QPushButton,QVBoxLayout,QMessageBox
from PyQt5.QtGui import QFont
import sys
from controller.inputCheck import checkInput
from controller.csvParser import parseCsv
from controller.calculateMoney import calculate_money

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Severance Pay Calculator')
        self.setGeometry(200,200, 600, 400)  # X, Y, Width, Height
        
        self.setStyleSheet('background-color: #f4f7c9;')
        
        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)
        
        font = QFont()
        font.setFamily("Comic Sans MS")  # กำหนดชนิดของฟอนต์
        font.setPointSize(12)
        #font.setPixelSize(20)
        font.setBold(True)
        
        self.employeeIdInputLabel = QLabel('Enter Employee ID:', self)
        self.employeeIdInputLabel.setFont(font)
        self.employeePositonInputLabel = QLabel('Enter Employee Position:', self)
        self.employeePositonInputLabel.setFont(font)
        self.employeeSalaryInputLabel = QLabel('Enter Employee Salary:', self)
        self.employeeSalaryInputLabel.setFont(font)
        self.employeeStartDateInputLabel = QLabel('Enter Employee Start Date:', self)
        self.employeeStartDateInputLabel.setFont(font)
        
        #add input dialog #boxให้userกรอก
        
        self.employeeIdInput = QLineEdit(self) 
        self.employeeIdInput.setMinimumHeight(35)
    
        self.employeePositionInput = QLineEdit(self)
        self.employeePositionInput.setMinimumHeight(35)
   
        self.employeeSalaryInput = QLineEdit(self)
        self.employeeSalaryInput.setMinimumHeight(35)
      
        self.employeestartDateInput = QLineEdit(self)
        self.employeestartDateInput.setMinimumHeight(35)
        #self.employeestartDateInput.setStyleSheet('font-size: 15px;')
        self.employeeIdInput.setStyleSheet('''
            QLineEdit {
            background-color: #ffffff;
            color: #333333;
            font-size: 13px;
            padding: 10px 20px;
            border-radius: 3px;
            }
        ''')
        self.employeePositionInput.setStyleSheet('''
            QLineEdit {
            background-color: #ffffff;
            color: #333333;
            font-size: 13px;
            padding: 10px 20px;
            border-radius: 3px;
            }
        ''')
        self.employeeSalaryInput.setStyleSheet('''
            QLineEdit {
            background-color: #ffffff;
            color: #333333;
            font-size: 13px;
            padding: 10px 20px;
            border-radius: 3px;
            }
        ''')
        self.employeestartDateInput.setStyleSheet('''
            QLineEdit {
            background-color: #ffffff;
            color: #333333;
            font-size: 13px;
            padding: 10px 20px;
            border-radius: 3px;
            }
        ''')

    
        self.paidEmployeeLabel = QLabel("Paid Employee:")
        self.paidEmployeeLabel.setFont(font)
        self.totalSeverancePayLabel = QLabel("Total Severance Paid:")
        self.totalSeverancePayLabel.setFont(font)
        self.paidEmployeeIDLabel = QLabel("Employee ID Paid:")
        self.paidEmployeeIDLabel.setFont(font)
        
        #ปุ่มกด
        button = QPushButton('Calculate', self)
        button.setFont(font)
        button.setStyleSheet('''
            QPushButton {
            background-color: #e18acf;
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 10px 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            text-align: center;
            }
           QPushButton:hover {
                background-color: #e2a2d5;
            } 
        ''')
        button.clicked.connect(self.on_click) #เมื่อกดปุ่ม ให้เรียกฟังชั่น
        
        self.layout.addWidget(self.employeeIdInputLabel)
        self.layout.addWidget(self.employeeIdInput)
        
        self.layout.addWidget(self.employeePositonInputLabel)
        self.layout.addWidget(self.employeePositionInput)
        
        
        self.layout.addWidget(self.employeeSalaryInputLabel)
        self.layout.addWidget(self.employeeSalaryInput)
        
        
        self.layout.addWidget(self.employeeStartDateInputLabel)
        self.layout.addWidget(self.employeestartDateInput)
        
        self.layout.addWidget(button)
    
        self.layout.addWidget(self.paidEmployeeLabel)
        self.layout.addWidget(self.totalSeverancePayLabel)
        self.layout.addWidget(self.paidEmployeeIDLabel)
        
        self.setLayout(self.layout)
        
        self.paidEmployeeCount = 0
        self.totalSeverancePaid = 0.0
        self.paidEmployeeIDs = set()
            

    def on_click(self): #ฟังชั่นที่เรียกใช้
        #ลองดูว่ากดปุ่มแล้วให้ไปเอาข้อมูลinputที่userใส่มาเก็บในตัวแปรพวกนี้
        employeeId = self.employeeIdInput.text()
        employeePosition = self.employeePositionInput.text()
        employeeSalary = self.employeeSalaryInput.text()
        employeeStartDate = self.employeestartDateInput.text()
        #แล้วลองปริ้นค่าดู
        #print("Employee ID:", employeeId)
        #print("Employee Position:", employeePosition)
        #print("Employee Salary:", employeeSalary)
        #print("Employee Start Date:", employeeStartDate)
        if employeeId in self.paidEmployeeIDs:
            QMessageBox.warning(
                self, "Error", "This employee has already received severance pay"
            )
            return
        isValid = checkInput(employeeId, employeePosition, employeeSalary, employeeStartDate)
        #print("Is Valid:", isValid)
        if isValid:
           money = calculate_money(employeeId, employeePosition, employeeSalary, employeeStartDate)
           #print("Money:", money) 
           if money == 0:
               QMessageBox.information(
                   self, "Severance Pay", "This employee has no severance pay"
               )
               return
           reply = QMessageBox.question(
               self, "Money Calulate", f"Money you will get : {money:.2f} Th baht.Confirm?", QMessageBox.Yes | QMessageBox.No
           )
           if reply == QMessageBox.Yes:
               self.paidEmployeeCount += 1
               self.totalSeverancePaid += money
               self.paidEmployeeIDs.add(employeeId)
               
               self.paidEmployeeLabel.setText(
                   f"Paid Employee: {self.paidEmployeeCount}"
               )
               self.totalSeverancePayLabel.setText(
                   f"Total Severance Paid: {self.totalSeverancePaid:.2f} THB"
               )
               self.paidEmployeeIDLabel.setText(
                   f"Employee ID Paid: {', '.join(self.paidEmployeeIDs)}"
               )
               
               self.employeeIdInput.clear()
               self.employeePositionInput.clear()
               self.employeeSalaryInput.clear()
               self.employeestartDateInput.clear()
               
        else:
            QMessageBox.warning(self, "Error", "Invalid input. Please try again.") #เตือน
        

# start application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())



