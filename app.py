from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():

    cryptos = {
        "bitcoin": {
            "eur": 53524,
            "eur_24h_change": -2.16
        },
        "ethereum": {
            "eur": 1442,
            "eur_24h_change": -0.92
        },
        "solana": {
            "eur": 57,
            "eur_24h_change": -1.42
        },
        "dogecoin": {
            "eur": 0.14,
            "eur_24h_change": 1.20
        },
        "cardano": {
            "eur": 0.52,
            "eur_24h_change": -0.75
        },
        "ripple": {
            "eur": 1.95,
            "eur_24h_change": 0.84
        }
    }

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
        55000,
        54800,
        54650,
        54400,
        54100,
        53850,
        53524
    ]

    return render_template(
        "index.html",
        cryptos=cryptos,
        labels=labels,
        values=values
    )


if __name__ == "__main__":
    app.run(debug=True)