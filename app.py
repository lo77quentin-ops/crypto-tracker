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
        btc = requests.get(
            "https://api.coincap.io/v2/assets/bitcoin",
            timeout=10
        ).json()["data"]

        eth = requests.get(
            "https://api.coincap.io/v2/assets/ethereum",
            timeout=10
        ).json()["data"]

        sol = requests.get(
            "https://api.coincap.io/v2/assets/solana",
            timeout=10
        ).json()["data"]

        cryptos = {
            "bitcoin": {
                "eur": round(float(btc["priceUsd"]) * 0.87, 2),
                "eur_24h_change": float(btc["changePercent24Hr"])
            },
            "ethereum": {
                "eur": round(float(eth["priceUsd"]) * 0.87, 2),
                "eur_24h_change": float(eth["changePercent24Hr"])
            },
            "solana": {
                "eur": round(float(sol["priceUsd"]) * 0.87, 2),
                "eur_24h_change": float(sol["changePercent24Hr"])
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