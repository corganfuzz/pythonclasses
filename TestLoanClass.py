from Loan import Loan


def main():
    annualInterestRate = eval(input("Enter yearly interest rate, for example, 7.25: "))

    numberOfYears = eval(input("Enter number of years as integer: "))

    loanAmount = eval(input("Enter loan amount, ex 120000.95: "))

    borrower = input("Enter a borrowers name: ")

    # Create a loan object
    loan = Loan(annualInterestRate, numberOfYears, loanAmount, borrower)

    print("the loan is for", loan.getBorrower())
    print("the monthly payment is", format(loan.getMonthlyPayment(), ".2f"))
    print("the total payment is", format(loan.getTotalPayment(), ".2f"))


main()
