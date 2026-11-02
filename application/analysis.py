import pandas as pd  # pandas för tabeller och uträkningar


def bearbeta_manader(data):  # räknar ihop väderdatan per månad
    # gör om den dagliga datan till en tabell
    daily = data["daily"]
    df = pd.DataFrame(daily)

    df["time"] = pd.to_datetime(
        df["time"]
    )  # gör om det från text till datumformat och plockar ut månaden
    df["month"] = df["time"].dt.month

    df = df.dropna(
        subset=["temperature_2m_mean", "precipitation_sum"]
    )  # dropna tar bort dagar där temperatur eller nederbörd saknas

    if df.empty:  # ger ett fel om ingen data finns kvar
        raise ValueError("Ingen väderdata tillgänglig")

    manad = df.groupby(
        "month", as_index=False
    ).agg(  # groupby samlar alla dagar som hör till samma månad
        medeltemp=("temperature_2m_mean", "mean"),  # snittet av temperaturen
        nederbord=("precipitation_sum", "sum"),  # all nederbörd ihoplagd
    )

    return manad


# hittar varmaste,kallaste och månaden med högst nederbörd
def sammanfatta(manader):
    varmast = manader.loc[
        manader["medeltemp"].idxmax(), "month"
    ]  # använde idmax hittar raden med största värdet
    kallast = manader.loc[
        manader["medeltemp"].idxmin(), "month"
    ]  # idmin hittar raden med minsta värdet.
    blotast = manader.loc[manader["nederbord"].idxmax(), "month"]

    # skickar tillbaka månadsnummer
    return {"varmast": int(varmast), "kallast": int(kallast), "blotast": int(blotast)}
