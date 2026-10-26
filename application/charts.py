import plotly.express as px


def skapa_diagram(manader):
    manader = manader.copy()

    manadsnamn = [
        "Jan", "Feb", "Mar", "Apr", "Maj", "Jun",
        "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"
    ]

    temperatur_fig = px.line(
        manader,
        x="month",
        y="medeltemp",
        markers=True
    )

    temperatur_fig.update_layout(
        title="Medeltemperatur per månad",
        xaxis_title="Månad",
        yaxis_title="Temperatur (°C)",
        template="plotly_dark",
        hovermode="x unified"
    )

    temperatur_fig.update_xaxes(
        tickmode="array",
        tickvals=list(range(1, 13)),
        ticktext=manadsnamn,
        dtick=1
    )

    temperatur_fig.update_traces(
        hovertemplate="%{y:.1f} °C<extra></extra>"
    )

    temperatur_html = temperatur_fig.to_html(
        full_html=False,
        include_plotlyjs="cdn"
    )

    nederbord_fig = px.bar(
        manader,
        x="month",
        y="nederbord"
    )

    nederbord_fig.update_layout(
        title="Nederbörd per månad",
        xaxis_title="Månad",
        yaxis_title="Nederbörd (mm)",
        template="plotly_dark"
    )

    nederbord_fig.update_xaxes(
        tickmode="array",
        tickvals=list(range(1, 13)),
        ticktext=manadsnamn
    )

    nederbord_fig.update_traces(
        hovertemplate="%{y:.1f} mm<extra></extra>"
    )

    nederbord_html = nederbord_fig.to_html(
        full_html=False,
        include_plotlyjs="cdn"
    )

    return temperatur_html, nederbord_html