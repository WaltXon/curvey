import pandas as pd

from arps import arps_hyp_rate
from phd import rate_at_t, cum_at_t, effective_decline_annual, nominal_decline_annual
from config import config
from functions import get_products, annual_to_monthly_rate
from templates import volumes

products=get_products()

date_series=pd.date_range(config['start_date'], periods=config['max_life_months'], freq='M')

df = pd.DataFrame(index=date_series)

df['date']=df.index
df['days_in_month']=df.index.days_in_month
df['days_since_start']=df['days_in_month'].cumsum()
df['standard_time']=df['days_since_start']/(config['standard_days_in_year']/12.0)

volumes={}

for product in products:
    volumes[product]={}
    rate=[config['curves'][product]['Qi_monthly'],]
    cumulative=[0.0,]
    time=[0.0]
    for row in df.iterrows():
        volumes[product][row[1]['date']]['days_in_month']=row[1]['days_in_month']
        volumes[product][row[1]['date']]['days_since_start']=row[1]['days_since_start']
        volumes[product][row[1]['date']]['standard_time']=row[1]['standard_time']
        volumes[product][row[1]['date']]['initial_rate']=rate[-1]
        volumes[product][row[1]['date']]['period_end_rate']=rate_at_t(config['curves'][product]['nominal_decline_monthly'],
            config['curves'][product]['Qi_monthly'],
            rate[-1],
            config['curves'][product]['b_factor'],
            config['curves'][product]['b_factor_adj'],
            config['curves'][product]['Dmin_monthly'],
            row[1]['standard_time'])
        volumes[product][row[1]['date']]['cum_prod']=cum_at_t(
            config['curves'][product]['nominal_decline_monthly'],
            config['curves'][product]['Qi_monthly'],
            rate[-1],
            config['curves'][product]['b_factor'],
            config['curves'][product]['b_factor_adj'],
            config['curves'][product]['Dmin_monthly'],
            row[1]['standard_time'],
            time[-1],
            cumulative[-1])
        volumes[product][row[1]['date']]['volume_produced']=volumes[product][row['date']]['volume_produced'][-1]-cumulative[-1]
        volumes[product][row[1]['date']]['nominal_decline_annual']=nominal_decline_annual(
            config['curves'][product]['nominal_decline_annual'],
            rate[-1],
            config['curves'][product]['Qi_monthly'],
            config['curves'][product]['b_factor'],
            config['curves'][product]['Dmin_annual'])
        volumes[product][row[1]['date']]['effective_decline_annual']=effective_decline_annual(
            config['curves'][product]['nominal_decline_annual'])
        rate.append(volumes[product][row[1]['date']]['period_end_rate'][-1])
        cumulative.append(volumes[product][row[1]['date']]['cum_prod'])
        time.append(volumes[product][row[1]['date']]['standard_time'][-1])


