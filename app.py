from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():

    # =========================
    # PRIX DES CRYPTOS
    # =========================

    cryptos = {}

    try:
        price_url = (
            "https://api.coingecko.com/api/v3/simple/price"
            "?ids=bitcoin,ethereum,solana,dogecoin,cardano,ripple"
            "&vs_currencies=eur"
            "&include_24hr_change=true"
        )

        response = requests.get(price_url, timeout=10)

        data = response.json()

        # Si CoinGecko renvoie une erreur
        if "status" in data:
            raise Exception(f"CoinGecko error: {data}")

        cryptos = data

        # Sécurise eur_24h_change
        for crypto in cryptos:
            cryptos[crypto].setdefault("eur_24h_change", 0)

    except Exception as e:

        print("Erreur CoinGecko :", e)

        cryptos = {
            "bitcoin": {"eur": 0, "eur_24h_change": 0},
            "ethereum": {"eur": 0, "eur_24h_change": 0},
            "solana": {"eur": 0, "eur_24h_change": 0},
            "dogecoin": {"eur": 0, "eur_24h_change": 0},
            "cardano": {"eur": 0, "eur_24h_change": 0},
            "ripple": {"eur": 0, "eur_24h_change": 0},
        }

    # =========================
    # GRAPHIQUE BITCOIN
    # =========================

    labels = []
    values = []

    try:

        chart_url = (
            "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
            "?vs_currency=eur"
            "&days=7"
        )

        response = requests.get(chart_url, timeout=10)

        chart_data = response.json()

        if "status" in chart_data:
            raise Exception(f"CoinGecko graph error: {chart_data}")

        prices = chart_data.get("prices", [])

        for item in prices[::20]:
            labels.append("")
            values.append(round(item[1], 2))

        if not values:
            labels = ["Aucune donnée"]
            values = [0]

    except Exception as e:

        print("Erreur graphique :", e)

        labels = ["Aucune donnée"]
        values = [0]

    return render_template(
        "index.html",
        cryptos=cryptos,
        labels=labels,
        values=values
    )


if __name__ == "__main__":
    app.run(debug=True)