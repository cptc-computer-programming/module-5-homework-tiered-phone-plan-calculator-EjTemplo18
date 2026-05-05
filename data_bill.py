# constant values are set here:
TIER_1_DATA_LIMIT_GB = 10
TIER_2_DATA_LIMIT_GB = 20
PREMIUM_USER_OVERAGE_RATE_TIER_2 = 1
REGULAR_USER_OVERAGE_RATE_TIER_2 = 2
PREMIUM_USER_OVERAGE_RATE_TIER_3 = 2
REGULAR_USER_OVERAGE_RATE_TIER_3 = 3

# Your code goes here:

data_used = float(input("Enter data used (GB): "))
monthly_plan_cost = float(input("Enter monthly plan cost: "))
premium_plan = input("Do you have a premium plan? Enter yes or no: ")

if premium_plan == "yes":
    print("You have a premium plan.")
elif premium_plan == "no":
    print("You don't have a premium plan.")
else:
    print("Invalid input.")