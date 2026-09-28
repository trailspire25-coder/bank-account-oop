ElectricUsage = float(input("Enter your Electricity usage(kWh): "))

Bill1 = 0.5 * ElectricUsage
Bill2 = 0.75 * ElectricUsage
Bill3 = 1 * ElectricUsage
Bill4 = 1.25 * ElectricUsage


if ElectricUsage < 101:
    print(f"Your Bill is GHs {Bill1:.2f}")

elif ElectricUsage < 201 and ElectricUsage > 100:
    print(f"Your Bill is GHs {Bill2:.2f}")

elif ElectricUsage < 301 and ElectricUsage > 200:
    print(f"Your Bill is GHs {Bill3:.2f}")

else:
    print(f"Your Bill is GHs {Bill4:.2f}")