def GetEmployeeInfo():
    employee = input("Enter Employee Name: ")
    return employee
def GetHoursWorked():
    hours = float(input("Enter Hours: "))
    return hours
def GetHourlyRate():
    hourlyrate = float(input("Enter Hourly Rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input("Enter Tax Rate: "))
    return taxrate
def CalcNetPay(hours, hourlyrate, taxrate):
    grosspay = hourlyrate * hours
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay
def PrintAll(employee, hours, hourlyrate, grosspay, taxrate, incometax, netpay ):
    print(employee, f"{hours:,.2f}", f"${grosspay:,.2f}", f"{taxrate:,.2%}", f"${incometax:,.2f}", f"${netpay:,.2f}")
def PrintTotal(TotalEmp, TotalHours, TotalGP, TotalTaxes, TotalNP):
    print()
    print(f"Total Amount of Employees: {TotalEmp}")
    print(f"Total Hours Worked: {TotalHours:,.2f}")
    print(f"Total Gross Pay: ${TotalGP:,.2f}")
    print(f"Total Income Tax: ${TotalTaxes:,.2f}")
    print(f"Total Net Pay: ${TotalNP:,.2f}")
if __name__== "__main__":
    TotalEmp = 0
    TotalHours = 0.00
    TotalGP = 0.00
    TotalTaxes = 0.00
    TotalNP = 0.00
    while True:
        employee = GetEmployeeInfo()
        if (employee.upper() == "END"):
            break
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        grosspay, incometax, netpay = CalcNetPay(hours, hourlyrate, taxrate)
        PrintAll(employee, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotalEmp += 1
        TotalHours += hours
        TotalGP += grosspay
        TotalTaxes += incometax
        TotalNP += netpay

PrintTotal(TotalEmp, TotalHours, TotalGP, TotalTaxes, TotalNP)