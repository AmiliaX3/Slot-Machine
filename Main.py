import random

#BETTING SETTINGS
MAX_LINES = 3 #max of line, save time from adding the amount every time
MAX_BET = 200 #max of bet, save time from adding the amount every time
MIN_BET = 10 #min of bet, save time from adding the amount every time

#SLOT MACHINE LAYOUT
ROWS = 3 #amount of rows
COLS = 3 #amount of columns

#SYMBOLS
symbol_count = {
    "A": 2,
    "B": 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C" : 3,
    "D" : 2
}

#check for winnings, if the player won or not
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines

#GENERATE OUTCOMES
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols): #amount of columns to generate per spin
        column = []
        current_symbols = all_symbols[:] #pick from the copy symbol list
        for _ in range(rows): #amount of rows to generate per spin
            value = random.choice(current_symbols) #pick a random value from the list
            current_symbols.remove(value) #prevent picking the same value
            column.append(value) #this need to be column instead of columns due to the need to filling the columns

        columns.append(column)

    return columns

def print_slot_machine(columns): #see columns
    for row in range(len(columns[0])): #loop every column
        for i, column in enumerate (columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

        
def deposit(): #define the player balance
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Amount must be greater than 0.")
        else:
            print("Please enter an amount")

    return amount

def get_number_of_lines(): #define amount of slot lines allowed 
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
    return lines

def get_bet(): #define the amount allowed to bet per line
    while True:
        amount = input("How much do you want to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
                print("Please enter a vaild amount.")
        else:
            print("Please enter the amount you want to bet: $")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
            bet = get_bet()
            total_bet = bet * lines
    
            if total_bet > balance: #not enough in the account to bet
                print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
            else:
                break
                
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}") #has enough or more to bet
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)

    if winnings >= 0:
        print(f"You won ${winnings}!!!")
        print(f" How many lines you won:", *winnings_lines)
    else:
        print("You didn't win anything, better luck next time!")
    
    return winnings - total_bet #return the amount won minus the amount bet


def main(): #result 
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You have left with ${balance}")

    if balance <= 0:
        print("Thank you for playing, come back soon! Press q to quit.")
    
    

main()
