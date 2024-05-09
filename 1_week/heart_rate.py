"""When you physically exercise to strengthen your heart, you should maintain your heart rate within a range for at least 20 minutes. To find that range, subtract your age from 220. This difference is your maximum heart rate per minute. Your heart simply will not beat faster than this maximum (220 - age). When exercising to strengthen your heart, you should keep your heart rate between 65% and 85% of your heart's maximum rate."""

#This is the number that we have to substract
base = float(220)

#Age from the user
age = float(input('Please enter your age: '))

heart_rate_per_minute_65 = int((base - age) * 0.65)
heart_rate_per_minute_85 = int((base - age) * 0.85)

print(f"When you exercise to strengthen your heart, you should keep your heart rate between\n {heart_rate_per_minute_65} and {heart_rate_per_minute_85} beats per minute")