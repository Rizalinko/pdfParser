#
import sys, os
import pandas as pd

article = '950266001P1'
filename = '2019 Spares - BNR BNA6 EUR V2'

def getDataframe():
    if os.path.exists(filename+'.csv'):
        df = pd.read_csv(filename+'.csv')
    else:
        from tabula import read_pdf
        df = read_pdf(filename+'.pdf' ,pages = 'all')
        df = df[0]

    return df

def getPrice(df):
    index = df.index[df['Part number'] == article].tolist()[0]
    price = df.iloc[index]['Price EUR']
    print('{} EUR'.format(price))



if __name__ == '__main__':
    df = getDataframe()
    getPrice(df)

