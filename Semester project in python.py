def tax(price):
    return int(0.17 * price)


def rating(stars_no):
    review_stars = stars_no * '*'
    return review_stars


def customer():

    print('''    
           
          The names of the restaurants are given below
          --------------------------------------------
                      1 =  McDonalds
                      2 =  KFC
                      3 =  Ranchers
          --------------------------------------------''')
    while True:
        try:
            rest_selct = int(input("Enter the restaurant number:    "))
            if rest_selct == 1 or rest_selct == 2 or rest_selct ==3:
                break
        except ValueError:
            print("Please input correct restaurant number")
            continue

    rest_selct -= 1
    if rest_selct == 0:
        mcdonalds()
    elif rest_selct == 1:
        kfc()
    else:
        ranchers()





def restaurant_owner():
    print("* OWNERS SECTION *")
    print(''' 
    [1]MCDONALDS                  
    [2]KFC                             
    [3]Ranchers                         ''')
    mcdonaldsmenu = [
        'Zinger burger',
        'Happy meal',
        'Fries',
        'Wraps',
        'Tiramisu Cake',
        'Coffee',
        'Drink']
    mcdonaldsmenuprice = [550,
                          700,
                          200,
                          320,
                          500,
                          120,
                          70]
    kfcmenu = ['krunch', 'zinger', 'Hot wings', 'rice', 'Pizza', 'Boneless', 'drink']
    kfcmenuprice = [200,
    400,
    550,
    250,
    1050,
    350,
    70]
    ranchersmenu = ['krunch', 'zinger', 'mighty', 'rice', 'salad', 'wings', 'drink']
    ranchersmenuprice = [200,
        400,
        550,
        250,
        50,
        350,
        70]
    while True:
        try:
            name = int(input("Which restaurant do you own:?"))
            if 0 < name < 4:
                break
        except ValueError:
            print("Enter the correct number")
            continue
#mcdonalds starts from here.
    if name == 1:
        while True:
            name = "MCDONALDS"  #only admins can change the password.
            password = "1234"
            print("Login")
            restaurant_name = str(input("Enter the restaurant ID : ")).upper()
            restaurant_password = str(input("Enter your password : "))
            if restaurant_name == name and restaurant_password == password:
                    print("You have logged in")
                    break
            else:
                print("invalid credentials")
        while True:
            while True:
                try:
                    options = int(input('''
                    Press [1] to view your menu.
                    Press [2] to edit your menu.
                    Press [3] to exit.\n
                    '''))

                    if 0<options<4:
                        break
                except ValueError:
                    print("invalid credentials")
                    continue

            if options == 3:
                break
            elif options == 1:
                print('''
                 [1]Zinger burger                               Rs;550',
                 [2]Happy meal                                  Rs;700'
                 [3]Fries                                       Rs;200'
                 [4]Wraps                                       Rs;320'
                 [5]Tiramisu Cake                               Rs;500'
                 [6]Coffee                                      Rs;120'
                 [7]Drink                                       Rs;70''')
            elif options == 2:
                print('''What changes do you want to make in current menu?
                [1]Zinger burger                               Rs;550'
                [2]Happy meal                                  Rs;700'
                [3]Fries                                       Rs;200'
                [4]Wraps                                       Rs;320'
                [5]Tiramisu Cake                               Rs;500'
                [6]Coffee                                      Rs;120'
                [7]Drink                                       Rs;70
                ''')
                while True:
                    try:
                        edit = int(input('''Press
                        [1] To add items
                        [2] To remove items
                        [3] To exit\n'''))
                        if 0 < edit < 4:
                            break
                    except ValueError:
                        print("invalid credentials")
                        continue

                if edit == 3:
                    break

                elif edit == 1:
                    item = str(input('Enter the item you want to add:'))
                    mcdonaldsmenu.append(item)
                    while True:
                        try:
                            price = int(input("Enter the price for the item you have added:"))
                            break
                        except ValueError:
                            print("Invalid credentials")
                    mcdonaldsmenuprice.append(price)
                    print("Your item", item, 'is added for the price', price)
                    print(mcdonaldsmenu)
                    print(mcdonaldsmenuprice)


                else:
                    print('''
                    [1]Zinger burger            
                    [2]Happy meal                                 
                    [3]Fries                                     
                    [4]Wraps                                    
                    [5]Tiramisu Cake                            
                    [6]Coffee                                      
                    [7]Drink                                       ''')
                    while True:
                        try:
                            remove1 = int(input("Enter the number of item you want to remove?"))
                            break
                        except ValueError:
                            print("Invalid Credentials")
                            continue
                    remove1 -= 1
                    mcdonaldsmenu.remove(mcdonaldsmenu[remove1])
                    print('''
                    [1]Zinger burger                         Rs;550
                    [2]Happy meal                            Rs;700
                    [3]Fries                                 Rs;200
                    [4]Wraps                                 Rs;320
                    [5]Tiramisu Cake                         Rs;500
                    [6]Coffee                                Rs;120
                    [7]Drink                                 Rs;70''')
                    while True:
                        try:
                            removeprice = int(input("Enter the price of the item you have removed."))
                            break
                        except ValueError:
                            print("invalid Credentials")
                            continue
                    mcdonaldsmenuprice.remove(removeprice)
                    print(mcdonaldsmenu)
                    print(mcdonaldsmenuprice)

