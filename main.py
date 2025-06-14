import random 


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count  = {
  "A" : 2,
  "B" : 4,
  "C" : 6,
  "D" : 8
}


def get_slot_machine_spin(rows,cols, symbols ):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for i in range(symbol_count):

def deposit():
  while True:
    amount = input("What would You Like to deposit?:  ")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Amount must be greater than 0.")
    else:
      print("please Enter a valid number")
  return amount


def get_bet ():
  while True:
    amount = input("What would You Like to bet?:  ")
    if amount.isdigit():
      amount = int(amount)
      if MIN_BET<= amount <= MAX_BET:
        break
      else:
        print(f"Amount must be between ${MIN_BET}- ${MAX_BET}")
    else:
      print("please Enter a valid number")
  return amount



def get_number_of_lines():
   while True:
     lines = input("Enter The Number of Lines to be bet on (1-" + str(MAX_LINES) + ")?  ")
     if lines.isdigit():
       lines = int(lines)
       if 1 <= lines <= MAX_LINES:
         break 
       else:
         print("Enter a Valid Number of Lines")

     else:
       print("Please Enter Valid Number of Lines ")
   return lines




def main():
  balance = deposit()
  lines = get_number_of_lines()
  while True:
    bet = get_bet()
    total_bet = bet * lines

    if total_bet> balance:
      print(f"You don't have enough to bet on that amaount, your current balance is: ${balance} ")
    
    else:
      break


  print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
  print(lines,balance)
main()

