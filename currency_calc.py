import requests

def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if to_currency.upper() in data['rates']:
            rate = data['rates'][to_currency.upper()]
            converted = amount * rate
            print(f"\n💱 {amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
        else:
            print("❌ Currency not supported.")
    except Exception as e:
        print("❌ Error fetching data:", e)

if __name__ == "__main__":
    print("🌍 Currency Converter")
    from_currency = input("From currency (e.g., USD): ")
    to_currency = input("To currency (e.g., INR): ")

    try:
        amount = float(input("Amount: "))
        convert_currency(from_currency, to_currency, amount)
    except ValueError:
        print("Please enter a valid number.")
