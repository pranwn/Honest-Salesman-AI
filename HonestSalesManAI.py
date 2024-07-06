# Product information
products = {
    'laptop': {
        'description': 'A high-performance laptop with 16GB RAM and 512GB SSD. Perfect for gaming, video editing, and heavy-duty tasks!',
        'price': 1200,
        'tock': 5,
        'color': '\033[94m',  # Blue
        'advice': 'If you\'re a heavy user, this laptop is a great investment!',
        'average_money_range': 1000,
        'category': 'computer',
        'ubgenres': {
            'Samsung': 1000,
            'Microsoft': 1100,
            'Apple': 1300
        }
    },
    'phone': {
        'description': 'A smartphone with a great camera and long battery life. Capture life\'s precious moments with crystal-clear clarity!',
        'price': 800,
        'tock': 10,
        'color': '\033[92m',  # Green
        'advice': 'If you\'re due for an upgrade, this phone is a great choice!',
        'average_money_range': 500,
        'category': 'phone',
        'ubgenres': {
            'Samsung': 700,
            'Apple': 800,
            'Google': 600
        }
    },
    'headphones': {
        'description': 'Noise-cancelling headphones with superior sound quality. Immerse yourself in pure audio bliss!',
        'price': 150,
        'tock': 20,
        'color': '\033[93m',  # Yellow
        'advice': 'If you love music, these headphones are a must-have!',
        'average_money_range': 100,
        'category': 'accessory',
        'ubgenres': {
            'Sony': 120,
            'Bose': 150,
            'Beats': 100
        }
    },
    'tablet': {
        'description': 'A sleek and powerful tablet perfect for reading, browsing, and streaming your favorite content!',
        'price': 500,
        'tock': 15,
        'color': '\033[94m',  # Blue
        'advice': 'If you want a portable entertainment device, this tablet is a great option!',
        'average_money_range': 300,
        'category': 'computer',
        'ubgenres': {
            'Apple': 500,
            'Samsung': 400,
            'Amazon': 300
        }
    },
    'martwatch': {
        'description': 'A stylish smartwatch that tracks your fitness goals and keeps you connected on-the-go!',
        'price': 200,
        'tock': 12,
        'color': '\033[95m',  # Magenta
        'advice': 'If you\'re into fitness, this smartwatch is a great motivator!',
        'average_money_range': 150,
        'category': 'accessory',
        'ubgenres': {
            'Apple': 250,
            'Samsung': 200,
            'Fitbit': 150
        }
    },
    'gamingconsole': {
        'description': 'A powerful gaming console with stunning graphics and immersive gameplay. Get ready to level up!',
        'price': 300,
        'tock': 8,
        'color': '\033[91m',  # Red
        'advice': 'If you\'re a gamer, this console is a must-have!',
        'average_money_range': 200,
        'category': 'gaming',
        'ubgenres': {
            'PlayStation': 300,
            'Xbox': 250,
            'Nintendo': 200
        }
    }
}

# Welcome message
print("\033[92mWelcome to TechTopia, your one-stop shop for all things tech!\033[0m")
print("We have the following items available:")
for product in products:
    print(f"  - {products[product]['color']}{product.capitalize()}\033[0m")
print("Type 'exit' to quit, or ask me about a product!")

