oranges = 12
cost_per_orange = 0.5
total_cost = oranges * cost_per_orange
output = '{} oranges costs £{}' .format(oranges , total_cost)
print(output)
#alternatively
output = str(oranges) + " oranges costs £" + str(total_cost)
print(output)

days = 31
hours = 24
total_hours = days * hours
msg = "There are {} in {} days".format(total_hours, days)
print(msg)



