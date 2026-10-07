"""
Employee Salary & Benefits System - *args, **kwargsA company wants a reusable function to generate an employee's salary report.
Every employee has:
● ​Employee name
● ​Basic salary
● ​Any number of allowances, where only the amounts matter
● ​Any number of deductions, where each deduction has a meaningful name such ​as PF, Tax, Insurance, Loan

Calculate and display:
●​ Total allowances
● ​Gross salary
● ​Total deductions
● ​Net salary
● ​Complete deduction details

Example:
Employee: Rahul
Basic Salary: ₹50,000
Allowances:
₹5,000
₹3,000
₹2,000
Deductions:
PF = ₹3,000
Tax = ₹2,000
Insurance = ₹1,000
"""

def salary_report(employee_name, basic_salary, *allowances, **deductions):
    total_allowances = sum(allowances)
    gross_salary = basic_salary + total_allowances
    total_deductions = sum(deductions.values())
    net_salary = gross_salary - total_deductions

    print(f"Employee: {employee_name}")
    print(f"Basic Salary: ₹{basic_salary}")
    print("Allowances:")
    for allowance in allowances:
        print(f"₹{allowance}")
    print("Deductions:")
    for deduction_name, deduction_amount in deductions.items():
        print(f"{deduction_name} = ₹{deduction_amount}")
    print(f"Total Allowances: ₹{total_allowances}")
    print(f"Gross Salary: ₹{gross_salary}")
    print(f"Total Deductions: ₹{total_deductions}")
    print(f"Net Salary: ₹{net_salary}")
