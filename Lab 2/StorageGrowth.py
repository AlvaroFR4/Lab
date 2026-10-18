GROWTH = 1.06

usage = float(input("Current usage in GB: "))

month1 = usage * GROWTH
month2 = month1 * GROWTH
month3 = month2 * GROWTH

print(f"Month 1: {month1:.2f} GB")
print(f"Month 2: {month2:.2f} GB")
print(f"Month 3: {month3:.2f} GB")
