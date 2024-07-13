import openai
import pandas as pd

# Configure OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Load and preprocess ShopWise data
def load_shopwise_data(filepath):
    data = pd.read_csv(filepath)
    data['Transaction_Date'] = pd.to_datetime(data['Transaction Date'])
    data['Month_Year'] = data['Transaction_Date'].dt.to_period('M')
    return data

# Calculate expenditure statistics
def calculate_expenditure(data):
    total_expenditure = data['Total Amount'].sum()
    monthly_expenditure = data.groupby('Month_Year')['Total Amount'].sum()
    return total_expenditure, monthly_expenditure

# Detect spontaneous purchases
def detect_spontaneous_purchases(data):
    data['Spontaneous Purchase'] = data['Decision Time'].apply(lambda t: t < pd.Timedelta(minutes=15))
    spontaneous_purchases = data[data['Spontaneous Purchase']]
    return spontaneous_purchases

# Compile purchasing insights
def compile_insights(data):
    total_expenditure, monthly_expenditure = calculate_expenditure(data)
    spontaneous_purchases = detect_spontaneous_purchases(data)
    return {
        "total_expenditure": total_expenditure,
        "monthly_expenditure": monthly_expenditure,
        "spontaneous_purchases": spontaneous_purchases
    }

# Get a response from the OpenAI API
def request_openai_response(prompt_text):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt_text,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Main function to process data and interact with OpenAI API
def shopwise_assistant(filepath, question):
    data = load_shopwise_data(filepath)
    insights = compile_insights(data)
    
    # Formulate the prompt for the AI response
    prompt = f"""
    You are an AI assistant analyzing ShopWise purchase data for a user. Here are the user's spending details:
    
    Total expenditure: ${insights['total_expenditure']}
    
    Monthly expenditure breakdown:
    {insights['monthly_expenditure']}
    
    Spontaneous purchases:
    {insights['spontaneous_purchases']}
    
    The user asks: "{question}"
    Based on the provided data, offer recommendations and insights for future purchases.
    """
    
    # Obtain a response from the OpenAI API
    response = request_openai_response(prompt)
    return response

# Example usage
filepath = 'shopwise_order_history.csv'
user_question = "Is this a good month to invest in a new tablet?"
response = shopwise_assistant(filepath, user_question)
print(response)
