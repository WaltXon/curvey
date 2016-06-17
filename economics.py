import pandas as pd

from config import config
from volumes import volumes
from pricing import pricing

vol=volumes()
prices=pricing()

gross=pd.concat([vol, prices], axis=1)
gross['gross_sales_oil']=gross['gross_volume_oil']*gross['price_oil']
gross['gross_sales_gas']=gross['gross_volume_gas']*gross['price_gas']
# gross['gross_sales_ngl']=gross['gross_volume_ngl']*gross['price_ngl']