import pandas as pd   #importera pandas


def bearbeta_manader(data):   #skapade funktion 
    daily = data["daily"]
    df = pd.DataFrame(daily)

    df["time"] = pd.to_datetime(df["time"])         #gör om datumen från text till datumformat
    df["month"] = df["time"].dt.month               

    df = df.dropna(subset=["temperature_2m_mean", "precipitation_sum"])  #tar bort raderna där nederbörd eller temp saknas med subset

    if df.empty:
        raise ValueError("Ingen väderdata tillgänglig")          

    manad = df.groupby("month", as_index=False).agg(       #delade upp raderna med groupby 
        medeltemp=("temperature_2m_mean", "mean"),
        nederbord=("precipitation_sum", "sum"),
    )

    return manad


def sammanfatta(manader):
    varmast = manader.loc[manader["medeltemp"].idxmax(), "month"]          #använde idmax hittar raden med största värdet
    kallast = manader.loc[manader["medeltemp"].idxmin(), "month"]          #idmin hittar raden med minsta värdet.
    blotast = manader.loc[manader["nederbord"].idxmax(), "month"]         

    return {"varmast": int(varmast), "kallast": int(kallast), "blotast": int(blotast)}  
