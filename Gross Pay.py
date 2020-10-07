#This program gives the user their gross pay
base_hours = 40 #base hours per week
Overtime_multiplier =1.5 #Multiplier for the amount of overtime hours
hours_worked=float(input("Please enter the number of  hours worked "))
hourly_pay_rate=float(input("Enter your hourly pay rate: "))
if hours_worked>base_hours:
    overtime_hours=hours_worked-base_hours

    overtime_pay = overtime_hours*hourly_pay_rate*Overtime_multiplier
    gross_pay=base_hours*hourly_pay_rate+overtime_pay
else:
    gross_pay=hours_worked*hourly_pay_rate
print('The gross pay is $', format(gross_pay, ' ,.2f'))