#kfc starts from here.
    elif name==2:
        while True:
            name = "KFC"
            password = "1234"
            print("Login")
            restaurant_name = str(input("Enter the restaurant ID : ")).upper()
            restaurant_password = str(input("Enter your password : "))
            if restaurant_name == name and restaurant_password == password:
                print("You have logged in")
                break
            else:
                print("invalid credentials")
        while True:
            while True:
                try:
                    options = int(input('''
                    Press [1] to view your menu.
                    Press [2] to edit your menu.
                    Press [3] to exit.\n
                    '''))

                    if 0 < options < 4:
                        break
                except ValueError:
                    print("invalid credentials")
                    continue
            if options == 3:
                break
            elif options == 1:
                print('''
            [1]Krunch                                 Rs;200
            [2]Zinger                                 Rs;400
            [3]Hot wings                              Rs;550
            [4]Rice                                   Rs;250
            [5]Pizza                                  Rs;1050
            [6]Boneless                               Rs;350
            [7]Drink                                  Rs;70''')
            elif options == 2:
                print('''What changes do you want to make in current menu?
            [1]Krunch                                 Rs;200
            [2]Zinger                                 Rs;400
            [3]Hot wings                              Rs;550
            [4]Rice                                   Rs;250
            [5]Pizza                                  Rs;1050
            [6]Boneless                               Rs;350
            [7]Drink                                  Rs;70
                ''')
                while True:
                    try:
                        edit = int(input('''Press
                        [1] To add items
                        [2] To remove items
                        [3] To exit\n'''))
                        if 0 < edit < 4:
                            break
                    except ValueError:
                        print("invalid credentials")
                        continue

                if edit == 3:
                    break
                elif edit == 1:
                    item = str(input('Enter the item you want to add:'))
                    kfcmenu.append(item)
                    while True:
                        try:
                            price = int(input("Enter the price for the item you have added:"))
                            break
                        except ValueError:
                            print("Invalid credentials")
                    kfcmenuprice.append(price)
                    print("Your item", item, 'is added for the price', price)
                    print(kfcmenu)
                    print(kfcmenuprice)

                else:
                    print('''
                    [1]Krunch                                 
                    [2]Zinger                              
                    [3]Hot wings                     
                    [4]Rice                                
                    [5]Pizza                               
                    [6]Boneless                            
                    [7]Drink                    ''')
                    while True:
                        try:
                            remove1 = int(input("Enter the number of item you want to remove?"))
                            break
                        except ValueError:
                            print("Invalid Credentials")
                            continue
                    remove1 -= 1
                    mcdonaldsmenu.remove(mcdonaldsmenu[remove1])
                    print('''
                    [1]Krunch                                 Rs;200
                    [2]Zinger                                 Rs;400
                    [3]Hot wings                              Rs;550
                    [4]Rice                                   Rs;250
                    [5]Pizza                                  Rs;1050
                    [6]Boneless                               Rs;350
                    [7]Drink                                  Rs;70''')
                    while True:
                        try:
                            removeprice = int(input("Enter the price of the item you have removed."))
                            break
                        except ValueError:
                            print("invalid Credentials")
                            continue
                    kfcmenuprice.remove(removeprice)
                    print(kfcmenu)
                    print(kfcmenuprice)

