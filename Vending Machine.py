print("""
██    ██ ███████ ███    ██ ██████  ██ ███    ██  ██████      ███    ███  █████   ██████ ██   ██ ██ ███    ██ ███████ 
██    ██ ██      ████   ██ ██   ██ ██ ████   ██ ██           ████  ████ ██   ██ ██      ██   ██ ██ ████   ██ ██      
██    ██ █████   ██ ██  ██ ██   ██ ██ ██ ██  ██ ██   ███     ██ ████ ██ ███████ ██      ███████ ██ ██ ██  ██ █████   
 ██  ██  ██      ██  ██ ██ ██   ██ ██ ██  ██ ██ ██    ██     ██  ██  ██ ██   ██ ██      ██   ██ ██ ██  ██ ██ ██      
  ████   ███████ ██   ████ ██████  ██ ██   ████  ██████      ██      ██ ██   ██  ██████ ██   ██ ██ ██   ████ ███████  
      """)

#function to operate the vending machine based on the amount of money of user
def vendingmachine(amount_cash):
    total = 0

    #define items available in the vending machine
    drinks = [ #drinks category with item number, name, price, and stock
        {'item no.': 'D1', 'item': 'Cocal Cola', 'price': 2.0, 'stock': 5},
        {'item no.': 'D2', 'item': 'Sprite', 'price': 2.0, 'stock': 5},
        {'item no.': 'D3', 'item': 'Fanta', 'price': 2.0, 'stock': 5},
        {'item no.': 'D4', 'item': 'Pepsi', 'price': 2.0, 'stock': 5},
        {'item no.': 'D5', 'item': 'Mountain Dew', 'price': 2.0, 'stock': 5},
        {'item no.': 'D6', 'item': 'Mineral Water', 'price': 1.5, 'stock': 15},
    ]

    snacks = [ #snacks category with item number, name, price, and stock
        {'item no.': 'S1', 'item': 'Piattos', 'price': 1.5, 'stock': 5},
        {'item no.': 'S2', 'item': 'Nova', 'price': 1.75, 'stock': 5},
        {'item no.': 'S3', 'item': 'V Cut', 'price': 1.25, 'stock': 5},
        {'item no.': 'S4', 'item': 'Clover', 'price': 2.0, 'stock': 5},
        {'item no.': 'S5', 'item': 'Tortillos', 'price': 2.0, 'stock': 5},
    ]

    chocolates = [ #chocolates category with item number, name, price, and stock
        {'item no.': 'C1', 'item': 'Kitkat', 'price': 2.5, 'stock': 5},
        {'item no.': 'C2', 'item': 'Snickers', 'price': 4.0, 'stock': 5},
        {'item no.': 'C3', 'item': 'Hersheys', 'price': 4.0, 'stock': 5},
        {'item no.': 'C4', 'item': 'M&Ms', 'price': 4.0, 'stock': 5},
    ]

    #function to display menu for the selected category
    def menu(category):
        #printing formatted menu
        print ('\n')
        print ('┌───────┬─────────────────┬───────┬───────┐')
        print ('│ Item# │      Item       │ Price │ Stock │')
        print ('├───────┼─────────────────┼───────┼───────┤')
        
        for item in category:
            item_num = item['item no.']
            item_name = item['item']
            price = f"${item['price']}" #f string will allow expressions to embed within curly brackets {}
            stock = str(item['stock'])

            #will print menu table where contents are properly centered
            print(f"│{item_num.center(7)}│{item_name.center(17)}│{price.center(7)}│{stock.center(7)}│") 
        
        print ('└───────┴─────────────────┴───────┴───────┘')
    
    #function to select item from selected category
    def select(category):
        #prompting the user to input the item number of item they want to purchase
        while True:
            item_num = input('Please enter the item # of item to purchase ("cancel" to go back): ')
            if item_num.lower() == 'cancel':
                return None
            for item in category:
                if item['item no.'].lower() == item_num.lower() and item['stock'] > 0: #checks if item number is valid and have stock
                   return item
            print ('\nInvalid item number or item out of stock. Please try again.')

    #function to process payment for selected item
    def payment_process(selected,total):
        price = float(selected['price'])
        stock = selected['stock']

        if stock <= 0: #checks if item is in stock
            print ('Sorry, this item is out of stock.') #output if item is not available
            return total
        
        print (f"Enjoy your {selected['item']}!") #output if purchase is successful
        selected['stock'] -= 1
        total += price

        return total
        
    while True:
        #displaying options to select category or finish purchasing
        print ('\nPlease select a category of item to purchase: ')
        print ('1 - Drinks')
        print ('2 - Snacks')
        print ('3 - Chocolates')
        print ('4 - Done')

        choice = input('Please enter the number of your choice: ') #asks user the number of their selected option

        if choice == '4': #purchase ends here
            print ('\n────────────────────────────────────────────────────────────────────')
            print ('┌───────────────────────────────────────────────────────────────────┐')
            print ('│             Thank you for using the vending machine.              │')
            print ('└───────────────────────────────────────────────────────────────────┘')
            break
    
        #will handle user's choice and will display menu of selected category
        elif choice in ['1', '2', '3']:
            if choice == '1':
                menu(drinks)
                selected = select(drinks)
            elif choice == '2':
                menu(snacks)
                selected = select(snacks)
            elif choice == '3':
                menu(chocolates)
                selected = select(chocolates)

            #processing selected item if checked available
            if selected:
                total = payment_process(selected, total)

        else: #output if choice is invalid
            print ('Invalid choice. Please enter a valid option.')
    
    return total

def valid_cash():
#asks user for the amount of money they have
  while True:
    try:
        amount_cash = float(input('Please enter cash: $'))
        if amount_cash <= 0: #input amount should be more than 0
            print ('Please enter valid amount greater than 0.')
        else:
            return amount_cash
    except ValueError: #maintains program stability if user input can't be interpreted as float; then prompts user to enter valid number
        print ('Please enter a valid number/amount.')

amount_cash = valid_cash()

#loop to operate vending machine and handle purchase process    
while True:
  #runs vending machine  with the amount of money entered
  total_all = vendingmachine(amount_cash)

  #checks if total cost exceeds amount of money entered
  if total_all > amount_cash:
    #output that will notify user about insufficient money and suggests to reselect items
    print (' Item/s not dispensed. Purchase cancelled due to insufficient cash.')
    print ('''       Please select item(s) totaling an amount within your
                         remaining balance.''')
    print ('────────────────────────────────────────────────────────────────────\n')
    print ('                             Reselect                               ')
    print (' ')

  else:
    #calculates change
    change = amount_cash - total_all
     
    print ('                 Item/s have been dispensed. Enjoy!                 ')
    print ('────────────────────────────────────────────────────────────────────')    
    print (f'\nTotal: ${total_all:.2f}') #displays total
    print ('────────────────────────────────────────────────────────────────────')
    print (f'Change: ${change:.2f}') #displays change
    print ('────────────────────────────────────────────────────────────────────')
    print ('\n')
    break #break out of the loop once purchase is completed
