times_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rate = []
for time in times_slots:
    rate = int(input(f"Enter your heart rate for {time}: "))
    heart_rate.append([time, rate])
print(heart_rate)
total = 0
for rate in heart_rate:
    total += rate[1]
average = round(total / len(heart_rate))
print("average heart rate:", average)0