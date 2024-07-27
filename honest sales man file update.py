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