while True:
    user_input = input("\nWhat product are you interested in? ").strip().lower()

    if user_input == 'exit':
        print("\033[92mThanks for shopping at TechTopia! Come back soon!\033[0m")
        break

    if user_input not in products:
        print("\033[91mSorry, we don't have that product.\033[0m\n")
        continue

    print(f"\n{products[user_input]['color']}{user_input.capitalize()} Info:\033[0m")
    print(f"Description: {products[user_input]['description']}")
    print(f"Price: ${products[user_input]['price']}")
   print(f"Stock: {products[user_input]['stock']}")
    print(f"Advice: {products[user_input]['advice']}\n")

    action = input("Would you like to 'info' or 'buy' this product? ").strip().lower()

    if action == 'info':
        print(f"\n{products[user_input]['color']}{user_input.capitalize()} Info:\033[0m")
        print(f"Description: {products[user_input]['description']}")
        print(f"Price: ${products[user_input]['price']}")
        print(f"Stock: {products[user_input]['stock']}\n")
    elif action == 'buy':
        account_balance = int(input("How much money do you have in your account? "))
        if account_balance < 50:
            print("\033[91mYou're making an impulse buy! Are you sure you want to proceed?\033[0m")
            confirm = input("Type 'yes' to confirm, or 'no' to cancel: ").strip().lower()
            if confirm!= 'yes':
                continue

        have_product = input("Do you already have this product? (yes/no) ").strip().lower()
        if have_product == 'yes':
            product_age = input("Is your current product old or new? (old/new) ").strip().lower()
            if product_age == 'old':
                print(f"\033[92mWe recommend buying a new {user_input} since your current one is old.\033[0m")
            else:
                print(f"\033[91mYou already have a new {user_input}, no need to buy another one.\033[0m\n")
                continue

        subgenre = input("Which brand would you like? (type 'list' to see options) ").strip().lower()
        if subgenre == 'list':
            print("Available brands:")
            for brand in products[user_input]['subgenres']:
                print(f"  - {brand}")
            subgenre = input("Which brand would you like? ").strip().lower()

        if subgenre not in products[user_input]['subgenres']:
            print(f"\033[91mSorry, we don't have {subgenre} {user_input}(s).\033[0m\n")
            continue

        quantity = int(input("How many would you like to buy? "))
        if products[user_input]['stock'] >= quantity:
            total_price = products[user_input]['subgenres'][subgenre] * quantity
            if total_price > account_balance:
                print(f"\033[91mSorry, you don't have enough money in your account to buy {quantity} {subgenre} {user_input}(s).\033[0m\n")
                continue
            products[user_input]['stock'] -= quantity
            print(f"\033[92mCongratulations, you've purchased {quantity} {subgenre} {user_input}(s)!\033[0m")
            print(f"Total cost: ${total_price}\n")
            website = input("Would you like to know where to find the best price for this product? (yes/no) ").strip().lower()
            if website == 'yes':
                if subgenre == 'Samsung':
                    print("You can find the best price for Samsung products on Amazon.")
                elif subgenre == 'Apple':
                    print("You can find the best price for Apple products on Apple's official website.")
                elif subgenre == 'Microsoft':
                    print("You can find the best price for Microsoft products on Best Buy.")
                else:
                    print("You can find the best price for this product on various online marketplaces.")
        else:
            print(f"\033[91mSorry, we only have {products[user_input]['stock']} {user_input}(s) in stock.\033[0m\n")
    else:
        print("\033[91mInvalid action. Please use 'info' or 'buy'.\033[0m\n")----->MAKE SURE THE ITEM ISNT A INPULSE SPEND IF THEY HAVE LESS THAN 50 DOLLARS CONSIDER IT A INPULSE BUY. ALSO ADD SUBGENRES UNDER EACH CATAGORY(EX. A LAPTOP HAS MULTIPLE DIFFERENT BRANDS LIKE SAMSUNG, MICROSOFT, APPLE) AND GIVE THEIR PRICE POINTS , THEN RECOMMEND THEM AN ITEM BASED ON THEIR PRICE POINT AND WHICH WEBSITE THEY CAN GO TO FIND THE BEST PRICE FOR THAT PRODUCT. ASK THEM QUESTIONS TO DETERMINE WHICH BRAND IS BEST SUITED TO THEIR PREFRENCES[/
    else:
        print("\033[91mInvalid action. Please use 'info' or 'buy'.\033[0m\n")

    if user_input == 'laptop':
        print("What is your budget for the laptop?")
        budget = int(input("Enter a number: "))
        if budget < 500:
            print("Based on your budget, we recommend the Samsung laptop.")
        elif budget < 1000:
            print("Based on your budget, we recommend the Microsoft laptop.")
        else:
            print("Based on your budget, we recommend the Apple laptop.")

        print("Do you need a laptop for gaming, video editing, or general use?")
        use_case = input("Enter 'gaming', 'video editing', or 'general use': ")
        if use_case == 'gaming':
            print("Based on your use case, we recommend the Samsung laptop.")
        elif use_case == 'video editing':
            print("Based on your use case, we recommend the Apple laptop.")
        else:
            print("Based on your use case, we recommend the Microsoft laptop.")

    elif user_input == 'phone':
        print("What is your budget for the phone?")
        budget = int(input("Enter a number: "))
        if budget < 300:
            print("Based on your budget, we recommend the Samsung phone.")
        elif budget < 600:
            print("Based on your budget, we recommend the Apple phone.")
        else:
            print("Based on your budget, we recommend the Google phone.")

        print("Do you need a phone with a good camera, long battery life, or water resistance?")
        feature = input("Enter 'camera', 'battery life', or 'water resistance': ")
        if feature == 'camera':
            print("Based on your feature preference, we recommend the Samsung phone.")
        elif feature == 'battery life':
            print("Based on your feature preference, we recommend the Apple phone.")
        else:
            print("Based on your feature preference, we recommend the Google phone.")

    elif user_input == 'headphones':
        print("What is your budget for the headphones?")
        budget = int(input("Enter a number: "))
        if budget < 100:
            print("Based on your budget, we recommend the Beats headphones.")
        elif budget < 200:
            print("Based on your budget, we recommend the Sony headphones.")
        else:
            print("Based on your budget, we recommend the Bose headphones.")

        print("Do you need headphones for music, gaming, or exercise?")
        use_case = input("Enter 'music', 'gaming', or 'exercise': ")
        if use_case == 'music':
            print("Based on your use case, we recommend the Sony headphones.")
        elif use_case == 'gaming':
            print("Based on your use case, we recommend the Bose headphones.")
        else:
            print("Based on your use case, we recommend the Beats headphones.")

    elif user_input == 'tablet':
        print("What is your budget for the tablet?")
        budget = int(input("Enter a number: "))
        if budget < 200:
            print("Based on your budget, we recommend the Amazon tablet.")
        elif budget < 400:
            print("Based on your budget, we recommend the Samsung tablet.")
        else:
            print("Based on your budget, we recommend the Apple tablet.")

        print("Do you need a tablet for reading, browsing, or gaming?")
        use_case = input("Enter 'reading', 'browsing', or 'gaming': ")
        if use_case == 'reading':
            print("Based on your use case, we recommend the Amazon tablet.")
        elif use_case == 'browsing':
            print("Based on your use case, we recommend the Samsung tablet.")
        else:
            print("Based on your use case, we recommend the Apple tablet.")

    elif user_input == 'smartwatch':
        print("What is your budget for the smartwatch?")
        budget = int(input("Enter a number: "))
        if budget < 150:
            print("Based on your budget, we recommend the Fitbit smartwatch.")
        elif budget < 300:
            print("Based on your budget, we recommend the Samsung smartwatch.")
        else:
            print("Based on your budget, we recommend the Apple smartwatch.")

        print("Do you need a smartwatch for fitness, notifications, or music control?")
        use_case = input("Enter 'fitness', 'notifications', or 'music control': ")
        if use_case == 'fitness':
            print("Based on your use case, we recommend the Fitbit smartwatch.")
        elif use_case == 'notifications':
            print("Based on your use case, we recommend the Samsung smartwatch.")
        else:
            print("Based on your use case, we recommend the Apple smartwatch.")

    elif user_input == 'gamingconsole':
        print("What is your budget for the gaming console?")
        budget = int(input("Enter a number: "))
        if budget < 200:
            print("Based on your budget, we recommend the Nintendo gaming console.")
        elif budget < 300:
            print("Based on your budget, we recommend the Xbox gaming console.")
        else:
            print("Based on your budget, we recommend the PlayStation gaming console.")

        print("Do you need a gaming console for exclusive games, online multiplayer, or VR capabilities?")
        use_case = input("Enter 'exclusive games', 'online multiplayer', or 'VR capabilities': ")
        if use_case == 'exclusive games':
            print("Based on your use case, we recommend the Nintendo gaming console.")
        elif use_case == 'online multiplayer':
            print("Based on your use case, we recommend the Xbox gaming console.")
        else:
            print("Based on your use case, we recommend the PlayStation gaming console.")


            