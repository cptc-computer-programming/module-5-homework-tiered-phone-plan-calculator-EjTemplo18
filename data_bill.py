# constant values are set here:
TIER_1_DATA_LIMIT_GB = 10
TIER_2_DATA_LIMIT_GB = 20
PREMIUM_USER_OVERAGE_RATE_TIER_2 = 1
REGULAR_USER_OVERAGE_RATE_TIER_2 = 2
PREMIUM_USER_OVERAGE_RATE_TIER_3 = 2
REGULAR_USER_OVERAGE_RATE_TIER_3 = 3

# Your code goes here:
# Input:

data_used = int(input("Enter data used (GB): "))
monthly_cost = int(input("Enter monthly plan cost: "))
premium_plan = input("Do you have a premium plan? Enter yes or no: ")

is_premium = premium_plan == "yes"

# Process:

if data_used <= TIER_1_DATA_LIMIT_GB:
    overage_gb = 0
else:
    overage_gb = data_used - TIER_1_DATA_LIMIT_GB

if overage_gb == 0:
    overage_rate = 0

elif data_used <= TIER_2_DATA_LIMIT_GB:
    overage_rate = PREMIUM_USER_OVERAGE_RATE_TIER_2 if is_premium else REGULAR_USER_OVERAGE_RATE_TIER_2

else:
    overage_rate = PREMIUM_USER_OVERAGE_RATE_TIER_3 if is_premium else REGULAR_USER_OVERAGE_RATE_TIER_3

overage_cost = overage_gb * overage_rate
total_bill = monthly_cost + overage_cost

# Output:

print(f"GB over the limit: {overage_gb:.2f}")
print(f"Overage cost: ${overage_cost:.2f}")
print(f"Total bill: ${total_bill:.2f}")