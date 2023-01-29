import pandas as pd


filename = "D:\\Kircata\\Python Projects\\MinFin_Analysis\\SEBRA.csv"
data_store = "D:\\Kircata\\Python Projects\\data"

def import_min_fin_raw_data():
    """

    :return: pandas dataframe with expenses from Min_Fin
    """

    df_list = []
    chunksize = 10 ** 6
    with pd.read_csv(filename, chunksize=chunksize) as reader:
        for chunk in reader:
            df_list.append(chunk)

    df = pd.concat(df_list)

    df.to_parquet(data_store)

    return df


if __name__ == "__main__":

    df = import_min_fin_raw_data()
    print(df['SETTLEMENT_DATE'].to_datetime)


