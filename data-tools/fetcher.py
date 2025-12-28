import requests

def fetch_prices(symbol="AAPL"):
    url = f"https://api.example.com/prices/{symbol}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("API error")

    return response.json()

if __name__ == "__main__":
    print(fetch_prices())
