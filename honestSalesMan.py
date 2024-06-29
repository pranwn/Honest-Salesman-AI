# Product information
products = {
    'laptop': {
        'description': 'A high-performance laptop with 16GB RAM and 512GB SSD. Perfect for gaming, video editing, and heavy-duty tasks!',
        'price': 1200,
        'stock': 5,
        'color': '\033[94m',  # Blue
        'advice': 'If you\'re a heavy user, this laptop is a great investment!',
        'average_money_range': 1000,
        'category': 'computer'
    },
    'phone': {
        'description': 'A smartphone with a great camera and long battery life. Capture life\'s precious moments with crystal-clear clarity!',
        'price': 800,
        'stock': 10,
        'color': '\033[92m',  # Green
        'advice': 'If you\'re due for an upgrade, this phone is a great choice!',
        'average_money_range': 500,
        'category': 'phone'
    },
    'headphones': {
        'description': 'Noise-cancelling headphones with superior sound quality. Immerse yourself in pure audio bliss!',
        'price': 150,
        'stock': 20,
        'color': '\033[93m',  # Yellow
        'advice': 'If you love music, these headphones are a must-have!',
        'average_money_range': 100,
        'category': 'accessory'
    },
    'tablet': {
        'description': 'A sleek and powerful tablet perfect for reading, browsing, and streaming your favorite content!',
        'price': 500,
        'stock': 15,
        'color': '\033[94m',  # Blue
        'advice': 'If you want a portable entertainment device, this tablet is a great option!',
        'average_money_range': 300,
        'category': 'computer'
    },
    'smartwatch': {
        'description': 'A stylish smartwatch that tracks your fitness goals and keeps you connected on-the-go!',
        'price': 200,
        'stock': 12,
        'color': '\033[95m',  # Magenta
        'advice': 'If you\'re into fitness, this smartwatch is a great motivator!',
        'average_money_range': 150,
        'category': 'accessory'
    },
    'gamingconsole': {
        'description': 'A powerful gaming console with stunning graphics and immersive gameplay. Get ready to level up!',
        'price': 300,
        'stock': 8,
        'color': '\033[91m',  # Red
        'advice': 'If you\'re a gamer, this console is a must-have!',
        'average_money_range': 200,
        'category': 'gaming'
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
        if account_balance < products[user_input]['average_money_range']:
            print(f"\033[91mSorry, this product is out ofyour budget. You need at least ${products[user_input]['average_money_range']} to buy this product.\033[0m\n")
            continue

        have_product = input("Do you already have this product? (yes/no) ").strip().lower()
        if have_product == 'yes':
            product_age = input("Is your current product old or new? (old/new) ").strip().lower()
            if product_age == 'old':
                print(f"\033[92mWe recommend buying a new {user_input} since your current one is old.\033[0m")
            else:
                print(f"\033[91mYou already have a new {user_input}, no need to buy another one.\033[0m\n")
                continue

        quantity = int(input("How many would you like to buy? "))
        if products[user_input]['stock'] >= quantity:
            total_price = products[user_input]['price'] * quantity
            if total_price > account_balance:
                print(f"\033[91mSorry, you don't have enough money in your account to buy {quantity} {user_input}(s).\033[0m\n")
                continue
            products[user_input]['stock'] -= quantity
            print(f"\033[92mCongratulations, you've purchased {quantity} {user_input}(s)!\033[0m")
            print(f"Total cost: ${total_price}\n")
        else:
            print(f"\033[91mSorry, we only have {products[user_input]['stock']} {user_input}(s) in stock.\033[0m\n")
    else:
        print("\033[91mInvalid action. Please use 'info' or 'buy'.\033[0m\n")