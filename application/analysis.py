import pandas as pd

def bearbeta_manader(data):
    daily = data ["daily"]
    df = pd.DataFrame(daily)

    df ["time"] = pd.to_datetime(df["time"])
    df ["month"] = df ["time"].dt.month

    df = df.dropna (
        subset = ["temperature_2m_mean" , "precipitation_sum"]
    )

    if df.empty:
        raise ValueError("Ingen väderdata tillgänglig")

    manad = df.groupby("month", as_index=False).agg(
        medeltemp = ("temperature_2m_mean", "mean"),
        nederbord = ("precipitation_sum", "sum"),
    )

    return manad

def sammanfatta (manader):
    varmast = manader.loc[manader["medeltemp"].idxmax(), "month"]
    kallast = manader.loc[manader["medeltemp"].idxmin(), "month"]
    blotast = manader.loc[manader["nederbord"].idxmax(), "month"]

    return {
        "varmast": int(varmast),
        "kallast": int(kallast),
        "blotast": int(blotast)
    }






    

