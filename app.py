from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():

    cryptos = {
        "bitcoin": {"eur": 0, "eur_24h_change": 0},
        "ethereum": {"eur": 0, "eur_24h_change": 0},
        "solana": {"eur": 0, "eur_24h_change": 0},
    }

    try:

        btc_price = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR",
            timeout=10
        ).json()

        eth_price = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=EUR",
            timeout=10
        ).json()

        sol_price = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=SOL&tsyms=EUR",
            timeout=10
        ).json()

        cryptos = {
            "bitcoin": {
                "eur": btc_price.get("EUR", 0),
                "eur_24h_change": 0
            },
            "ethereum": {
                "eur": eth_price.get("EUR", 0),
                "eur_24h_change": 0
            },
            "solana": {
                "eur": sol_price.get("EUR", 0),
                "eur_24h_change": 0
            }
        }

    except Exception as e:
        print("Erreur API :", e)

    labels = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]
    values = [100, 120, 110, 140, 130, 160, 170]

    return render_template(
        "index.html",
        cryptos=cryptos,
        labels=labels,
        values=values
    )


if __name__ == "__main__":
    app.run(debug=True)