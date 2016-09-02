hourly_rate = 12.0
overtime = hourly_rate *1.5
standard_hours =40
hours_worked = 60
income = ((hours_worked - standard_hours)*overtime) + (standard_hours *hourly_rate)

print("This week I worked")
print(hours_worked)
print("I made")
print(income)
print("This week")
