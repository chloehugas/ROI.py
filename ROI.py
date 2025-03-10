import math


def mortgage_payment(principal, annual_interest_rate, years):
    monthly_rate = annual_interest_rate / 12 / 100
    n = years * 12
    if monthly_rate == 0:
        return principal / n
    return principal * (monthly_rate * (1 + monthly_rate) ** n) / ((1 + monthly_rate) ** n - 1)


def calculate_roi(purchase_price, down_payment, loan_term, interest_rate, monthly_rent,
                  property_taxes, insurance, maintenance, hoa_fees, appreciation_rate):
    # Loan details
    loan_amount = purchase_price - down_payment
    monthly_mortgage = mortgage_payment(loan_amount, interest_rate, loan_term)

    # Monthly expenses
    total_monthly_expenses = property_taxes / 12 + insurance / 12 + maintenance / 12 + hoa_fees + monthly_mortgage

    # Cash flow
    monthly_cash_flow = monthly_rent - total_monthly_expenses

    # Annual cash flow
    annual_cash_flow = monthly_cash_flow * 12

    # Total cash invested (down payment + closing costs, assuming 2% of purchase price)
    total_cash_invested = down_payment + (purchase_price * 0.02)

    # ROI calculation
    roi = (annual_cash_flow / total_cash_invested) * 100

    return {
        'Monthly Mortgage': round(monthly_mortgage, 2),
        'Monthly Cash Flow': round(monthly_cash_flow, 2),
        'Annual Cash Flow': round(annual_cash_flow, 2),
        'Total Cash Invested': round(total_cash_invested, 2),
        'ROI (%)': round(roi, 2)
    }


# Sample inputs
purchase_price = float(input("Enter property purchase price: "))
down_payment = float(input("Enter down payment: "))
loan_term = int(input("Enter loan term (years): "))
interest_rate = float(input("Enter annual interest rate (%): "))
monthly_rent = float(input("Enter expected monthly rent: "))
property_taxes = float(input("Enter annual property taxes: "))
insurance = float(input("Enter annual insurance cost: "))
maintenance = float(input("Enter annual maintenance cost: "))
hoa_fees = float(input("Enter monthly HOA fees: "))
appreciation_rate = float(input("Enter annual property appreciation rate (%): "))

# Calculate ROI
results = calculate_roi(purchase_price, down_payment, loan_term, interest_rate, monthly_rent,
                        property_taxes, insurance, maintenance, hoa_fees, appreciation_rate)

# Display results
print("\nReal Estate ROI Calculation:")
for key, value in results.items():
    print(f"{key}: ${value}")