# ranchers starts from here.
    elif name==3:
        while True:
            name = "RANCHERS"
            password = "1234"
            print("Login")
            restaurant_name = str(input("Enter the restaurant ID : ")).upper()
            restaurant_password = str(input("Enter your password : "))
            if restaurant_name == name and restaurant_password == password:
                print("You have logged in")
                break
            else:
                print("invalid credentials")
        while True:
            while True:
                try:
                    options = int(input('''
                    Press [1] to view your menu.
                    Press [2] to edit your menu.
                    Press [3] to exit.\n
                    '''))

                    if 0 < options < 4:
                        break
                except ValueError:
                    print("invalid credentials")
                    continue
            if options == 3:
                break
            elif options == 1:
                print('''
                [1]Krunch                                 Rs;200'
                [2]Zinger                                 Rs;400'
                [3]Mighty                                 Rs;550'
                [4]Rice                                   Rs;250'
                [5]Salad                                  Rs;50'
                [6]Wings                                  Rs;350'
                [7]Drink                                  Rs;70''')
            elif options == 2:
                print('''What changes do you want to make in current menu?
                 [1]Krunch                                Rs;200'
                 [2]Zinger                                Rs;400'
                 [3]Mighty                                Rs;550'
                 [4]Rice                                  Rs;250'
                 [5]Salad                                 Rs;50'
                 [6]Wings                                 Rs;350'
                 [7]Drink                                 Rs;70
                ''')
                while True:
                    try:
                        edit = int(input('''Press
                        [1] To add items
                        [2] To remove items
                        [3] To exit\n'''))
                        if 0 < edit < 4:
                            break
                    except ValueError:
                        print("invalid credentials")
                        continue

                if edit == 3:
                    break
                elif edit == 1:
                    item = str(input('Enter the item you want to add:'))
                    ranchersmenu.append(item)
                    while True:
                        try:
                            price = int(input("Enter the price for the item you have added:"))
                            break
                        except ValueError:
                            print("Invalid credentials")
                    ranchersmenuprice.append(price)
                    print("Your item", item, 'is added for the price', price)
                    print(ranchersmenu)
                    print(ranchersmenuprice)

                else:
                    print('''
                     [1]Krunch                                Rs;200'
                     [2]Zinger                                Rs;400'
                     [3]Mighty                                Rs;550'
                     [4]Rice                                  Rs;250'
                     [5]Salad                                 Rs;50'
                     [6]Wings                                 Rs;350'
                     [7]Drink                                 Rs;70''')
                    while True:
                        try:
                            remove1 = int(input("Enter the number of item you want to remove?"))
                            break
                        except ValueError:
                            print("Invalid Credentials")
                            continue
                    remove1 -= 1
                    ranchersmenu.remove(ranchersmenu[remove1])
                    print('''
                    [1]Krunch                                 Rs;200
                    [2]Zinger                                 Rs;400
                    [3]Hot wings                              Rs;550
                    [4]Rice                                   Rs;250
                    [5]Pizza                                  Rs;1050
                    [6]Boneless                               Rs;350
                    [7]Drink                                  Rs;70''')
                    while True:
                        try:
                            removeprice = int(input("Enter the price of the item you have removed."))
                            break
                        except ValueError:
                            print("invalid Credentials")
                            continue
                    ranchersmenuprice.remove(removeprice)
                    print(ranchersmenu)
                    print(ranchersmenuprice)



    else:
        print('Enter the correct option.')


