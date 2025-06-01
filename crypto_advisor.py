# CryptoBuddy - Your AI-Powered Financial Sidekick! 🌟

# Sample cryptocurrency database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def get_sustainable_crypto():
    """Find the most sustainable cryptocurrency."""
    return max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])

def get_trending_crypto():
    """Find cryptocurrencies with rising price trends."""
    return [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]

def get_profitable_recommendation():
    """Recommend coins based on profitability metrics."""
    return [coin for coin, data in crypto_db.items() 
            if data["price_trend"] == "rising" and data["market_cap"] == "high"]

def get_sustainable_recommendation():
    """Recommend coins based on sustainability metrics."""
    return [coin for coin, data in crypto_db.items() 
            if data["energy_use"] == "low" and data["sustainability_score"] > 0.7]

def process_query(user_input):
    """Process user queries and provide appropriate responses."""
    user_input = user_input.lower()
    
    # Add disclaimer to all responses
    disclaimer = "\n⚠️ Disclaimer: Crypto investments are risky—always do your own research!"
    
    if "sustainable" in user_input or "green" in user_input:
        sustainable_coin = get_sustainable_crypto()
        return f"🌱 {sustainable_coin} is our most eco-friendly option with excellent sustainability metrics!" + disclaimer
    
    elif "trending" in user_input or "rising" in user_input:
        trending_coins = get_trending_crypto()
        return f"📈 These coins are trending up: {', '.join(trending_coins)}!" + disclaimer
    
    elif "profitable" in user_input or "growth" in user_input:
        profitable_coins = get_profitable_recommendation()
        if profitable_coins:
            return f"💰 For profitability, consider: {', '.join(profitable_coins)}. They show strong market performance!" + disclaimer
        return "🤔 No coins currently meet our strict profitability criteria." + disclaimer
    
    else:
        return "👋 I can help you find sustainable and profitable crypto investments! Try asking about:\n- Trending cryptocurrencies\n- Sustainable options\n- Growth potential" + disclaimer

def main():
    print("🤖 Hello! I'm CryptoBuddy, your AI crypto advisor!")
    print("💡 Ask me about sustainable or profitable cryptocurrency investments!")
    print("❓ Type 'exit' to end our conversation.\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("\n👋 Thanks for chatting! Remember to invest wisely!")
            break
        
        response = process_query(user_input)
        print(f"\nCryptoBuddy: {response}\n")

if __name__ == "__main__":
    main()