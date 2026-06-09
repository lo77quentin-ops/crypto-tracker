from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():

    cryptos = {
        "bitcoin": {"eur": 53524, "eur_24h_change": -2.16},
        "ethereum": {"eur": 1442, "eur_24h_change": -0.92},
        "solana": {"eur": 57, "eur_24h_change": -1.42},
        "dogecoin": {"eur": 0.14, "eur_24h_change": 1.35},
        "cardano": {"eur": 0.52, "eur_24h_change": -0.74},
        "ripple": {"eur": 1.95, "eur_24h_change": 0.88}
    }

    labels = [
        "03/06", "04/06", "05/06",
        "06/06", "07/06", "08/06", "09/06"
    ]

    values = [
        55200, 54850, 54600,
        54350, 54000, 53750, 53524
    ]

    cities = {
        "Paris": (48.8566, 2.3522),
        "Marseille": (43.2965, 5.3698),
        "Lyon": (45.7640, 4.8357),
        "Toulouse": (43.6047, 1.4442),
        "Nice": (43.7102, 7.2620),
        "Nantes": (47.2184, -1.5536),
        "Lille": (50.6292, 3.0573),
        "Strasbourg": (48.5734, 7.7521)
    }

    weather = []

    for city, (lat, lon) in cities.items():
        try:
            url = (
                f"https://api.open-meteo.com/v1/forecast"
                f"?latitude={lat}"
                f"&longitude={lon}"
                f"&current=temperature_2m"
            )

            data = requests.get(url, timeout=5).json()

            weather.append({
                "city": city,
                "temp": round(data["current"]["temperature_2m"])
            })

        except Exception:
            weather.append({
                "city": city,
                "temp": "N/A"
            })

    return render_template(
        "index.html",
        cryptos=cryptos,
        labels=labels,
        values=values,
        weather=weather
    )


if __name__ == "__main__":
    app.run(debug=True)