def ranchers():
    print("WELCOME TO THE RANCHERS\n-----------------------\n")

    menu_array = ['[1]Krunch                                 Rs;200',
                  '[2]Zinger                                 Rs;400',
                  '[3]Mighty                                 Rs;550',
                  '[4]Rice                                   Rs;250',
                  '[5]Salad                                  Rs;50',
                  '[6]Wings                                  Rs;350',
                  '[7]Drink                                  Rs;70']

    menu_list = ['krunch', 'zinger', 'mighty', 'rice', 'salad', 'wings', 'drink']
    payment_status = ""
    menu_price = [
        200,
        400,
        550,
        250,
        50,
        350,
        70]

    spaces = 25

    receipt = "RANCHERS".center(75) + "\n---------------------------------------------------------------------------\n" \
              + "|Product|".ljust(spaces) + "|Quantity|".center(spaces) + "|price|".rjust(spaces) + \
              "\n---------------------------------------------------------------------------\n"

    total_price = 0



    print("What would you like to eat today " + customer_name)
    print("Here's the menu\n-----------------------\n")

    for items in menu_array:
        print(items)
    print("\n-----------------------\n")

    while True:

        while True: #this while loop is used for exception.
            try:
                order_number = int(input("Select with respect to number"))
                if 0 < order_number < 8:
                    break
            except ValueError:
                print('''Please enter correct order number"

                      ''')
                continue
        order_number -= 1
        order_name = menu_list[order_number]
        food_price = menu_price[order_number]
        while True:
            try:
                order_quantity = int(input("How many "+order_name+" you want to add"))
                break
            except ValueError:
                print('''Please enter correct  number"

                      ''')
                continue
        order_price = order_quantity * food_price
        total_price += order_price
        receipt += order_name.upper().ljust(spaces) + str(order_quantity).center(spaces) + str(order_price).rjust(
            spaces) + "\n"

        print(f"{order_quantity} {order_name.upper()} has been added\n-----------------------\n")
        print(f"{order_price}  is your bill for {order_quantity} {order_name.upper()}\n-----------------------\n")

        while True:
            more_order = input("Do you want to add more " + customer_name + "\n"
                                                                            "Type YES for more order\n"
                                                                            "NO for payment\n"
                                                                            "-----------------------\n").upper()

            if more_order.upper() == "YES" or more_order == "NO":
                break
            else:
                print("Please enter the valid response\n-----------------------\n")

        if more_order == "NO":
            break

    print("You have completed your order")
    print(f"{customer_name} Your total price  for this order is {total_price}\n-----------------------\n")
    print("Enter your delivery address\n-----------------------")
    address = input()

    check = True
    while check:
        while True: #this while is used for payment.
            try:
                payment_method = int(input("Which method do you want to choose\n-----------------------\n"
                                           "Press 1 for Credit Card Payment\n"
                                           "Press 2 for Cash on delivery\n-----------------------\n"))
                if payment_method == 1 or payment_method == 2:
                    break
            except ValueError:

                print("Please enter the valid payment method\n")
                continue


        if payment_method == 1:
            print("Enter your card credentials")

            for i in range(1, 4, 1):
                card_no = input("Enter the card number(13 digit only)\n-----------------------\n")
                if len(card_no) == 13:
                    print("Payment Approved\n-----------------------\n")
                    payment_status = "Paid"
                    check = False
                    break

                else:
                    print("Credentials not True")
                    if i == 3:
                        print("You've entered wrong credentials\n"
                              "Card attempt limit exceeded!\n"
                              "Re-enter payment method\n-----------------------\n")

        else:
            print(f"Our rider will collect Rs {total_price}at the time of delivery\n-----------------------\n")
            payment_status = "Pending"
            check = False

    review = "INVALID"


    while True:
        try:

            stars = int(input("How was your experience\n"
                              "Describe in 1 to 5 Numbers\n-----------------------\n"))
            if 0 < stars < 6:
                review = rating(stars)
                break
        except ValueError:
            print("Please enter the valid response")

    GST = tax(total_price)
    total_price += GST

    receipt += "---------------------------------------------------------------------------\n"
    receipt += "GST : ".ljust(spaces) + "".center(spaces) + str(GST).rjust(spaces) + '\n'
    receipt += "TOTAL BILL : ".ljust(spaces) + "".center(spaces) + str(total_price).rjust(spaces) + '\n'
    receipt += "Payment Status : ".ljust(spaces) + "".center(spaces) + payment_status.rjust(spaces) + '\n'
    receipt += "Rating : ".ljust(spaces) + "".center(spaces) + review.rjust(spaces) + '\n'
    receipt += "Street Address : " + str(address) + '\n'
    print(f"Here's your receipt {customer_name}\n"
          f"---------------------------------------------------------------------------\n"
          f"\n\n"
          f" {receipt}\n"
          f"---------------------------------------------------------------------------\n"
          f"Thank You for ordering  {customer_name} your order will be delivered in 25 mins"
          f"\n---------------------------------------------------------------------------\n")


