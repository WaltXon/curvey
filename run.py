import pandas as pd

from arps import arps_hyp
from config import config
from functions import get_products, annual_to_monthly_rate
from templates import volumes

products=get_products()

for product in products:
    for t in range(0,config['economic_life_max']):
        volume=arps_hyp(config['curves'][product]['QiPerMonth'],
            annual_to_monthly_rate(config['curves'][product]['DiPerYear']),
            config['curves'][product]['b'],
            t)
        volumes[product].append(volume)




