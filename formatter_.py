import pandas as pd
from io import StringIO

mods  = ['cc', 'dm', 'hc',  'md', 'pl', 'cold order']
path = '/Users/home/Downloads/'
filename = 'menu-breakdown-jul8-8-2023.csv'


# df = pd.read_csv(path+filename)
# df.reset_index(inplace=True)
# df = df.tail(-2)
# df = df[['Item Name','Modifier','Menu Group','Avg Price']]
# mapping = {
#     'Modifier':'Avg Price',
#     'Menu Group':'Item Name',
#     'Item Name':'Modifier',
#     'Avg Price':'Quantity'}
# df.rename(columns=mapping, inplace=True)

# df.fillna(method='ffill', inplace=True)
# # prices = df[df['Avg Price'].isnull()==False]
# # print(prices)

# df = df[df['Modifier'].str.lower().isin(mods)]

# df.to_csv('test.csv')
# print(df['Modifier'].unique())

def convert(file):
    print('starting conversion..')
    df = pd.read_csv(file)
    df.reset_index(inplace=True)
    df = df.tail(-2)
    df = df[['Item Name','Modifier','Menu Group','Avg Price']]
    mapping = {
        'Modifier':'Avg Price',
        'Menu Group':'Item Name',
        'Item Name':'Modifier',
        'Avg Price':'Quantity'}
    df.rename(columns=mapping, inplace=True)

    df.fillna(method='ffill', inplace=True)
    # prices = df[df['Avg Price'].isnull()==False]
    # print(prices)

    df = df[df['Modifier'].str.lower().isin(mods)]
    print('fin...')
    return df.to_csv()