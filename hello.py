def calculate_interest(calculated_interest):
    calculated_interest = (input_principal_amount * input_interest_rate * input_investment_time) / 100
    print(f"The simple interest for a principal amount of ${input_principal_amount:,.2f} \
at an interest rate of {input_interest_rate}% over a period of {input_investment_time} years is: ${calculated_interest:,.2f}")

input_principal_amount = float(input("Enter the principal amount: "))
input_interest_rate = float(input("Enter the interest rate: "))
input_investment_time = float(input("Enter the investment time: "))

calculate_interest(calculated_interest = (input_principal_amount * input_interest_rate * input_investment_time) / 100)