import openai
import pandas as pd

openai.api_key = 'YOUR_OPENAI_API_KEY'

def load_purchase_data(filepath):
    data = pd.read_csv(filepath)
    data['Order_Date'] = pd.to_datetime(data['Order Date'])
    data['Month'] = data['Order_Date'].dt.to_period('M')
    return data

def spending_analysis(data):
    total_spent = data['Item Total'].sum()
    monthly_expenses = data.groupby('Month')['Item Total'].sum()
    return total_spent, monthly_expenses

def detect_impulse_purchases(data):
    data['Quick_Purchase'] = data['Time to Purchase'].apply(lambda t: t < pd.Timedelta(minutes=10))
    quick_buys = data[data['Quick_Purchase']]
    return quick_buys

def summarize_insights(data):
    total_spent, monthly_expenses = spending_analysis(data)
    quick_buys = detect_impulse_purchases(data)
    return {
        "total_spent": total_spent,
        "monthly_expenses": monthly_expenses,
        "quick_buys": quick_buys
    }

def fetch_openai_response(prompt_text):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt_text,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def ai_assistant(filepath, question):
    data = load_purchase_data(filepath)
    insights = summarize_insights(data)
    
    # Formulate prompt for AI response
    prompt = f"""
    You are an AI assistant analyzing Amazon purchase data for a user. Below are their spending insights:

    Total spent: ${insights['total_spent']}

    Monthly spending:
    {insights['monthly_expenses']}

    Impulse purchases:
    {insights['quick_buys']}
    
    The user asks: "{question}"
    Provide personalized advice based on the data.
    """
    
    response = fetch_openai_response(prompt)
    return response

# Example usage
filepath = 'amazon_order_history.csv'
user_question = "Is it a good idea to buy a new laptop now?"
response = ai_assistant(filepath, user_question)
print(response)

products = {
    'laptop': {
        'description': 'A high-performance laptop with 16GB RAM and 512GB SSD. Perfect for gaming, video editing, and heavy-duty tasks!',
        'price': 1200,
        'stock': 5,
        'color': '\033[94m',  # Blue
        'advice': 'If you\'re a heavy user, this laptop is a great investment!',
        'average_money_range': 1000,
        'category': 'computer',
        'subgenres': {
            'Samsung': 1000,
            'Microsoft': 1100,
            'Apple': 1300
        }
    },
    'phone': {
        'description': 'A smartphone with a great camera and long battery life. Capture life\'s precious moments with crystal-clear clarity!',
        'price': 800,
        'stock': 10,
        'color': '\033[92m',  # Green
        'advice': 'If you\'re due for an upgrade, this phone is a great choice!',
        'average_money_range': 500,
        'category': 'phone',
        'subgenres': {
            'Samsung': 700,
            'Apple': 800,
            'Google': 600
        }
    },
    'headphones': {
        'description': 'Noise-cancelling headphones with superior sound quality. Immerse yourself in pure audio bliss!',
        'price': 150,
        'stock': 20,
        'color': '\033[93m',  # Yellow
        'advice': 'If you love music, these headphones are a must-have!',
        'average_money_range': 100,
        'category': 'accessory',
        'subgenres': {
            'Sony': 120,
            'Bose': 150,
            'Beats': 100
        }
    },
    'tablet': {
        'description': 'A sleek and powerful tablet perfect for reading, browsing, and streaming your favorite content!',
        'price': 500,
        'stock': 15,
        'color': '\033[94m',  # Blue
        'advice': 'If you want a portable entertainment device, this tablet is a great option!',
        'average_money_range': 300,
        'category': 'computer',
        'subgenres': {
            'Apple': 500,
            'Samsung': 400,
            'Amazon': 300
        }
    },
    'smartwatch': {
        'description': 'A stylish smartwatch that tracks your fitness goals and keeps you connected on-the-go!',
        'price': 200,
        'stock': 12,
        'color': '\033[95m',  # Magenta
        'advice': 'If you\'re into fitness, this smartwatch is a great motivator!',
        'average_money_range': 150,
        'category': 'accessory',
        'subgenres': {
            'Apple': 250,
            'Samsung': 200,
            'Fitbit': 150
        }
    },
    'gamingconsole': {
        'description': 'A powerful gaming console with stunning graphics and immersive gameplay. Get ready to level up!',
        'price': 300,
        'stock': 8,
        'color': '\033[91m',  # Red
        'advice': 'If you\'re a gamer, this console is a must-have!',
        'average_money_range': 200,
        'category': 'gaming',
        'subgenres': {
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
            if confirm != 'yes':
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
            total_price = products[user_input]['price'] * quantity
            if account_balance >= total_price:
                products[user_input]['stock'] -= quantity
                account_balance -= total_price
                print(f"\033[92mYou bought {quantity} {subgenre} {user_input}(s) for ${total_price}.\033[0m")
                print(f"Remaining balance: ${account_balance}")
            else:
                print(f"\033[91mInsufficient balance. You need ${total_price}, but you only have ${account_balance}.\033[0m")
        else:
            print(f"\033[91mSorry, we only have {products[user_input]['stock']} {user_input}(s) in stock.\033[0m")
    else:
        print("\033[91mInvalid action. Please type 'info' or 'buy'.\033[0m")
