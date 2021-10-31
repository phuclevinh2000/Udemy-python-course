stock_prices = [('APPl', 200), ('GOOG', 400), ('FACE', 600)]
for item, price in stock_prices:
    print(price)

# check salary for employee
work_hours = [('Abby', 100), ('Billy', 7600), ('Cass', 500)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hours:
        if(hours > current_max):
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month, current_max)


print(employee_check(work_hours))
# extract name, hour from the return
name, hour = employee_check(work_hours)
print(name)
