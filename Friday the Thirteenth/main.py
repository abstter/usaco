'''
ID: Abhiram Avasarala
LANG: PYTHON3
TASK: friday 
'''
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def day_of_week(year, month, day):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check for leap year 
    if is_leap_year(year):
        days_in_month[2] = 29
    
    # Zeller's Congruence algorithm for finding the day of the week
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    day_of_week = (day + 13 * (month + 1) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
    
    return day_of_week

def friday(n):
    days_count = [0] * 7  # Initialize an array 
    
    for year in range(1900, 1900 + n):
        for month in range(1, 13):
            day_of_13th = day_of_week(year, month, 13)
            days_count[day_of_13th] += 1
    
    return days_count

# Read input from file
with open('friday.in', 'r') as infile:
    n = int(infile.readline().strip())

# Calculate result
result = friday(n)

# Write output to file
with open('friday.out', 'w') as outfile:
    outfile.write(' '.join(map(str, result)) + '\n')