def mcdonalds():
    print("WELCOME TO THE MCDONALDS PAKISTAN\n-----------------------\n")

    menu_array = ['[1]Zinger burger                             Rs;550',
                  '[2]Happy meal                                  Rs;700',
                  '[3]Fries                                       Rs;200',
                  '[4]Wraps                                       Rs;320',
                  '[5]Tiramisu Cake                               Rs;500',
                  '[6]Coffee                                      Rs;120',
                  '[7]Drink                                       Rs;70']

    menu_list = ['Zinger burger', 'Happy meal', 'Fries', 'Wraps', 'Tiramisu Cake', 'Coffee', 'Drink']
    payment_status = ""
    menu_price = [
        550,
        700,
        200,
        320,
        500,
        120,
        70]

    spaces = 25

    receipt = "MCDONALDS PAKISTAN".center(
        75) + "\n---------------------------------------------------------------------------\n" \
              + "|Product|".ljust(spaces) + "|Quantity|".center(spaces) + "|price|".rjust(spaces) + \
              "\n---------------------------------------------------------------------------\n"

    total_price = 0



    print("What would you like to eat today " + customer_name)
    print("Here's the menu\n-----------------------\n")

    for items in menu_array:
        print(items)
    print("\n-----------------------\n")

    while True:

        while True:
            try:
                order_number = int(input("Select with respect to number"))
                if 0 < order_number < 8:
                    break
            except ValueError:
                print('''Please enter correct order number"

                      ''')
                continue
        order_number -= 1
        order_name = menu_list[order_number]
        food_price = menu_price[order_number]
        while True:
            try:
                order_quantity = int(input("How many " + order_name + " you want to add"))
                break
            except ValueError:
                print('''Please enter correct  number"

                      ''')
                continue
        order_price = order_quantity * food_price
        total_price += order_price
        receipt += order_name.upper().ljust(spaces) + str(order_quantity).center(spaces) + str(order_price).rjust(
            spaces) + "\n"

        print(f"{order_quantity} {order_name.upper()} has been added\n-----------------------\n")
        print(f"{order_price}  is your bill for {order_quantity} {order_name.upper()}\n-----------------------\n")

        while True:
            more_order = input("Do you want to add more " + customer_name + "\n"
                                                                            "Type YES for more order\n"
                                                                            "NO for payment\n"
                                                                            "-----------------------\n").upper()

            if more_order.upper() == "YES" or more_order == "NO":
                break
            else:
                print("Please enter the valid response\n-----------------------\n")

        if more_order == "NO":
            break

    print("You have completed your order")
    print(f"{customer_name} Your total price  for this order is {total_price}\n-----------------------\n")
    print("Enter your delivery address\n-----------------------")
    address = input()

    check = True
    while check:
        while True:
            try:
                payment_method = int(input("Which method do you want to choose\n-----------------------\n"
                                           "Press 1 for Credit Card Payment\n"
                                           "Press 2 for Cash on delivery\n-----------------------\n"))
                if payment_method == 1 or payment_method == 2:
                    break
            except ValueError:

                print("Please enter the valid payment method\n")
                continue

        if payment_method == 1:
            print("Enter your card credentials")

            for i in range(1, 4, 1):
                card_no = input("Enter the card number(13 digit only)\n-----------------------\n")
                if len(card_no) == 13:
                    print("Payment Approved\n-----------------------\n")
                    payment_status = "Paid"
                    check = False
                    break

                else:
                    print("Credentials not True")
                    if i == 3:
                        print("You've entered wrong credentials\n"
                              "Card attempt limit exceeded!\n"
                              "Re-enter payment method\n-----------------------\n")

        else:
            print(f"Our rider will collect Rs {total_price} at the time of delivery.\n-----------------------\n")
            payment_status = "Pending"
            check = False

    review = "INVALID"


    while True:
        try:

            stars = int(input("How was your experience\n"
                              "Describe in 1 to 5 Numbers\n-----------------------\n"))
            if 0 < stars < 6:
                review = rating(stars)
                break
        except ValueError:
            print("Please enter the valid response")

    GST = tax(total_price)
    total_price += GST

    receipt += "---------------------------------------------------------------------------\n"
    receipt += "GST : ".ljust(spaces) + "".center(spaces) + str(GST).rjust(spaces) + '\n'
    receipt += "TOTAL BILL : ".ljust(spaces) + "".center(spaces) + str(total_price).rjust(spaces) + '\n'
    receipt += "Payment Status : ".ljust(spaces) + "".center(spaces) + payment_status.rjust(spaces) + '\n'
    receipt += "Rating : ".ljust(spaces) + "".center(spaces) + review.rjust(spaces) + '\n'
    receipt += "Street Address : " + str(address) + '\n'

    print(f"Here's your receipt {customer_name}\n"
          f"---------------------------------------------------------------------------\n"
          f"\n\n"
          f" {receipt}\n"
          f"---------------------------------------------------------------------------\n"
          f"Thank You for ordering  {customer_name} your order will be delivered in 25 mins"
          f"\n---------------------------------------------------------------------------\n")


