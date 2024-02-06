#define variables ofr Kilogram (kg) values
kg_value_1 = 50
kg_value_2 = 926
kg_value_3 = 43.9

#conversion factor: 1 pound (lb) = Kilograms (kg) * 2.20462
conversion_factor = 2.20462

#calculate pounds for each kilogram value
pounds_1 = kg_value_1 * conversion_factor
pounds_2 = kg_value_2 * conversion_factor
pounds_3 = kg_value_3 * conversion_factor

#output the results
print(f"{kg_value_1} kilograms is equal to {pounds_1:.2f} pounds.")
print(f"{kg_value_2} kilograms is equal to {pounds_2:.2f} pounds.")
print(f"{kg_value_3} kilograms is equal to {pounds_3:.2f} puounds.")