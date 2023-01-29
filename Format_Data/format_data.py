import  pandas as pd

from Source_Data.Import_Raw_Data import import_min_fin_raw_data

def expenses_by_year_organization(expenses):
    """
    Get raw expense data and return summarized expenses by organization within MinFin by year
    :return: dataframe
    """

    expenses["SETTLEMENT_YEAR"] = expenses['SETTLEMENT_DATE'].dt.strftime('%Y')
    expenses["REG_YEAR"] = expenses['REG_DATE'].dt.strftime('%YYYY')

    return df


if __name__ == "__main__":
    expenses = import_min_fin_raw_data()
    df = expenses_by_year_organization(expenses)
    print(df.head)