def kfc():
    print("WELCOME TO THE KFC\n-----------------------\n")

    menu_array = ['[1]Krunch                             Rs;200',
                  '[2]Zinger                                 Rs;400',
                  '[3]Hot wings                              Rs;550',
                  '[4]Rice                                   Rs;250',
                  '[5]Pizza                                  Rs;1050',
                  '[6]Boneless Chicken                       Rs;350',
                  '[7]Drink                                  Rs;70']

    menu_list = ['Krunch', 'Zinger', 'Hot wings', 'Rice', 'Pizza', 'Boneless Chicken', 'Drink']
    payment_status = ""
    menu_price = [
        200,
        400,
        550,
        250,
        1050,
        350,
        70]

    spaces = 25

    receipt = "KFC".center(75) + "\n---------------------------------------------------------------------------\n" \
              + "|Product|".ljust(spaces) + "|Quantity|".center(spaces) + "|price|".rjust(spaces) + \
              "\n---------------------------------------------------------------------------\n"

    total_price = 0



    print("What would you like to eat today " + customer_name)
    print("Here's the menu\n-----------------------\n")

    for items in menu_array:
        print(items)
    print("\n-----------------------\n")

    while True:
        while True:
            try:
                order_number = int(input("Select with respect to number"))
                if 0 < order_number < 8:
                    break
            except ValueError:
                print('''Please enter correct order number"
                      
                      ''')
                continue
        order_number -= 1
        order_name = menu_list[order_number]
        food_price = menu_price[order_number]
        while True:
            try:
                order_quantity = int(input("How many " + order_name + " you want to add"))
                break
            except ValueError:
                print('''Please enter correct  number"

                      ''')
                continue
        order_price = order_quantity * food_price
        total_price += order_price
        receipt += order_name.upper().ljust(spaces) + str(order_quantity).center(spaces) + str(order_price).rjust(
            spaces) + "\n"

        print(f"{order_quantity} {order_name.upper()} has been added\n-----------------------\n")
        print(f"{order_price}  is your bill for {order_quantity} {order_name.upper()}\n-----------------------\n")

        while True:
            more_order = input("Do you want to add more " + customer_name + "\n"
                                                                            "Type YES for more order\n"
                                                                            "NO for payment\n"
                                                                            "-----------------------\n").upper()

            if more_order.upper() == "YES" or more_order == "NO":
                break
            else:
                print("Please enter the valid response\n-----------------------\n")

        if more_order == "NO":
            break

    print("You have completed your order")
    print(f"{customer_name} Your total price  for this order is {total_price}\n-----------------------\n")
    print("Enter your delivery address\n-----------------------")
    address = input()

    check = True
    while check:
        while True:
            try:
                payment_method = int(input("Which method do you want to choose\n-----------------------\n"
                                           "Press 1 for Credit Card Payment\n"
                                           "Press 2 for Cash on delivery\n-----------------------\n"))
                if payment_method == 1 or payment_method == 2:
                    break
            except ValueError:

                print("Please enter the valid payment method\n")
                continue


        if payment_method == 1:
            print("Enter your card credentials")

            for i in range(1, 4, 1):
                card_no = input("Enter the card number(13 digit only)\n-----------------------\n")
                if len(card_no) == 13:
                    print("Payment Approved\n-----------------------\n")
                    payment_status = "Paid"
                    check = False
                    break

                else:
                    print("Credentials not True")
                    if i == 3:
                        print("You've entered wrong credentials\n"
                              "Card attempt limit exceeded!\n"
                              "Re-enter payment method\n-----------------------\n")

        else:
            print(f"Our rider will collect Rs {total_price} at the time of delivery.\n-----------------------\n")
            payment_status = "Pending"
            check = False

    review = "INVALID"


    while True:
        try:

            stars = int(input("How was your experience\n"
                              "Describe in 1 to 5 Numbers\n-----------------------\n"))
            if 0 < stars < 6:
                review = rating(stars)
                break
        except ValueError:
            print("Please enter the valid response")

    GST = tax(total_price)
    total_price += GST

    receipt += "---------------------------------------------------------------------------\n"
    receipt += "GST : ".ljust(spaces) + "".center(spaces) + str(GST).rjust(spaces) + '\n'
    receipt += "TOTAL BILL : ".ljust(spaces) + "".center(spaces) + str(total_price).rjust(spaces) + '\n'
    receipt += "Payment Status : ".ljust(spaces) + "".center(spaces) + payment_status.rjust(spaces) + '\n'
    receipt += "Rating : ".ljust(spaces) + "".center(spaces) + review.rjust(spaces) + '\n'
    receipt += "Street Address : " + str(address) + '\n'

    print(f"Here's your receipt {customer_name}\n"
          f"---------------------------------------------------------------------------\n"
          f"\n\n"
          f" {receipt}\n"
          f"---------------------------------------------------------------------------\n"
          f"Thank you for ordering {customer_name} your order will be delivered in 25 mins"
          f"\n---------------------------------------------------------------------------\n")


print(""" 

 |==========================================| 
       == Welcome To Food Panda	==
 |==========================================|
 
""")

print("----------------------------\n"
    "[1]Customer\n"
    "[2]Restaurant owner\n"
      "----------------------------\n")
person = ['[1]Customer',
          '[2]Restaurant owner',
          ]
while True:
    while True:
        try:
            number = int(input("Enter an above mentioned number: "))
            if number ==1 or number ==2:
                 break
        except ValueError:
            print("Please input above mentioned number only...")
            continue

    # print(person_name)
    if number == 1:
        print("Login")
        customer_name = str(input("Enter Your Name : ")).upper()
        customer_password = str(input("Set up a password : "))
        print("You have logged in")



        customer()
        while True:
            x = input("Enter YES to order from another restaurant\n"
                      "Enter NO to exit").upper()
            if x == "YES":
                customer()

            else:
                break
        break #this break statement is for upper while loop.



    else:
        restaurant_owner()
        break
