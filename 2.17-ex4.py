# This code calculates the day of return from 
# holidays, asking the user for the day they left
# and how many days are out, counting Sunday as 
# day 0 and Saturday the day 6


starting_day_number = input("what number of day are you leaving? ")
days_out = input("what is the length of your stay? ")

starting_day_int = int(starting_day_number)
days_out_int = int(days_out)

sum_days = starting_day_int + days_out_int

return_day = sum_days % 7

print(return_day)
