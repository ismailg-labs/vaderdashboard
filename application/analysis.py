import pandas as pd

def bearbeta_manader(data):
    daily = data ["daily"]
    df = pd.DataFrame(daily)

    df ["time"] = pd.to_datetime(df["time"])
    df ["months"] = df ["time"].dt.month

    df = df.dropna (
        subset = ["temperature_2m_mean" , "precipitation_sum"]
    )

    if df.empty:
        raise ValueError("Ingen väderdata tillgänglig")

    manad = df.groupby("months", as_index=False).agg(
        medeltemp = ("temperature_2m_mean", "mean"),
        nederbord = ("precipitation_sum", "sum"),
    )

    return manad


    

