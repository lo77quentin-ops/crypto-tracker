from flask import Flask, render_template
import requests

app = Flask(__name__)

# Valeurs de secours
DEFAULT_CRYPTOS = {
    "bitcoin": {
        "eur": 95000,
        "eur_24h_change": 1.2
    },
    "ethereum": {
        "eur": 3200,
        "eur_24h_change": -0.5
    },
    "solana": {
        "eur": 145,
        "eur_24h_change": 2.1
    }
}


@app.route("/")
def home():

    cryptos = DEFAULT_CRYPTOS.copy()

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
        print("Erreur API :", e)

    # Graphique toujours affiché
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
        92000,
        93000,
        92500,
        94000,
        95000,
        94500,
        96000
    ]

    return render_template(
        "index.html",
        cryptos=cryptos,
        labels=labels,
        values=values
    )


if __name__ == "__main__":
    app.run(debug=True)