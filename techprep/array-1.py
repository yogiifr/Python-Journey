# 1. Let us say your expense for every month are listed below,
#     1. January - 2200
#     2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190

# Create a list to store these monthly expenses and using that find out,

expenses = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
feb_to_jan = expenses[1] -expenses[0]
print(f"Expenses compare from Februari and Januari is {feb_to_jan}")

# 2. Find out your total expense in first quarter (first three months) of the year.
first_quarter = expenses[0] + expenses[1] + expenses[2]
print(f"Expenses on the first quarter {first_quarter}")

# 3. Find out if you spent exactly 2000 dollars in any month
month_count = 0

for exp in expenses:
    if exp == 2000:
        month_count += 1

print (f"Total month with exaclty 2000 spends is {month_count}")
# Or
print("Did I spent 2000$ in any month? ", 2000 in exp)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
add_june = expenses.append(1980)
print (expenses)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list based on this
april_expenses = expenses[3]
print (f"Expenses on April {april_expenses}")
april_expenses = expenses[3] + 200
print (f"April expenses after refund {april_expenses}")
