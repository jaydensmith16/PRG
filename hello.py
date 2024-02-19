# Days of the week
days = ["Monday", "Tuesday"," Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# how many steps the person took per day
step_num = [1200, 3400, 2000, 900, 910, 1000, 800]
# The numbers are in place of the numbers someone would be putting into this code

for i in range(len(days)):
    day = days[i]
    steps = step_num[i]
    # takes number of steps from the steps list
    print(f"On {day} how many steps did you take?")
    print(f"{steps}")
# total step calculation
total_steps = sum(step_num)
print(f"The total steps for the week is {total_steps}.")
# average steps per day
average = (total_steps // 7)
print(f"The average steps per day is {average}.")