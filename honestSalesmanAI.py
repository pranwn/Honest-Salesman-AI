# Product information
products = {
    'laptop': {
        'description': 'A high-performance laptop with 16GB RAM and 512GB SSD. Perfect for gaming, video editing, and heavy-duty tasks!',
        'price': 1200,
        'stock': 5,
        'color': '\033[94m',  # Blue
        'advice': 'If you\'re a heavy user, this laptop is a great investment!'
    },
    'phone': {
        'description': 'A smartphone with a great camera and long battery life. Capture life\'s precious moments with crystal-clear clarity!',
        'price': 800,
        'stock': 10,
        'color': '\033[92m',  # Green
        'advice': 'If you\'re due for an upgrade, this phone is a great choice!'
    },
    'headphones': {
        'description': 'Noise-cancelling headphones with superior sound quality. Immerse yourself in pure audio bliss!',
        'price': 150,
        'stock': 20,
        'color': '\033[93m',  # Yellow
        'advice': 'If you love music, these headphones are a must-have!'
    },
    'tablet': {
        'description': 'A sleek and powerful tablet perfect for reading, browsing, and streaming your favorite content!',
        'price': 500,
        'stock': 15,
        'color': '\033[94m',  # Blue
        'advice': 'If you want a portable entertainment device, this tablet is a great option!'
    },
    'smartwatch': {
        'description': 'A stylish smartwatch that tracks your fitness goals and keeps you connected on-the-go!',
        'price': 200,
        'stock': 12,
        'color': '\033[95m',  # Magenta
        'advice': 'If you\'re into fitness, this smartwatch is a great motivator!'
    },
    'gamingconsole': {
        'description': 'A powerful gaming console with stunning graphics and immersive gameplay. Get ready to level up!',
        'price': 300,
        'stock': 8,
        'color': '\033[91m',  # Red
        'advice': 'If you\'re a gamer, this console is a must-have!'
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
        quantity = int(input("How many would you like to buy? "))
        if products[user_input]['stock'] >= quantity:
            total_price = products[user_input]['price'] * quantity
            products[user_input]['stock'] -= quantity
            print(f"\033[92mCongratulations, you've purchased {quantity} {user_input}(s)!\033[0m")
            print(f"Total cost: ${total_price}\n")
        else:
            print(f"\033[91mSorry, we only have {products[user_input]['stock']} {user_input}(s) in stock.\033[0m\n")
    else:
        print("\033[91mInvalid action. Please use 'info' or 'buy'.\033[0m\n")