import plotly.express as px

def skapa_diagram(manader):
    temperatur_fig = px.line(manader, x="month", y="medeltemp")

    temperatur_fig.update_layout(title= "Medeltemperatur per månad", xaxis_title= "Månad", yaxis_title= "Temperatur (°C)")

    temperatur_html = temperatur_fig.to_html(full_html=False, include_plotlyjs="cdn")

    nederbord_fig = px.bar(manader, x="month", y="nederbord")

    nederbord_fig.update_layout(title= "Nederbörd per månad", xaxis_title= "Månad", yaxis_title= "Nederbörd (mm)")

    nederbord_html = nederbord_fig.to_html(full_html=False, include_plotlyjs="cdn")

    return temperatur_html, nederbord_html
