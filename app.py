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
            "eur_24h_change": 1.35
        },
        "cardano": {
            "eur": 0.52,
            "eur_24h_change": -0.74
        },
        "ripple": {
            "eur": 1.95,
            "eur_24h_change": 0.88
        }
    }

    labels = [
        "03/06",
        "04/06",
        "05/06",
        "06/06",
        "07/06",
        "08/06",
        "09/06"
    ]

    values = [
        55200,
        54850,
        54600,
        54350,
        54000,
        53750,
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