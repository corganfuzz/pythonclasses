from AccountClass import Account


def main():

    id = 1122
    balance = 20000
    annualInterestRate = 4.5

    account = Account(id, balance, annualInterestRate)

    print('the account id is ', account.getId())
    print('the balance of the account is ', format(account.getBalance(), '.2f'))
    print('the monthly interest rate is ', format(account.getMonthlyInterestRate(), '.5f'))
    print('the monthly interest is ', format(account.getMonthlyInterest(), '.2f'))
    print('After withdraw the balance is', format(account.withdraw(), '.2f'))
    print('After deposit the balance is', format(account.deposit(), '.2f'))


main()
