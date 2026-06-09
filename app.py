from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

DEFAULT_CRYPTOS = {
    "bitcoin": {"eur": 95000, "eur_24h_change": 1.2},
    "ethereum": {"eur": 3200, "eur_24h_change": -0.5},
    "solana": {"eur": 145, "eur_24h_change": 2.1}
}


@app.route("/")
def home():

    cryptos = DEFAULT_CRYPTOS.copy()

    # ==========================
    # PRIX DES CRYPTOS
    # ==========================

    try:

        url = (
            "https://api.coingecko.com/api/v3/simple/price"
            "?ids=bitcoin,ethereum,solana"
            "&vs_currencies=eur"
            "&include_24hr_change=true"
        )

        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            data = response.json()

            cryptos = {
                "bitcoin": {
                    "eur": data.get("bitcoin", {}).get("eur", 95000),
                    "eur_24h_change": data.get("bitcoin", {}).get("eur_24h_change", 0)
                },
                "ethereum": {
                    "eur": data.get("ethereum", {}).get("eur", 3200),
                    "eur_24h_change": data.get("ethereum", {}).get("eur_24h_change", 0)
                },
                "solana": {
                    "eur": data.get("solana", {}).get("eur", 145),
                    "eur_24h_change": data.get("solana", {}).get("eur_24h_change", 0)
                }
            }

    except Exception as e:
        print("Erreur prix :", e)

    # ==========================
    # GRAPHIQUE BITCOIN 7 JOURS
    # ==========================

    labels = []
    values = []

    try:

        chart_url = (
            "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
            "?vs_currency=eur"
            "&days=7"
        )

        response = requests.get(chart_url, timeout=10)

        if response.status_code == 200:

            chart_data = response.json()

            prices = chart_data.get("prices", [])

            for item in prices[::24]:
                timestamp = item[0]
                price = item[1]

                day = datetime.fromtimestamp(
                    timestamp / 1000
                ).strftime("%d/%m")

                labels.append(day)
                values.append(round(price, 2))

    except Exception as e:
        print("Erreur graphique :", e)

    if not values:
        labels = [
            "Lun",
            "Mar",
            "Mer",
            "Jeu",
            "Ven",
            "Sam",
            "Dim"
        ]

        values = [
            cryptos["bitcoin"]["eur"] - 3000,
            cryptos["bitcoin"]["eur"] - 2000,
            cryptos["bitcoin"]["eur"] - 1000,
            cryptos["bitcoin"]["eur"] - 500,
            cryptos["bitcoin"]["eur"],
            cryptos["bitcoin"]["eur"] + 500,
            cryptos["bitcoin"]["eur"] + 1000
        ]

    return render_template(
        "index.html",
        cryptos=cryptos,
        labels=labels,
        values=values
    )


if __name__ == "__main__":
    app.run(debug=True)