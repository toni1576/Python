# Change a num INT variable by adding
name = "Antonio"
age = 19

print(f"{name} is {age} and will be {age +1} next year")

# Columns alignment, makes the name appear in different spaces/spacing
print(f"{name:<30}")
print(f"{name:>30}")
print(f"{name:^30}")

# Calculating
score_1 = 88
score_2 = 73
score_3 = 65

average = (score_1 + score_2 + score_3) / 3

print(average)
print(f"{average: ,.0f}")

# Idk lmao
distance_to_monroe = 852
distance_to_phoenix = 1712

print(f"distance to monroe, North Carolina{distance_to_monroe: ,.0f}")
print(f"distance to Phoenix, Arizona {distance_to_phoenix: ,.0f}")

# how to use percentage
current_mort_rate = 0.0675
print(f"Mortgage rate = {current_mort_rate: .2%}")
