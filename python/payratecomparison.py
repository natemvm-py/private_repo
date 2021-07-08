#VARIABLES
hourly_rate = 0.0
tax_percent = 0.0
ksaver_percent = 0.0
hours = 0.0
gross_pay = 0.0
take_pay = 0.0
fuckyou = 0

#PROGRAM

tax_percent = float(input("Enter tax rate percent: "))
print(type(tax_percent))
ksaver_percent = float(input("Enter kiwisaver contribution percent: "))
print(type(ksaver_percent))
hours = float(input("Enter amount of hours: "))
print(type(hours))

count = int(input("How many times do you want the script to compare rates?"))

for i in range(count):
    hourly_rate = float(input("Enter hourly rate: "))
    print(type(hourly_rate))

    gross_pay = hourly_rate * hours
    print(gross_pay)

    ksaver_taken = ksaver_percent * gross_pay / 100
    print(ksaver_taken)
    tax_taken = tax_percent * gross_pay / 100
    print(tax_taken)
    take_pay = gross_pay - ksaver_taken - tax_taken
    print("Take Home Pay:", take_pay)