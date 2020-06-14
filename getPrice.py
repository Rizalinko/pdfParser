#
import sys, os
import pandas as pd

article = '651838001P10'
filename = '2019 Spares - BNR BNA6 EUR V2'

def getDataframe():
    if os.path.exists(filename+'.csv'):
        df = pd.read_csv(filename+'.csv')
    else:
        from tabula import read_pdf
        df = read_pdf(filename+'.pdf' ,pages = 'all')

    return df

def getPrice(df_all):
    for df in df_all:
        try:
            index = df.index[df['Part number'] == article].tolist()[0]
            price = df.iloc[index]['Price EUR']
            print('{} EUR'.format(price))
            break
        except IndexError:
            pass
    return




if __name__ == '__main__':
    df = getDataframe()
    getPrice(df)

