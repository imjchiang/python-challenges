print("Welcome to Chase bank.")

balance = input("Your balance is\n")
balance = int(balance)

def complete():
    finish = input("Are you done? (Y/N)\n")

    if (finish == "Y"):
        print("Have a nice day!")
    elif (finish == "N"):
        do_something(balance)
    else:
        print("INVALID INPUT")
        complete()

def do_something(balance):
    options = input("What would you like to do? (deposit, withdraw, check_balance)\n")

    if (options == "deposit"):
        deposit = input("How much would you like to deposit?\n")
        deposit = int(deposit)
        balance += deposit
    elif (options == "withdraw"):
        withdraw = input("How much would you like to withdraw?\n")
        withdraw = int(withdraw)
        balance -= withdraw
    elif (options == "check_balance"):
        print("Your balance is {}".format(balance))
    else:
        print("INVALID INPUT")

    complete()
    

do_something(balance)
