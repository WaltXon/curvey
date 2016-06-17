import datetime
import pandas as pd
from config import config

oil_file=r'C:\Users\WaltN\Desktop\GitHub\curvey\output\oil_prices.xlsx'
gas_file=r'C:\Users\WaltN\Desktop\GitHub\curvey\output\gas_prices.xlsx'

def dump_prices():
    oil=pd.DataFrame([x[1] for x in config['price_oil'].items()], index=[x[0] for x in config['price_oil'].items()])
    oil.to_excel(oil_file)
    oil=pd.DataFrame([x[1] for x in config['price_gas'].items()], index=[x[0] for x in config['price_gas'].items()])
    oil.to_excel(gas_file)


def update_oil_prices():
    oil=pd.read_excel(oil_file)
    oil_working=oil.to_dict()
    oil_new={}
    for k,v in oil_working[0].iteritems():
        if type(k)==datetime.datetime:
            oil_new[datetime.datetime.strftime(k, '%m/%d/%Y')]=round(v,2)
        elif type(k)==unicode:
            oil_new[str(k)]=round(v,2)
        else:
            oil_new[k]=round(v,2)
    #config['price_oil']=oil_new

def update_gas_prices():
    gas=pd.read_excel(gas_file)
    gas_working=oil.to_dict()
    gas_new={}
    for k,v in gas_working[0].iteritems():
        if type(k)==datetime.datetime:
            gas_new[datetime.datetime.strftime(k, '%m/%d/%Y')]=round(v,2)
        elif type(k)==unicode:
            gas_new[str(k)]=round(v,2)
        else:
            gas_new[k]=round(v,2)
    #config['price_gas']=new_gas

def update_prices():
    update_oil_prices()
    update_gas_prices()