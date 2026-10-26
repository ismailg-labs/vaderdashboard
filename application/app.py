from application.api import hamta_vader
from application.charts import skapa_diagram
from application.analysis import bearbeta_manader, sammanfatta
from flask import Flask, render_template
import requests

 
app = Flask (__name__,template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dashboard")
def dashboard():
    try:
        data = hamta_vader()
        manader = bearbeta_manader(data)
        slutsats1, slutsats2, slutsats3 = sammanfatta(manader)
        temperatur_html, nederbord_html = skapa_diagram(manader)
    except (requests.exceptions.RequestException, ValueError): 
        return render_template("dashboard.html", error="Väderdata kunde inte hämtas."),

    
    return render_template(
            "dashboard.html",
            temperatur_html=temperatur_html,
            nederbord_html=nederbord_html,
            slutsats1=slutsats1,
            slutsats2=slutsats2,
            slutsats3=slutsats3,    
        )


if __name__ == "__main__":
    app.run(debug=True)