from flask import Flask, render_template
from api import hamta_vader
from charts import skapa_diagram
from analysis import bearbeta_manader, sammanfatta
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
    data = hamta_vader()
    manader = bearbeta_manader(data)
    slutsats1, slutsats2, slutsats3 = sammanfatta(manader)
    diagram_temp, diagram_nederbord = skapa_diagram(manader)

    return render_template(
        "dashboard.html",
        diagram_temp=diagram_temp,
        diagram_nederbord=diagram_nederbord,
        slutsats1=slutsats1,
        slutsats2=slutsats2,
        slutsats3=slutsats3,    
    )


if __name__ == "__main__":
    app.run(debug=True)



