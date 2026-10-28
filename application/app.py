import requests
from flask import Flask, render_template

from application.analysis import bearbeta_manader, sammanfatta
from application.api import hamta_vader
from application.charts import skapa_diagram

# Skapar flask appen och visar vart templates finns
app = Flask(__name__, template_folder="templates")

# Visar start sidan för vår app
@app.route("/")
def index():
    return render_template("index.html")

# Visar sidan med info om projektet
@app.route("/about")
def about():
    return render_template("about.html")

# Hämtar och analyserar data som visas för användaren på denna sida
@app.route("/dashboard")
def dashboard():
    try:
        # Hämtar väderdata och beräknar statistik per månad.
        data = hamta_vader()
        manader = bearbeta_manader(data)

        # Tar fram de varmaste, kallaste och blötaste månaderna.
        slutsatser = sammanfatta(manader)
        slutsats1 = slutsatser["varmast"]
        slutsats2 = slutsatser["kallast"]
        slutsats3 = slutsatser["blotast"]

        # Skapar diagrammen
        temperatur_html, nederbord_html = skapa_diagram(manader)

    except (requests.exceptions.RequestException, ValueError):
        # Visar ett felmeddelande om väderdatan inte kan hämtas eller användas korrekt.
        return render_template(
            "dashboard.html", error="Väderdata kunde inte hämtas."
        ), 503

    # Skickar statistiken och diagrammen till jinja2 så de kan användas i mallar.
    return render_template(
        "dashboard.html",
        temperatur_html=temperatur_html,
        nederbord_html=nederbord_html,
        slutsats1=slutsats1,
        slutsats2=slutsats2,
        slutsats3=slutsats3,
    )

# Startar Flask om filen körs direkt
if __name__ == "__main__":
    app.run(debug=True)
