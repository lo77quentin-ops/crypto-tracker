from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():

    cryptos = {}

    try:
        price_url = (
            "https://api.coingecko.com/api/v3/simple/price"
            "?ids=bitcoin,ethereum,solana"
            "&vs_currencies=eur"
            "&include_24hr_change=true"
        )

        response = requests.get(price_url, timeout=10)
        data = response.json()

        cryptos = {
            "bitcoin": {
                "eur": data["bitcoin"]["eur"],
                "eur_24h_change": data["bitcoin"].get("eur_24h_change", 0)
            },
            "ethereum": {
                "eur": data["ethereum"]["eur"],
                "eur_24h_change": data["ethereum"].get("eur_24h_change", 0)
            },
            "solana": {
                "eur": data["solana"]["eur"],
                "eur_24h_change": data["solana"].get("eur_24h_change", 0)
            }
        }

    except Exception as e:
        print("Erreur CoinGecko :", e)

        cryptos = {
            "bitcoin": {"eur": 0, "eur_24h_change": 0},
            "ethereum": {"eur": 0, "eur_24h_change": 0},
            "solana": {"eur": 0, "eur_24h_change": 0},
        }

    # Données de démonstration pour le graphique
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